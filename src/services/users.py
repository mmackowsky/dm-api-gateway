from fastapi import APIRouter, FastAPI, Request, Response, status

from src.config import get_settings
from src.datastructures.users import UserForm, UsernamePasswordForm, UserUpdateForm
from src.handlers import auth_handler

settings = get_settings()
router = APIRouter(tags=["Users"])


@router.post("/api/login", status_code=status.HTTP_201_CREATED)
async def login(
    username_password: UsernamePasswordForm, request: Request, response: Response
):
    return await auth_handler(
        request=request,
        response=response,
        service_url=settings.USERS_SERVICE_URL,
        status_code=status.HTTP_201_CREATED,
        payload=username_password.dict(),
        post_processing_func="processing.access_token_generate_handler",
    )


@router.post("/api/users", status_code=status.HTTP_201_CREATED)
async def register(user: UserForm, request: Request, response: Response):
    return await auth_handler(
        request=request,
        response=response,
        payload=user.dict(),
        status_code=status.HTTP_201_CREATED,
        service_url=settings.USERS_SERVICE_URL,
    )


@router.get("/api/users", status_code=status.HTTP_200_OK)
async def get_users(request: Request, response: Response):
    return await auth_handler(
        request=request,
        response=response,
        service_url=settings.USERS_SERVICE_URL,
        status_code=status.HTTP_200_OK,
        authentication_required=True,
        service_authorization_checker="default",
    )


@router.get("/api/users/{user_id}", status_code=status.HTTP_200_OK)
async def get_user(user_id: int, request: Request, response: Response):
    return await auth_handler(
        request=request,
        response=response,
        service_url=settings.USERS_SERVICE_URL,
        status_code=status.HTTP_200_OK,
        authentication_required=True,
        service_authorization_checker="default",
    )


@router.delete("/api/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, request: Request, response: Response):
    return await auth_handler(
        request=request,
        response=response,
        service_url=settings.USERS_SERVICE_URL,
        status_code=status.HTTP_204_NO_CONTENT,
        authentication_required=True,
        service_authorization_checker="default",
    )


@router.put("/api/users/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(
    user_id: int, user: UserUpdateForm, request: Request, response: Response
):
    return await auth_handler(
        request=request,
        response=response,
        payload=user.dict(),
        status_code=status.HTTP_200_OK,
        service_url=settings.USERS_SERVICE_URL,
        authentication_required=True,
    )
