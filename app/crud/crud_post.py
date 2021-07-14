from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app.schemas.post import PostCreate
from app.models.post import Post


def create_post(db: Session, post: PostCreate, user_id: int):
    post_data = jsonable_encoder(post)
    db_item = Post(**post_data, user_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Post).offset(skip).limit(limit).all()
