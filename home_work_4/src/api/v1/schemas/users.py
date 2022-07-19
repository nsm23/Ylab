from typing import Optional, List
from pydantic import BaseModel, EmailStr

from src.models.post import Post


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False


class UserUpdate(UserBase):
    password: Optional[str] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None


class UserDelete(UserBase):
    password: str


class User(UserBase):
    id: Optional[int] = None
    is_active: Optional[bool] = True
    posts: List[Post] = []

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    username: str
    password: str
