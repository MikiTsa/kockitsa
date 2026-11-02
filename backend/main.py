import os
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


def connect():
    return psycopg.connect(os.environ["DATABASE_URL"], row_factory=dict_row)


def user(request: Request, *roles):
    if "user_id" not in request.session:
        raise HTTPException(401, "Niste prijavljeni")
    if roles and request.session["role"] not in roles:
        raise HTTPException(403, "Dejanje ni dovoljeno za vašo vlogo")
    return request.session["user_id"]


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


# keep mount last
app.mount("/", StaticFiles(directory=Path(__file__).parent.parent / "frontend", html=True), name="frontend")
