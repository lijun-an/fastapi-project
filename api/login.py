from pydantic import BaseModel
from core.Auth import create_access_token


def register(age: int):
    return {'age': age}


def login(data: dict):
    token = create_access_token(data)
    return {"token": token}
