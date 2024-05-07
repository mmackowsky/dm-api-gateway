from fastapi import APIRouter, Request, Response, status

from src.config import get_settings
from src.handlers import auth_handler

router = APIRouter(prefix="/api", tags=["Energy Consumption"])
settings = get_settings()


@router.get("/api/energy", status_code=status.HTTP_200_OK)
async def get_energy_consumptions(request: Request, response: Response):
    return await auth_handler(
        request=request,
        response=response,
        service_url=settings.ENERGY_SERVICE_URL,
        authentication_required=True,
        status_code=status.HTTP_200_OK,
    )


@router.get("/api/energy/{measurement_id}", status_code=status.HTTP_200_OK)
async def get_energy_consumption_by_id(
    measurement_id: int, request: Request, response: Response
):
    return await auth_handler(
        request=request,
        response=response,
        service_url=settings.ENERGY_SERVICE_URL,
        authentication_required=True,
        status_code=status.HTTP_200_OK,
    )


@router.delete("/api/energy/{measurement_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_energy_measurement(request: Request, response: Response):
    return await auth_handler(
        request=request,
        response=response,
        service_url=settings.ENERGY_SERVICE_URL,
        authentication_required=True,
        status_code=status.HTTP_204_NO_CONTENT,
    )


@router.post("/api/energy/collect-data", status_code=status.HTTP_201_CREATED)
async def collect_data(request: Request, response: Response):
    return await auth_handler(
        request=request,
        response=response,
        service_url=settings.ENERGY_SERVICE_URL,
        authentication_required=True,
        status_code=status.HTTP_201_CREATED,
    )
