import uvicorn
from fastapi import FastAPI, Request, Response, status

from config import get_settings
from datastructures.users import UsernamePasswordForm
from services import devices, energy_consumption, payments, users, water_consumption

app = FastAPI()
settings = get_settings()


app.include_router(users.router)
app.include_router(energy_consumption.router)
app.include_router(water_consumption.router)
app.include_router(devices.router)
app.include_router(payments.router)


if __name__ == "__main__":
    uvicorn.run(app, host=settings.SERVICE_HOST, port=settings.SERVICE_PORT)
