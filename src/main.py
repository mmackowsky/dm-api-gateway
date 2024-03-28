import requests
import uvicorn
from fastapi import FastAPI, Request, Response, status

from config import get_settings

app = FastAPI()
settings = get_settings()


@app.post("/api/public")
async def login(data: dict):
    response = requests.post(url="http://127.0.0.1:8002", data=data)
    if response.status_code == 200:
        print("Data send successfully")
    return data


if __name__ == "__main__":
    uvicorn.run(app, host=settings.service_host, port=settings.service_port)
