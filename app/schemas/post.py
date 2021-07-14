from typing import Optional, List
from datetime import datetime

from .orm import OrmBase
from .user import UserBase


class PostBase(OrmBase):
    id: Optional[int]
    title: str


class PostCreate(PostBase):
    context: str

    class Config:
        schema_extra = {
            "example": {
                "title": "API is a new web framework",
                "context": "Just any text"
            }
        }


class Post(PostCreate):
    author: Optional[UserBase] = None
    created_at: datetime
    likes: List[UserBase] = []

    class Config:
        orm_mode = True
