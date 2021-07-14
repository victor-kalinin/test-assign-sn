from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.db.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String(255), nullable=False)
    email = Column(String(64), unique=True)
    hashed_password = Column(String(128))
    created_at = Column(DateTime, default=datetime.utcnow)
    login_at = Column(DateTime)

    posts = relationship('Post', back_populates='author')
    likes = relationship('Like', back_populates='users')
