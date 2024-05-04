import uvicorn
from fastapi import Request, Response, status

from src.decorator import route
from src.main import app, settings


@route(
    request_method=app.get,
    path="/api/energy",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.WATER_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder="auth.decode_access_token",
    service_authorization_checker="auth.is_default_user",  # CHANGE FROM is_admin_user to is_default_user
    service_header_generator="auth.generate_request_header",
)
async def get_water_consumptions(request: Request, response: Response):
    pass


@route(
    request_method=app.get,
    path="/api/energy/{measurement_id}",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.WATER_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder="auth.decode_access_token",
    service_authorization_checker="auth.is_default_user",  # CHANGE FROM is_admin_user to is_default_user
    service_header_generator="auth.generate_request_header",
)
async def get_water_consumption_by_id(
    measurement_id: int, request: Request, response: Response
):
    pass


@route(
    request_method=app.delete,
    path="/api/energy/{measurement_id}",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.WATER_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder="auth.decode_access_token",
    service_authorization_checker="auth.is_default_user",  # CHANGE FROM is_admin_user to is_default_user
    service_header_generator="auth.generate_request_header",
)
async def delete_water_measurement(
    measurement_id: int, request: Request, response: Response
):
    pass
