from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: str


def register(age: int):
    return {'age': age}


def login(data: Login):
    return '登录'
