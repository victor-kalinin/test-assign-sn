from typing import Any
from datetime import datetime

from pydantic import BaseModel


class LikeBase(BaseModel):
    is_like: bool
    post_id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True


class LikeGroup(BaseModel):
    date_group: Any
    count: int
