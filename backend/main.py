import os
from decimal import Decimal
from pathlib import Path
from typing import Literal

import bcrypt
import psycopg
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from psycopg.rows import dict_row
from pydantic import BaseModel, Field
from starlette.middleware.sessions import SessionMiddleware

load_dotenv()

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ["SECRET_KEY"])


class RegisterIn(BaseModel):
    name: str = Field(min_length=1)
    email: str = Field(min_length=1)
    password: str = Field(min_length=1)
    role: Literal["buyer", "seller"]


class LoginIn(BaseModel):
    email: str
    password: str


class ListingIn(BaseModel):
    set_id: int
    condition: Literal["sealed", "new", "used"]
    price: Decimal = Field(gt=0, max_digits=10, decimal_places=2)
    description: str | None = None


def connect():
    return psycopg.connect(os.environ["DATABASE_URL"], row_factory=dict_row)


def user(request: Request, *roles):
    if "user_id" not in request.session:
        raise HTTPException(401, "Niste prijavljeni")
    if roles and request.session["role"] not in roles:
        raise HTTPException(403, "Dejanje ni dovoljeno za vašo vlogo")
    return request.session["user_id"]


def change(sql, params):
    with connect() as conn:
        if conn.execute(sql, params).rowcount == 0:
            raise HTTPException(409, "Oglas ne obstaja ali dejanje ni dovoljeno")


@app.post("/register", status_code=201)
def register(data: RegisterIn):
    password_hash = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt()).decode()
    try:
        with connect() as conn:
            conn.execute(
                "INSERT INTO users (name, email, password_hash, role) "
                "VALUES (%s, %s, %s, %s)",
                (data.name, data.email, password_hash, data.role),
            )
    except psycopg.errors.UniqueViolation:
        raise HTTPException(409, "Račun s tem e-poštnim naslovom že obstaja")


@app.post("/login")
def login(data: LoginIn, request: Request):
    with connect() as conn:
        row = conn.execute(
            "SELECT id, name, role, password_hash "
            "FROM users "
            "WHERE email = %s",
            (data.email,),
        ).fetchone()
    if not row or not bcrypt.checkpw(data.password.encode(), row["password_hash"].encode()):
        raise HTTPException(401, "Napačna e-pošta ali geslo")
    request.session.update(user_id=row["id"], name=row["name"], role=row["role"])
    return {"name": row["name"], "role": row["role"]}


@app.post("/logout")
def logout(request: Request):
    request.session.clear()


@app.get("/me")
def me(request: Request):
    if "user_id" not in request.session:
        return None
    return {"name": request.session["name"], "role": request.session["role"]}


@app.get("/sets")
def search_sets(q: str = ""):
    with connect() as conn:
        return conn.execute(
            "SELECT id, set_number, name, theme, piece_count, release_year "
            "FROM sets "
            "WHERE set_number ILIKE %s OR name ILIKE %s "
            "ORDER BY name "
            "LIMIT 20",
            (f"%{q}%", f"%{q}%"),
        ).fetchall()


@app.post("/listings", status_code=201)
def create_listing(listing: ListingIn, request: Request):
    seller_id = user(request, "seller")
    try:
        with connect() as conn:
            return conn.execute(
                "INSERT INTO listings (set_id, seller_id, condition, price, description) "
                "VALUES (%s, %s, %s, %s, %s) "
                "RETURNING id, status",
                (listing.set_id, seller_id, listing.condition, listing.price, listing.description or None),
            ).fetchone()
    except psycopg.errors.ForeignKeyViolation:
        raise HTTPException(404, "Komplet ni v katalogu")


@app.get("/my/listings")
def my_listings(request: Request):
    seller_id = user(request, "seller")
    with connect() as conn:
        return conn.execute(
            "SELECT l.id, s.set_number, s.name AS set_name, l.condition, l.price, l.status, l.created_at "
            "FROM listings l "
            "JOIN sets s ON s.id = l.set_id "
            "WHERE l.seller_id = %s "
            "ORDER BY l.created_at DESC",
            (seller_id,),
        ).fetchall()


@app.get("/admin/listings")
def pending_listings(request: Request):
    user(request, "admin")
    with connect() as conn:
        return conn.execute(
            "SELECT l.id, s.set_number, s.name AS set_name, s.theme, s.piece_count, s.release_year, "
            "l.condition, l.price, l.description, u.name AS seller_name, l.created_at "
            "FROM listings l "
            "JOIN sets s ON s.id = l.set_id "
            "JOIN users u ON u.id = l.seller_id "
            "WHERE l.status = 'pending' "
            "ORDER BY l.created_at"
        ).fetchall()


@app.post("/listings/{listing_id}/approve")
def approve(listing_id: int, request: Request):
    user(request, "admin")
    change(
        "UPDATE listings "
        "SET status = 'approved' "
        "WHERE id = %s AND status = 'pending'",
        (listing_id,),
    )


# keep mount last
app.mount("/", StaticFiles(directory=Path(__file__).parent.parent / "frontend", html=True), name="frontend")
