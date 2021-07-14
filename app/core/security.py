from typing import Optional
from datetime import datetime, timedelta

from passlib.context import CryptContext
from jose import JWTError, jwt

from app.core.config import settings
from app.schemas.token import TokenData

from . import exceptions


ALGORITHM: str = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"expire": str(expire)})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_decoded_by_token(token: str):
    try:
        token_data = TokenData(**jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM]))
    except JWTError:
        raise exceptions.CREDENTIALS_EXCEPTION
    if token_data.expire < datetime.utcnow():
        raise exceptions.TOKEN_EXCEPTION
    return token_data
