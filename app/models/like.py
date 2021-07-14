from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, Boolean, DateTime
from sqlalchemy.orm import relationship

from app.db.base import Base


class Like(Base):
    __tablename__ = 'likes'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'), primary_key=True)
    is_like = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    users = relationship('User', back_populates='likes')
    posts = relationship('Post', back_populates='likes')
