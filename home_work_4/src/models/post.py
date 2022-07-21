from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel

__all__ = ("Post",)

from src.models.user import User


class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    title: str = Field(nullable=False)
    description: str = Field(nullable=False)
    views: int = Field(default=0)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)

