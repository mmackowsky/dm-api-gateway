import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """
    API Gateway variables
    """

    ACCESS_TOKEN_DEFAULT_EXPIRE_MINUTES: int = os.getenv(
        "ACCESS_TOKEN_DEFAULT_EXPIRE_MINUTES"
    )
    ALGORITHM: str = os.getenv("ALGORITHM")
    GATEWAY_TIMEOUT: int = os.getenv("GATEWAY_TIMEOUT")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    SERVICE_PORT: int = os.getenv("SERVICE_PORT")
    SERVICE_HOST: str = os.getenv("SERVICE_HOST")
    """
    External services urls.
    """
    USERS_SERVICE_URL: str = os.getenv("USERS_SERVICE_URL")
    ENERGY_SERVICE_URL: str = os.getenv("ENERGY_SERVICE_URL")

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
