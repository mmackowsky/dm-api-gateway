import uvicorn
from fastapi import FastAPI, Request, Response, status

from config import get_settings

app = FastAPI()
settings = get_settings()


@app.get("/api/users")
async def read_users():
    return {"users": []}


if __name__ == "__main__":
    uvicorn.run(app, host=settings.service_host, port=settings.service_port)
