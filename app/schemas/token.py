from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: Optional[str]


class TokenData(BaseModel):
    email: str
    expire: datetime
