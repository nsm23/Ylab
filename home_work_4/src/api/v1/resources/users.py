from fastapi import APIRouter, Depends
from starlette import status

from src.api.v1.schemas.users import UserCreate, UserLogin, UserUpdate
from src.services.users import get_user_service, UserService
from fastapi_jwt_auth import AuthJWT

router = APIRouter()


@router.post(path="/create", summary="Create user",
             tags=["users"], status_code=status.HTTP_201_CREATED,)
def user_create(
        user: UserCreate,
        user_service: UserService = Depends(get_user_service),
) -> dict:
    context = user_service.create_user(user=user)
    return context


@router.post(path="/login", summary="Login", tags=["users"],)
def user_login(
        user: UserLogin,
        user_service: UserService = Depends(get_user_service),
        authorize: AuthJWT = Depends(),
):
    return user_service.login(authorize, user)


@router.get(
    path="/user_info", summary="User information", tags=["users"],)
def user_info(
        user_service: UserService = Depends(get_user_service),
        authorize: AuthJWT = Depends(),
):
    return user_service.user_detail(authorize)


@router.patch(
    path="/update", summary="Update profile", tags=["users"],)
def user_update(
        user: UserUpdate,
        user_service: UserService = Depends(get_user_service),
        authorize: AuthJWT = Depends(),
):
    return user_service.user_change(authorize, user=user)


@router.post(path="/logout", summary="Logout", tags=["users"],)
def user_logout(
        user_service: UserService = Depends(get_user_service),
        authorize: AuthJWT = Depends(),
):
    return user_service.logout(authorize)


@router.post(
    path="/logout_all", summary="Full logout", tags=["users"],)
def user_logout_all(
        user_service: UserService = Depends(get_user_service),
        authorize: AuthJWT = Depends(),
):
    return user_service.logout_all(authorize)


@router.post(
    path="/refresh_token", summary="Refresh token", tags=["users"],)
def refresh(
        user_service: UserService = Depends(get_user_service),
        authorize: AuthJWT = Depends(),
):
    return user_service.refresh(authorize)









