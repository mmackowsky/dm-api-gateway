import uvicorn
from fastapi import FastAPI, Request, Response, status

from src.datastructures.devices import DeviceForm
from src.decorator import route
from src.main import app, settings


@route(
    request_method=app.post,
    path="/api/devices/",
    status_code=status.HTTP_201_CREATED,
    payload_key=None,
    service_url=settings.DEVICES_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder="auth.decode_access_token",
    service_authorization_checker="auth.is_default_user",  # CHANGE FROM is_admin_user to is_default_user
    service_header_generator="auth.generate_request_header",
)
async def add_device(device_form: DeviceForm, request: Request, response: Response):
    pass


@route(
    request_method=app.get,
    path="/api/devices/",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.DEVICES_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder="auth.decode_access_token",
    service_authorization_checker="auth.is_default_user",  # CHANGE FROM is_admin_user to is_default_user
    service_header_generator="auth.generate_request_header",
)
async def get_devices(request: Request, response: Response):
    pass


@route(
    request_method=app.get,
    path="/api/devices/{id}",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.DEVICES_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder="auth.decode_access_token",
    service_authorization_checker="auth.is_default_user",  # CHANGE FROM is_admin_user to is_default_user
    service_header_generator="auth.generate_request_header",
)
async def get_device_by_id(request: Request, response: Response, id: int):
    pass


@route(
    request_method=app.delete,
    path="/api/devices/{id}",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.DEVICES_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder="auth.decode_access_token",
    service_authorization_checker="auth.is_default_user",  # CHANGE FROM is_admin_user to is_default_user
    service_header_generator="auth.generate_request_header",
)
async def delete_device(request: Request, response: Response, id: int):
    pass


if __name__ == "__main__":
    uvicorn.run(app, host=settings.SERVICE_HOST, port=settings.SERVICE_PORT)
