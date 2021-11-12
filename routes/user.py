from fastapi import APIRouter, Response, status
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from models.user import users
from schemas.user import User

from cryptography.fernet import Fernet

key = Fernet.generate_key()  # => generate key for password
f = Fernet(key)

user = APIRouter()


@user.get("/users", response_model=list[User], tags=["users"])
def get_users():
    return conn.execute(users.select()).fetchall()


@user.post("/users", response_model=User, description="Create a new user",tags=["users"])
def create_user(user: User):
    new_user = {"name": user.name, "email": user.email}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    # print(new_user) -> Test
    result = conn.execute(users.insert().values(new_user))
    # print(result.lastrowid) -> Test
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()


@user.get("/users/{id}", response_model=User, tags=["users"])
def get_user(id: str):
    # print(id) -> Test
    return conn.execute(users.select().where(users.c.id == id)).first()
    # example http://localhost:8000/users1


@user.delete("/users{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
def delete_user(id: str):
    conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)  # response => deleted


@user.put("/users/{id}", response_model=User, description="Update a user by ID", tags=["users"])
def update_user(id: str, user: User):
    conn.execute(users.update().values(name=user.name,
                                       email=user.email,
                                       password=f.encrypt(
                                           user.password.encode("utf-8"))
                                       ).where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).first()
