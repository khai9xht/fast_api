from pydantic import BaseModel
from typing import Optional


class BaseUser(BaseModel):
    email: str
    username: str
    priority: int


class UserCreate(BaseUser):
    password:str


class User(BaseUser):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str 
    token_type: str = 'Bearer'

class ItemCreate(BaseModel):
    name: str
    amount: int
    price: float
