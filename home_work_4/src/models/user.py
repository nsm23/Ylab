import uuid
from datetime import datetime

from sqlalchemy import UniqueConstraint
from sqlmodel import SQLModel, Field

__all__ = ("User",)


def create_uuid() -> uuid.UUID:
    num = uuid.uuid4()
    while num.hex[0] == '0':
        num = str(uuid.uuid4())
    return num


class User(SQLModel, table=True):
    __table_args__ = (UniqueConstraint("username"),
                      UniqueConstraint("email")
                      )
    uuid: str = Field(default_factory=create_uuid, primary_key=True, nullable=False)
    username: str = Field(nullable=False, max_length=12)
    email: str = Field(nullable=False)
    password: str = Field(nullable=False)
    is_active: bool = Field(default=True, nullable=False)
    is_superuser: bool = Field(default=False, nullable=False)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)

