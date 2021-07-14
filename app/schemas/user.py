from typing import Optional
from datetime import datetime

from pydantic import EmailStr

from .orm import OrmBase


class UserBase(OrmBase):
    id: Optional[int]
    fullname: str
    email: EmailStr


class UserCreate(UserBase):
    password: str

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Victor Kalinin",
                "email": "victor.kalinin@example.com",
                "password": "StRon9Pa$$w0rd"
            }
        }


class User(UserBase):
    hashed_password: str


class UserActivity(UserBase):
    created_at: datetime
    login_at: datetime
    been_active_at: datetime
