import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    service_port: int = os.getenv("SERVICE_PORT")
    service_host: str = os.getenv("SERVICE_HOST")
    users_service_url: str = os.getenv("USERS_SERVICE_URL")

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
