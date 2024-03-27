import requests
import uvicorn
from fastapi import FastAPI, Request, Response, status

from config import get_settings

app = FastAPI()
settings = get_settings()


@app.get("/api/users")
async def read_users():
    response = requests.get(url="http://127.0.0.1:8002")
    return response.status_code


if __name__ == "__main__":
    uvicorn.run(app, host=settings.service_host, port=settings.service_port)
