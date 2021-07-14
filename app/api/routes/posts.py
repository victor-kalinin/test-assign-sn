from typing import List
from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends

from app.api.depends import get_db
from app.schemas.post import PostBase
from app.crud.crud_post import get_posts


router = APIRouter()


@router.get('/', response_model=List[PostBase])
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = get_posts(db, skip=skip, limit=limit)
    return posts
