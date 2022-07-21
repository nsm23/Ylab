from sqlmodel import Session, create_engine
from src.core.config import DATABASE_URL

__all__ = ("get_session",)


engine = create_engine(DATABASE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session
