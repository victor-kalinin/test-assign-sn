from typing import Generator

from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

from app.db.session import SessionLocal
from app.schemas.token import TokenData
from app.schemas.user import UserBase
from app.core.security import get_decoded_by_token
from app.crud.crud_user import get_user_by_email
from app.core.exceptions import USER_NOT_FOUND
from app.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f'{settings.API_V1_STR}/login')


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    token_data: TokenData = get_decoded_by_token(token)
    current_user = get_user_by_email(db=db, email=token_data.email)
    if not current_user:
        raise USER_NOT_FOUND

    return UserBase(**dict(current_user.__dict__))
