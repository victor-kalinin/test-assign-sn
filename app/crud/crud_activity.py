from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Session
from sqlalchemy import func, and_

from app.models.post import Post
from app.models.like import Like
from app.models.user import User


def user_last_activity(db: Session, db_user: User):

    def datetime_min(dt: DateTime):
        return dt.created_at if dt is not None else datetime.min

    user_db_dict = dict(db_user.__dict__)
    user_last_like = db.query(Like).filter(Like.user_id == db_user.id)\
                                   .order_by(Like.created_at.desc()).first()
    user_last_post = db.query(Post).filter(Post.user_id == db_user.id)\
                                   .order_by(Post.created_at.desc()).first()
    last_data_activity = max(datetime_min(user_last_like),
                             datetime_min(user_last_post))
    user_db_dict.update({'been_active_at': last_data_activity})

    return user_db_dict


def read_all_likes(db: Session, date_from: datetime, date_to: datetime):
    return db.query(func.date(Like.created_at).label('date_group'),
                    func.count(func.date(Like.created_at)).label('count')).where(
                    and_(Like.is_like,
                         Like.created_at >= func.date(date_from),
                         Like.created_at <= func.date(date_to))) \
                    .group_by(func.date(Like.created_at)).all()
