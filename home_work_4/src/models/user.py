from datetime import datetime
from typing import Optional

from sqlalchemy import String, Column, Integer, UniqueConstraint
from sqlmodel import SQLModel, Field

__all__ = ("User",)


class User(SQLModel, table=True):
    __table_args__ = (UniqueConstraint("username"),
                      UniqueConstraint("email")
                      )
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    username: str = Field(nullable=False, max_length=12)
    email: str = Field(nullable=False)
    password: str = Field(nullable=False)
    is_active: bool = Field(default=True, nullable=False)
    is_superuser: bool = Field(default=False, nullable=False)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    

