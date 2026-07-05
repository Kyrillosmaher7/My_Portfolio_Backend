from fastapi import APIRouter, Depends

from app.core.auth import get_current_admin
from app.deps import get_auth_service
from app.models import admin
from app.schemas.auth.change_password import ChangePasswordRequest
from app.schemas.auth.login import LoginRequest
from app.schemas.auth.token import RefreshRequest, TokenResponse
from app.schemas.response import ResponseDTO
from app.services.auth_service import AuthService


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post(
    "/login",
    response_model=ResponseDTO[
        TokenResponse
    ]
)
async def login(
    request: LoginRequest,
    auth_service: AuthService = Depends(
        get_auth_service
    )
):
    tokens = await auth_service.login(
        request.email,
        request.password,
    )

    return ResponseDTO(
        status=True,
        code=200,
        message="Login successful",
        data=tokens,
    )


@router.post(
    "/refresh",
    response_model=ResponseDTO[dict]
)
async def refresh(
    request: RefreshRequest,
    auth_service: AuthService = Depends(
        get_auth_service
    )
):
    token = await auth_service.refresh(
        request.refresh_token
    )

    return ResponseDTO(
        status=True,
        code=200,
        message="Token refreshed",
        data=token,
    )

@router.post(
    "/logout",
    response_model=ResponseDTO[bool]
)
async def logout(
    request: RefreshRequest,
    auth_service: AuthService = Depends(
        get_auth_service
    )
):
    await auth_service.logout(
        request.refresh_token
    )

    return ResponseDTO(
        status=True,
        code=200,
        message="Logged out",
        data=True,
    )

@router.post(
    "/change-password",
    response_model=ResponseDTO[bool]
)

async def change_password(
    request: ChangePasswordRequest,
    current_admin: admin = Depends(
        get_current_admin
    ),
    auth_service: AuthService = Depends(
        get_auth_service
    )
):
    await auth_service.change_password(
        current_admin.id,
        request.old_password,
        request.new_password,
    )

    return ResponseDTO(
        status=True,
        code=200,
        message="Password changed",
        data=True,
    )