from typing import Optional

from pydantic import BaseModel


class UsernamePasswordForm(BaseModel):
    username: str
    password: str


class UserForm(UsernamePasswordForm):
    """
    id, hashed_password = None  -> fields is set in users-service
    """

    id: int = None
    email: str = None
    full_name: str = None
    user_type: str = "default"
    hashed_password: str = None


class UserUpdateForm(BaseModel):
    username: str = None
    email: str = None
    full_name: str = None
    user_type: str = None


class LoginResponse(BaseModel):
    access_token: str
    token_type: str


class UserResponse(BaseModel):
    id: int = None
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    user_type: str
    hashed_password: str = None

    # class Config:
    #     orm_mode = True
