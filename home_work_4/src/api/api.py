from fastapi import APIRouter
from src.api.v1.resources import users
api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["users"])
