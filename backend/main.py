import os
from pathlib import Path
from typing import Literal

import bcrypt
import psycopg
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from psycopg.rows import dict_row
from pydantic import BaseModel, Field

load_dotenv()

app = FastAPI()


class RegisterIn(BaseModel):
    name: str = Field(min_length=1)
    email: str = Field(min_length=1)
    password: str = Field(min_length=1)
    role: Literal["buyer", "seller"]


def connect():
    return psycopg.connect(os.environ["DATABASE_URL"], row_factory=dict_row)


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


# keep mount last
app.mount("/", StaticFiles(directory=Path(__file__).parent.parent / "frontend", html=True), name="frontend")
