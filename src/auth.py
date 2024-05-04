from datetime import datetime, timedelta

import jwt

from .config import get_settings
from .exceptions import AuthTokenCorrupted, AuthTokenExpired, AuthTokenMissing

settings = get_settings()


def generate_access_token(
    data: dict,
    expires_delta: timedelta = timedelta(
        minutes=settings.ACCESS_TOKEN_DEFAULT_EXPIRE_MINUTES
    ),
):
    expire = datetime.utcnow() + expires_delta
    token_data = {
        "id": data["id"],
        "user_type": data["user_type"],
        "exp": expire,
    }

    encoded_jwt = jwt.encode(
        token_data, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def decode_access_token(authorization: str = None):
    if not authorization:
        raise AuthTokenMissing("Auth token is missing in headers.")
    token = authorization.replace("Bearer : ", "")
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
        return payload
    except jwt.exceptions.ExpiredSignatureError:
        raise AuthTokenExpired("Auth token is expired.")
    except jwt.exceptions.DecodeError:
        raise AuthTokenCorrupted("Auth token is corrupted.")


def generate_request_header(token_payload):
    return {"request-user-id": str(token_payload["id"])}


def is_admin_user(token_payload):
    return token_payload["user_type"] == "admin"


def is_default_user(token_payload):
    return token_payload["user_type"] in ["default", "admin"]
