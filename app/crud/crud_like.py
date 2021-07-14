from sqlalchemy.orm import Session

from app.models.like import Like


def like_post(db: Session, post_id: int, user_id: int, is_like: bool):
    db_item = Like(post_id=post_id, user_id=user_id, is_like=is_like)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def is_user_liked_post(db: Session, post_id: int, user_id: int):
    return db.query(Like).filter(Like.post_id == post_id,
                                 Like.user_id == user_id).first()
