from databases import Database
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlmodel import Session, create_engine
from src.core.config import DATABASE_URL

__all__ = ("get_session", 'SessionLocal', 'database')


engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
metadata = MetaData()

database = Database(DATABASE_URL)


def get_session():
    with Session(engine) as session:
        yield session
