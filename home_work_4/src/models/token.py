from typing import Optional
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True


class TokenPayLoad(BaseModel):
    sub: Optional[str] = None

    class Config:
        orm_mode = True

