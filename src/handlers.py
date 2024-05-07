from importlib import import_module

import aiohttp
from fastapi import HTTPException, Request, Response, status

from .exceptions import AuthTokenCorrupted, AuthTokenExpired, AuthTokenMissing
from .network import make_request


def import_function(method_path):
    module, method = method_path.rsplit(".", 1)
    mod = import_module(module)
    return getattr(mod, method, lambda *args, **kwargs: None)


async def auth_handler(
    request: Request,
    response: Response,
    service_url: str,
    status_code: int,
    payload: dict = None,
    authentication_required: bool = False,
    post_processing_func: str = None,
    authentication_token_decoder: str = "auth.decode_access_token",
    service_authorization_checker: str = "auth.is_admin_user",
    service_header_generator: str = "auth.generate_request_header",
    **kwargs,
):
    service_headers = {}

    if authentication_required:
        # authentication
        authorization = request.headers.get("authorization")
        token_decoder = import_function(authentication_token_decoder)
        exc = None
        try:
            token_payload = token_decoder(authorization)
        except (AuthTokenMissing, AuthTokenExpired, AuthTokenCorrupted) as e:
            exc = str(e)
        except Exception as e:
            # in case a new decoder is used by dependency injection and
            # there might be an unexpected error
            exc = str(e)
        finally:
            if exc:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail=exc,
                    headers={"WWW-Authenticate": "Bearer"},
                )

        # authorization
        if service_authorization_checker:
            authorization_checker = import_function(service_authorization_checker)
            is_user_eligible = authorization_checker(token_payload)
            if not is_user_eligible:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="You are not allowed to access this scope.",
                    headers={"WWW-Authenticate": "Bearer"},
                )

        # service headers
        if service_header_generator:
            header_generator = import_function(service_header_generator)
            service_headers = header_generator(token_payload)

    scope = request.scope

    method = scope["method"].lower()
    path = scope["path"]

    url = f"{service_url}{path}"

    try:
        resp_data, status_code_from_service = await make_request(
            url=url,
            method=method,
            data=payload,
            headers=service_headers,
        )
    except aiohttp.client_exceptions.ClientConnectorError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Service is unavailable.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except aiohttp.client_exceptions.ContentTypeError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Service error.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    response.status_code = status_code_from_service

    if all([status_code_from_service == status_code, post_processing_func]):
        post_processing_f = import_function(post_processing_func)
        resp_data = post_processing_f(resp_data)

    return resp_data
