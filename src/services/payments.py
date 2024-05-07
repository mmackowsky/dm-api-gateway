from fastapi import APIRouter, Header, Request, Response, status

from src.config import get_settings
from src.handlers import auth_handler

router = APIRouter(prefix="/api", tags=["Payments"])
settings = get_settings()


@router.get("/stripe/cancel", status_code=status.HTTP_200_OK)
async def cancel(request: Request, response: Response):
    return await auth_handler(
        request=request,
        response=response,
        status_code=status.HTTP_200_OK,
        authentication_required=True,
        service_url=settings.PAYMENTS_SERVICE_URL,
    )


@router.get("/stripe/success", status_code=status.HTTP_200_OK)
async def success(request: Request, response: Response):
    return await auth_handler(
        request=request,
        response=response,
        status_code=status.HTTP_200_OK,
        authentication_required=True,
        service_url=settings.PAYMENTS_SERVICE_URL,
    )


@router.get("/stripe/create-payment-session", status_code=status.HTTP_200_OK)
async def create_payment_session(request: Request, response: Response):
    return await auth_handler(
        request=request,
        response=response,
        status_code=status.HTTP_200_OK,
        authentication_required=True,
        service_url=settings.PAYMENTS_SERVICE_URL,
    )


@router.post("/stripe/webhook", status_code=status.HTTP_201_CREATED)
async def webhook(
    request: Request, response: Response, stripe_signature: str = Header(None)
):
    return await auth_handler(
        request=request,
        response=response,
        status_code=status.HTTP_201_CREATED,
        authentication_required=True,
        service_url=settings.PAYMENTS_SERVICE_URL,
    )


@router.get("/stripe/checkout", status_code=status.HTTP_200_OK)
async def create_payment_session(request: Request, response: Response):
    return await auth_handler(
        request=request,
        response=response,
        status_code=status.HTTP_200_OK,
        authentication_required=True,
        service_url=settings.PAYMENTS_SERVICE_URL,
    )
