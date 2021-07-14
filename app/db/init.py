from .session import engine
from .base import Base


def create_new_db():
    Base.metadata.create_all(bind=engine)
