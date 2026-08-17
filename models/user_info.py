from pydantic import BaseModel


class UserRegisterInfo(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: str
    email: str
    username: str
    password: str


class UserLoginInfo(BaseModel):
    username: str
    password: str


class UserInfo(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str
    username: str
    role: str


class TokenInfo(BaseModel):
    access_token: str
    role: str
