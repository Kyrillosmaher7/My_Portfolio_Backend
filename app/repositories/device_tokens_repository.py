


from select import select

from sqlalchemy import select

from app.models.device_token import DeviceToken
from app.repositories.base import BaseRepository


class DeviceTokenRepository(BaseRepository[DeviceToken]):
    def __init__(self, session):
        super().__init__(DeviceToken, session)
    async def get_admin_tokens(self, admin_id: str) -> list[str]:
        result = await self.session.execute(
            select(DeviceToken.token)
            .where(DeviceToken.admin_id == admin_id)
        )

        return result.scalars().all()
    async def get_all_tokens(self) -> list[str]:
        result = await self.session.execute(
            select(DeviceToken.token)
        )
        return result.scalars().all()