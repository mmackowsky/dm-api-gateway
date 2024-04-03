from fastapi import FastAPI, Request, Response, status

from config import get_settings
from decorator import route
from structures.users import UserForm, UsernamePasswordForm, UserUpdateForm

app = FastAPI()
settings = get_settings()


@route(
    request_method=app.post,
    path="/api/login",
    status_code=status.HTTP_201_CREATED,
    payload_key="username_password",
    service_url=settings.USERS_SERVICE_URL,
    authentication_required=False,
    post_processing_func="post_processing.access_token_generate_handler",
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
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder="auth.decode_access_token",
    service_authorization_checker="auth.is_admin_user",
    service_header_generator="auth.generate_request_header",
    response_model="datastructures.users.UserResponse",
)
async def create_user(user: UserForm, request: Request, response: Response):
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
    service_authorization_checker="auth.is_admin_user",
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
    service_authorization_checker="auth.is_admin_user",
    service_header_generator="auth.generate_request_header",
    response_model="datastructures.users.UserResponse",
)
async def update_user(
    user_id: int, user: UserUpdateForm, request: Request, response: Response
):
    pass
