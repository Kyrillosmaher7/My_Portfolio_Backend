from datetime import datetime, timezone

from sqlalchemy import delete
from sqlalchemy import select
from sqlalchemy import update

from app.models.tokens import RefreshToken
from app.repositories.base import BaseRepository


class RefreshTokenRepository(
    BaseRepository[RefreshToken]
):

    def __init__(self, session):
        super().__init__(
            RefreshToken,
            session,
        )

    async def get_by_token(
        self,
        token: str,
    ) -> RefreshToken | None:
        result = await self.session.execute(
            select(RefreshToken)
            .where(
                RefreshToken.token == token
            )
        )

        return result.scalar_one_or_none()

    async def get_active_token(
        self,
        token: str,
    ) -> RefreshToken | None:
        result = await self.session.execute(
            select(RefreshToken)
            .where(
                RefreshToken.token == token,
                RefreshToken.revoked.is_(False),
                RefreshToken.expires_at >
                datetime.now(timezone.utc),
            )
        )

        return result.scalar_one_or_none()

    async def get_admin_tokens(
        self,
        admin_id: str,
    ) -> list[RefreshToken]:
        result = await self.session.execute(
            select(RefreshToken)
            .where(
                RefreshToken.admin_id == admin_id
            )
            .order_by(
                RefreshToken.created_at.desc()
            )
        )

        return result.scalars().all()

    async def get_active_admin_tokens(
        self,
        admin_id: str,
    ) -> list[RefreshToken]:
        result = await self.session.execute(
            select(RefreshToken)
            .where(
                RefreshToken.admin_id == admin_id,
                RefreshToken.revoked.is_(False),
                RefreshToken.expires_at >
                datetime.now(timezone.utc),
            )
            .order_by(
                RefreshToken.created_at.desc()
            )
        )

        return result.scalars().all()

    async def revoke(
        self,
        token: RefreshToken,
    ) -> RefreshToken:
        token.revoked = True

        await self.session.commit()
        await self.session.refresh(token)

        return token

    async def revoke_by_token(
        self,
        token: str,
    ) -> bool:
        refresh_token = await self.get_by_token(
            token
        )

        if not refresh_token:
            return False

        refresh_token.revoked = True

        await self.session.commit()

        return True

    async def revoke_all(
        self,
        admin_id: str,
    ) -> int:
        result = await self.session.execute(
            update(RefreshToken)
            .where(
                RefreshToken.admin_id == admin_id,
                RefreshToken.revoked.is_(False),
            )
            .values(
                revoked=True
            )
        )

        await self.session.commit()

        return result.rowcount or 0

    async def delete_expired_tokens(
        self,
    ) -> int:
        result = await self.session.execute(
            delete(RefreshToken)
            .where(
                RefreshToken.expires_at <
                datetime.now(timezone.utc)
            )
        )

        await self.session.commit()

        return result.rowcount or 0

    async def delete_admin_tokens(
        self,
        admin_id: str,
    ) -> int:
        result = await self.session.execute(
            delete(RefreshToken)
            .where(
                RefreshToken.admin_id == admin_id
            )
        )

        await self.session.commit()

        return result.rowcount or 0