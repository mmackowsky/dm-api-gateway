import uvicorn
from fastapi import Header, Request, Response, status

from src.decorator import route
from src.main import app, settings


@route(
    request_method=app.post,
    path="/stripe/cancel",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.PAYMENTS_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder="auth.decode_access_token",
    service_authorization_checker="auth.is_default_user",  # CHANGE FROM is_admin_user to is_default_user
    service_header_generator="auth.generate_request_header",
)
async def cancel(request: Request, response: Response):
    pass


@route(
    request_method=app.get,
    path="/stripe/success",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.PAYMENTS_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder="auth.decode_access_token",
    service_authorization_checker="auth.is_admin_user",  # CHANGE FROM is_admin_user to is_default_user
    service_header_generator="auth.generate_request_header",
)
async def success(request: Request, response: Response):
    pass


@route(
    request_method=app.get,
    path="/stripe/create-payment-session",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.PAYMENTS_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder="auth.decode_access_token",
    service_authorization_checker="auth.is_admin_user",  # CHANGE FROM is_admin_user to is_default_user
    service_header_generator="auth.generate_request_header",
)
async def create_payment_session(id: int, request: Request, response: Response):
    pass


@route(
    request_method=app.post,
    path="/stripe/webhook",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.PAYMENTS_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder="auth.decode_access_token",
    service_authorization_checker="auth.is_admin_user",  # CHANGE FROM is_admin_user to is_default_user
    service_header_generator="auth.generate_request_header",
)
async def webhook(
    request: Request, response: Response, stripe_signature: str = Header(None)
):
    pass


@route(
    request_method=app.get,
    path="/stripe/checkout",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.PAYMENTS_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder="auth.decode_access_token",
    service_authorization_checker="auth.is_admin_user",  # CHANGE FROM is_admin_user to is_default_user
    service_header_generator="auth.generate_request_header",
)
async def checkout(request: Request, response: Response):
    pass
