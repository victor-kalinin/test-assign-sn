from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.api.depends import get_db
from app.schemas.token import Token
from app.schemas.user import User
from app.core.security import verify_password, create_access_token
from app.crud.crud_user import get_user_by_email, update_user_login_date
from app.core.exceptions import INCORRECT_USERNAME_PASSWORD


router = APIRouter()


@router.post('/login', response_model=Token)
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, form_data.username)

    if not db_user:
        raise INCORRECT_USERNAME_PASSWORD

    user = User(**dict(db_user.__dict__))

    if not verify_password(form_data.password, user.hashed_password):
        raise INCORRECT_USERNAME_PASSWORD

    token: str = create_access_token(user.dict())
    db_user = update_user_login_date(db=db, db_user=db_user)
    return {"access_token": token, "token_type": "bearer"}
