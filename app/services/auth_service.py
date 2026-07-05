from fastapi import HTTPException
from fastapi import status

from app.models.tokens import (
    RefreshToken
)


class AuthService:

    def __init__(
        self,
        admin_repo,
        refresh_token_repo,
        password_service,
        jwt_service,
    ):
        self.admin_repo = admin_repo

        self.refresh_token_repo = (
            refresh_token_repo
        )

        self.password_service = (
            password_service
        )

        self.jwt_service = (
            jwt_service
        )
    async def login(
        self,
        email: str,
        password: str,
    ):

        admin = (
            await self.admin_repo
            .get_by_email(email)
        )

        if not admin:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )

        valid = (
            self.password_service
            .verify_password(
                password,
                admin.password_hash,
            )
        )

        if not valid:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )

        access_token = (
            self.jwt_service
            .create_access_token(
                admin.id
            )
        )

        refresh_token, expires_at = (
            self.jwt_service
            .create_refresh_token(
                admin.id
            )
        )

        await self.refresh_token_repo.create(
            {
                "admin_id": admin.id,
                "token": refresh_token,
                "expires_at": expires_at,
            }
        )

        return {
            "admin_id": admin.id,
            "access_token": access_token,
            "refresh_token": refresh_token,
        }
    async def refresh(
        self,
        refresh_token: str,
    ):

        payload = (
            self.jwt_service
            .validate_refresh_token(
                refresh_token
            )
        )

        stored_token = (
            await self.refresh_token_repo
            .get_active_token(
                refresh_token
            )
        )

        if not stored_token:
            raise HTTPException(
                status_code=401,
                detail="Refresh token revoked",
            )

        access_token = (
            self.jwt_service
            .create_access_token(
                payload["sub"]
            )
        )

        return {
            "access_token": access_token
        }
    async def logout(
        self,
        refresh_token: str,
    ):

        token = (
            await self.refresh_token_repo
            .get_by_token(
                refresh_token
            )
        )

        if token:
            await self.refresh_token_repo.revoke(
                token
            )

        return True
    async def logout_all(
        self,
        admin_id: str,
    ):
        await (
            self.refresh_token_repo
            .revoke_all(admin_id)
        )

        return True
    async def change_password(
        self,
        admin_id: str,
        old_password: str,
        new_password: str,
    ):

        admin = await self.admin_repo.get(
            admin_id
        )

        if not admin:
            raise HTTPException(
                status_code=404,
                detail="Admin not found",
            )

        valid = (
            self.password_service
            .verify_password(
                old_password,
                admin.password_hash,
            )
        )

        if not valid:
            raise HTTPException(
                status_code=400,
                detail="Wrong password",
            )

        admin.password_hash = (
            self.password_service
            .hash_password(
                new_password
            )
        )

        await self.admin_repo.session.commit()

        await (
            self.refresh_token_repo
            .revoke_all(admin_id)
        )

        return True