from typing import Optional, Union

from sqlalchemy.orm import Session

from src.api.v1.schemas.users import UserCreate, UserUpdate
from src.core.security import get_password_hash, verify_password
from src.models.user import User


def get_user(db: Session, username: str) -> Optional[User]:
    return db.query(User).filter(User.username == username).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def post(db: Session, payload: UserCreate):
    db_user = User(username=payload.username,
                   email=payload.email,
                   password=get_password_hash(payload.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def get(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def authenticate_user(db: Session,
                      username: str,
                      password: str) -> Union[User, bool]:
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def put(db: Session, user_id: int, payload: UserUpdate):
    db.query(User).filter(User.id == user_id).update({"username": payload.username,
                                                      "email": payload.email,
                                                      "password": get_password_hash(payload.password)})
    db.commit()
    return get(db, user_id)


def delete(db: Session, user_id: int):
    db_data = get(db, user_id)
    db.delete(db_data)
    db.commit()
    return db_data

