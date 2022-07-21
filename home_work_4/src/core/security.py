from datetime import timedelta

import redis
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel

from src.core.config import JWT_SECRET_KEY, REDIS_HOST, REDIS_PORT


class RedisSettings(BaseModel):
    jwt_secret_key = JWT_SECRET_KEY
    jwt_enabled: bool = True
    jwt_token_checks: set = {"access", "refresh"}
    access_expires: int = timedelta(minutes=15)
    refresh_expires: int = timedelta(days=30)
    host = REDIS_HOST
    port = REDIS_PORT


settings = RedisSettings()


@AuthJWT.load_config
def get_config():
    return RedisSettings()


@AuthJWT.token_in_denylist_loader
def check_token(decrypted_token):
    jti = decrypted_token["jti"]
    entry = blocked_access_tokens.get(jti)
    return entry and entry == "true"


blocked_access_tokens = redis.Redis(host=settings.host,
                                    port=settings.port,
                                    db=1,
                                    decode_responses=True,
                                    )

active_refresh_tokens = redis.Redis(host=settings.host,
                                    port=settings.port,
                                    db=2,
                                    decode_responses=True,
                                    )
