import uvicorn
from fastapi import FastAPI

from config import get_settings
from services import devices

app = FastAPI()
settings = get_settings()


if __name__ == "__main__":
    uvicorn.run(app, host=settings.SERVICE_HOST, port=settings.SERVICE_PORT)
