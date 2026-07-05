from datetime import datetime
from datetime import timedelta
from datetime import timezone

from jose import JWTError
from jose import jwt


class JWTService:

    def __init__(
        self,
        secret_key: str,
        algorithm: str,
        access_minutes: int,
        refresh_days: int,
    ):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.access_minutes = access_minutes
        self.refresh_days = refresh_days

    def create_access_token(
        self,
        admin_id: str,
    ) -> str:

        expire = (
            datetime.now(timezone.utc)
            + timedelta(
                minutes=self.access_minutes
            )
        )

        payload = {
            "sub": admin_id,
            "type": "access",
            "exp": expire,
        }

        return jwt.encode(
            payload,
            self.secret_key,
            algorithm=self.algorithm,
        )

    def create_refresh_token(
        self,
        admin_id: str,
    ) -> tuple[str, datetime]:

        expire = (
            datetime.now(timezone.utc)
            + timedelta(
                days=self.refresh_days
            )
        )

        payload = {
            "sub": admin_id,
            "type": "refresh",
            "exp": expire,
        }

        token = jwt.encode(
            payload,
            self.secret_key,
            algorithm=self.algorithm,
        )

        return token, expire

    def decode_token(
        self,
        token: str,
    ) -> dict:

        return jwt.decode(
            token,
            self.secret_key,
            algorithms=[
                self.algorithm
            ],
        )

    def validate_refresh_token(
        self,
        token: str,
    ) -> dict:

        payload = self.decode_token(
            token
        )

        if payload["type"] != "refresh":
            raise ValueError(
                "Invalid refresh token"
            )

        return payload

    def validate_access_token(
        self,
        token: str,
    ) -> dict:

        payload = self.decode_token(
            token
        )

        if payload["type"] != "access":
            raise ValueError(
                "Invalid access token"
            )

        return payload