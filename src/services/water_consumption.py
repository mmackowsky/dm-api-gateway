from fastapi import APIRouter, Request, Response, status

from src.config import get_settings
from src.handlers import auth_handler

router = APIRouter(prefix="/api", tags=["Water Consumption"])
settings = get_settings()


@router.get("/water", status_code=status.HTTP_200_OK)
async def get_water_consumptions(request: Request, response: Response):
    return await auth_handler(
        request=request,
        response=response,
        service_url=settings.WATER_SERVICE_URL,
        authentication_required=True,
        status_code=status.HTTP_200_OK,
    )


@router.get("/water/{measurement_id}", status_code=status.HTTP_200_OK)
async def get_water_consumption_by_id(
    measurement_id: int, request: Request, response: Response
):
    return await auth_handler(
        request=request,
        response=response,
        service_url=settings.WATER_SERVICE_URL,
        authentication_required=True,
        status_code=status.HTTP_200_OK,
    )


@router.delete("/water/{measurement_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_water_measurement(request: Request, response: Response):
    return await auth_handler(
        request=request,
        response=response,
        service_url=settings.WATER_SERVICE_URL,
        authentication_required=True,
        status_code=status.HTTP_204_NO_CONTENT,
    )


@router.post("/energy/collect-data", status_code=status.HTTP_201_CREATED)
async def collect_water_data(request: Request, response: Response):
    return await auth_handler(
        request=request,
        response=response,
        service_url=settings.WATER_SERVICE_URL,
        authentication_required=True,
        status_code=status.HTTP_201_CREATED,
    )
