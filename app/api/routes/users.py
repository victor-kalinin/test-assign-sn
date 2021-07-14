from typing import List
from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends

from app.api.depends import get_db, get_current_user
from app.schemas.user import UserBase, UserCreate, UserActivity
from app.schemas.post import Post, PostCreate
from app.schemas.like import LikeBase
from app.crud.crud_user import get_users, get_user_by_email, create_user, get_user
from app.crud.crud_post import create_post
from app.crud.crud_like import like_post, is_user_liked_post
from app.crud.crud_activity import user_last_activity
from app.core.exceptions import EMAIL_EXIST, USER_NOT_FOUND, ALREADY_LIKED


router = APIRouter()


@router.get('/', response_model=List[UserBase])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.post('/signup', response_model=UserBase)
def new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise EMAIL_EXIST
    return create_user(db=db, user=user)


@router.get('/me', response_model=UserBase)
async def read_users_me(current_user: UserBase = Depends(get_current_user)):
    return current_user


@router.post('/me/post', response_model=Post)
def create_item_for_user(post: PostCreate, db: Session = Depends(get_db),
                         current_user: UserBase = Depends(get_current_user)):
    return create_post(db=db, post=post, user_id=current_user.id)


@router.post('/me/like/{post_id}', response_model=LikeBase)
def like_post_by_user(post_id: int, is_like: bool = None, db: Session = Depends(get_db),
                      current_user: UserBase = Depends(get_current_user)):
    db_post_like = is_user_liked_post(db, user_id=current_user.id, post_id=post_id)
    if db_post_like:
        raise ALREADY_LIKED

    return like_post(db=db, post_id=post_id, user_id=current_user.id, is_like=is_like)


@router.get('/{user_id}/', response_model=UserBase)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise USER_NOT_FOUND
    return db_user


@router.get('/{user_id}/activity', response_model=UserActivity)
def user_activity(user_id: int, db: Session = Depends(get_db)):
    db_user = read_user(user_id=user_id, db=db)
    return user_last_activity(db=db, db_user=db_user)
