import uvicorn
from fastapi import FastAPI, Request, Response, status

from config import get_settings
from datastructures.users import (
    LoginResponse,
    UserForm,
    UsernamePasswordForm,
    UserUpdateForm,
)
from decorator import route

app = FastAPI()
settings = get_settings()

"""
Users Service
"""


@route(
    request_method=app.post,
    path="/api/login",
    status_code=status.HTTP_201_CREATED,
    payload_key="username_password",
    service_url=settings.USERS_SERVICE_URL,
    authentication_required=False,
    post_processing_func="processing.access_token_generate_handler",
    response_model="datastructures.users.LoginResponse",
)
async def login(
    username_password: UsernamePasswordForm, request: Request, response: Response
):
    pass


@route(
    request_method=app.post,
    path="/api/users",
    status_code=status.HTTP_201_CREATED,
    payload_key="user",
    service_url=settings.USERS_SERVICE_URL,
    authentication_required=False,
    post_processing_func=None,
    # authentication_token_decoder="auth.decode_access_token",
    # service_authorization_checker="auth.is_admin_user",
    # service_header_generator="auth.generate_request_header",
    response_model="datastructures.users.UserResponse",
)
async def register(user: UserForm, request: Request, response: Response):
    pass


@route(
    request_method=app.get,
    path="/api/users",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.USERS_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder="auth.decode_access_token",
    service_authorization_checker="auth.is_admin_user",
    service_header_generator="auth.generate_request_header",
    response_model="datastructures.users.UserResponse",
    response_list=True,
)
async def get_users(request: Request, response: Response):
    pass


@route(
    request_method=app.get,
    path="/api/users/{user_id}",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.USERS_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder="auth.decode_access_token",
    service_authorization_checker="auth.is_admin_user",
    service_header_generator="auth.generate_request_header",
    response_model="datastructures.users.UserResponse",
)
async def get_user(user_id: int, request: Request, response: Response):
    pass


@route(
    request_method=app.delete,
    path="/api/users/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    payload_key=None,
    service_url=settings.USERS_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder="auth.decode_access_token",
    service_authorization_checker="auth.is_default_user",  # CHANGE FROM is_admin_user to is_default_user
    service_header_generator="auth.generate_request_header",
)
async def delete_user(user_id: int, request: Request, response: Response):
    pass


@route(
    request_method=app.put,
    path="/api/users/{user_id}",
    status_code=status.HTTP_200_OK,
    payload_key="user",
    service_url=settings.USERS_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder="auth.decode_access_token",
    service_authorization_checker="auth.is_admin_user",  # CHANGE FROM is_admin_user to is_default_user
    service_header_generator="auth.generate_request_header",
    response_model="datastructures.users.UserResponse",
)
async def update_user(
    user_id: int, user: UserUpdateForm, request: Request, response: Response
):
    pass


"""
Energy Consumption Service
"""


@route(
    request_method=app.get,
    path="/api/energy",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.ENERGY_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder="auth.decode_access_token",
    service_authorization_checker="auth.is_default_user",  # CHANGE FROM is_admin_user to is_default_user
    service_header_generator="auth.generate_request_header",
)
async def get_energy_consumptions(request: Request, response: Response):
    pass


@route(
    request_method=app.get,
    path="/api/energy/{measurement_id}",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.ENERGY_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder="auth.decode_access_token",
    service_authorization_checker="auth.is_default_user",  # CHANGE FROM is_admin_user to is_default_user
    service_header_generator="auth.generate_request_header",
)
async def get_energy_consumption_by_id(
    measurement_id: int, request: Request, response: Response
):
    pass


@route(
    request_method=app.delete,
    path="/api/energy/{measurement_id}",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.ENERGY_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder="auth.decode_access_token",
    service_authorization_checker="auth.is_default_user",  # CHANGE FROM is_admin_user to is_default_user
    service_header_generator="auth.generate_request_header",
)
async def delete_energy_measurement(
    measurement_id: int, request: Request, response: Response
):
    pass


@route(
    request_method=app.post,
    path="/api/fake-measurement",
    status_code=status.HTTP_201_CREATED,
    payload_key=None,
    service_url=settings.ENERGY_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder="auth.decode_access_token",
    service_authorization_checker="auth.is_default_user",  # CHANGE FROM is_admin_user to is_default_user
    service_header_generator="auth.generate_request_header",
)
async def fake_measurement(request: Request, response: Response):
    pass


@route(
    request_method=app.post,
    path="/api/energy/collect-data",
    status_code=status.HTTP_201_CREATED,
    payload_key=None,
    service_url=settings.ENERGY_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder="auth.decode_access_token",
    service_authorization_checker="auth.is_default_user",  # CHANGE FROM is_admin_user to is_default_user
    service_header_generator="auth.generate_request_header",
)
async def collect_data(request: Request, response: Response):
    pass


"""
Water Consumption Service
"""


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


"""
Payments Service
"""


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


if __name__ == "__main__":
    uvicorn.run(app, host=settings.SERVICE_HOST, port=settings.SERVICE_PORT)
