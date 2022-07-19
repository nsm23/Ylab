import os
from typing import List

from fastapi_jwt_auth import AuthJWT
from fastapi import APIRouter, Depends, HTTPException, Path
from pydantic import BaseModel
from sqlalchemy.orm import Session

from src.api.v1 import deps
from src.api.v1.deps import ALGORITHM
from src.api.v1.schemas.users import UserLogin, User, UserCreate, UserUpdate
from src.services.users import authenticate_user, get_user_by_email, post, get, get_all, put, delete

router = APIRouter()


class Settings(BaseModel):
    jwt_secret_key: str = os.getenv('JWT_SECRET_KEY')
    jwt_algorithm: list = os.getenv('JWT_ALGORITHM')


@AuthJWT.load_config
def get_config():
    return Settings()


@router.post('/login')
def login(payload: UserLogin,
          authorize: AuthJWT = Depends(),
          db: Session = Depends(deps.get_db)):
    user_data = authenticate_user(db, payload.username, payload.password)
    if not user_data:
        raise HTTPException(status_code=401, detail='Wrong username or password')
    access_token = authorize.create_access_token(subject=user_data.username, algorithm=ALGORITHM)
    refresh_token = authorize.create_refresh_token(subject=user_data.username, algorithm=ALGORITHM)
    return {'access_token': access_token, 'refresh_token': refresh_token}


@router.get('/me/', response_model=User)
def read_me(authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    current_user = authorize.get_jwt_subject()
    return {'user': current_user}


@router.post('/refresh')
def refresh(authorize: AuthJWT = Depends()):
    authorize.jwt_refresh_token_required()
    current_user = authorize.get_jwt_subject()
    new_access_token = authorize.create_access_token(subject=current_user, algorithm=ALGORITHM)
    return {'access_token': new_access_token}


@router.get('/protected')
def protect(authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    current_user = authorize.get_jwt_subject()
    return {'user': current_user}


@router.post('/create', response_model=User, status_code=201)
def create_user(payload: UserCreate, db: Session = Depends(deps.get_db)):
    db_user = get_user_by_email(db, email=payload.email)
    if db_user:
        raise HTTPException(status_code=400, detail='Email already exist')
    return post(db, payload)


@router.get('/{id}/', response_model=User)
def read_user(id: int = Path(..., gt=0),db: Session = Depends(deps.get_db)):
    user_data = get(db, id)
    if not user_data:
        raise HTTPException(status_code=404, detail='User not found')
    return user_data


@router.get('/', response_model=List[User])
def read_all_users(skip: int = 0, limit: int = 50, db: Session = Depends(deps.get_db)):
    return get_all(db, skip=skip, limit=limit)


@router.put("/{id}/", response_model=User)
def update_user(payload: UserUpdate, id: int = Path(..., gt=0), db: Session = Depends(deps.get_db)):
    user_data = get(db, id)
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    return put(db, id, payload)


@router.delete("/{id}/", response_model=User)
def delete_user(id: int = Path(..., gt=0), db: Session = Depends(deps.get_db)):
    user_data = get(db, id)
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    return delete(db, id)
