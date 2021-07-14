from fastapi import APIRouter

from app.api.routes import users, login, analytics, posts


api_router = APIRouter()
api_router.include_router(login.router, tags=['login'])
api_router.include_router(users.router, prefix='/users', tags=['users'])
api_router.include_router(posts.router, prefix='/posts', tags=['posts'])
api_router.include_router(analytics.router, tags=["analytics"])
