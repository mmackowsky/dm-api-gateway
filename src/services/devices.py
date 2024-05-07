from fastapi import APIRouter, Request, Response, status

from src.config import get_settings
from src.datastructures.devices import DeviceForm
from src.handlers import auth_handler

settings = get_settings()
router = APIRouter(prefix="/api", tags=["Devices"])


@router.post("/devices", status_code=status.HTTP_201_CREATED)
async def add_device(device_form: DeviceForm, request: Request, response: Response):
    return await auth_handler(
        request=request,
        response=response,
        service_url=settings.DEVICES_SERVICE_URL,
        status_code=status.HTTP_201_CREATED,
        authentication_required=True,
        payload=device_form.dict(),
    )


@router.get("/devices", status_code=status.HTTP_200_OK)
async def get_devices(request: Request, response: Response):
    return await auth_handler(
        request=request,
        response=response,
        service_url=settings.DEVICES_SERVICE_URL,
        status_code=status.HTTP_200_OK,
        authentication_required=True,
    )


@router.get("/devices/{id}", status_code=status.HTTP_200_OK)
async def get_device_by_id(request: Request, response: Response, id: int):
    return await auth_handler(
        request=request,
        response=response,
        service_url=settings.DEVICES_SERVICE_URL,
        status_code=status.HTTP_200_OK,
        authentication_required=True,
    )


@router.delete("/devices/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_device(request: Request, response: Response, id: int):
    return await auth_handler(
        request=request,
        response=response,
        service_url=settings.DEVICES_SERVICE_URL,
        status_code=status.HTTP_204_NO_CONTENT,
        authentication_required=True,
    )
