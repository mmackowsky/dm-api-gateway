import uvicorn
from fastapi import Request, Response, status

from src.decorator import route
from src.main import app, settings


@route(
    request_method=app.post,
    path="/api/payment/",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.PAYMENTS_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder="auth.decode_access_token",
    service_authorization_checker="auth.is_default_user",  # CHANGE FROM is_admin_user to is_default_user
    service_header_generator="auth.generate_request_header",
)
async def process_payment(request: Request, response: Response):
    pass


@route(
    request_method=app.get,
    path="/api/payment/",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.PAYMENTS_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder="auth.decode_access_token",
    service_authorization_checker="auth.is_admin_user",  # CHANGE FROM is_admin_user to is_default_user
    service_header_generator="auth.generate_request_header",
)
async def get_payments(request: Request, response: Response):
    pass


@route(
    request_method=app.get,
    path="/api/payment/{id}",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.PAYMENTS_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder="auth.decode_access_token",
    service_authorization_checker="auth.is_admin_user",  # CHANGE FROM is_admin_user to is_default_user
    service_header_generator="auth.generate_request_header",
)
async def get_payments(id: int, request: Request, response: Response):
    pass
