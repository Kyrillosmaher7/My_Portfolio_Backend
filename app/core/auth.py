from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from grpc import Status

from app.deps import get_admin_repo, get_jwt_service
from app.models import admin
from app.repositories.admin_repo import AdminRepository
from app.services.jwt_service import JWTService


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

async def get_current_admin(
    token: str = Depends(
        oauth2_scheme
    ),
    admin_repo: AdminRepository = Depends(
        get_admin_repo
    ),
    jwt_service: JWTService = Depends(
        get_jwt_service
    ),
) -> admin:

    try:

        payload = (
            jwt_service
            .validate_access_token(
                token
            )
        )

        admin_id = payload["sub"]

    except Exception:

        raise HTTPException(
            status_code=Status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

    admin = await admin_repo.get(
        admin_id
    )

    if not admin:
        raise HTTPException(
            status_code=Status.HTTP_401_UNAUTHORIZED,
            detail="Admin not found",
        )

    return admin