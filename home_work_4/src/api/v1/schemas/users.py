from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, UUID4


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str
    email: EmailStr
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False


class UserUpdate(UserBase):
    email: EmailStr
    password: Optional[str] = None
    is_active: Optional[bool] = None


class UserDelete(UserBase):
    password: str


class AboutUser(UserBase):
    uuid: UUID4
    password: str
    email: EmailStr
    created_at: datetime
    is_active: Optional[bool] = True


class UserLogin(BaseModel):
    username: str
    password: str
