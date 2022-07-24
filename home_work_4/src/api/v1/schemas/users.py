from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, UUID4

__all__ = ('UserBase', 'UserCreate',
           'UserUpdate', 'AboutUser',
           'UserLogin')


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str
    email: EmailStr


class UserUpdate(UserBase):
    email: EmailStr


class AboutUser(UserBase):
    uuid: UUID4
    password: str
    email: EmailStr
    created_at: datetime
    is_superuser: bool


class UserLogin(UserBase):
    password: str
