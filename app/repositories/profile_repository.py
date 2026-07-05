

from sqlalchemy import select

from app.models.profile import Profile
from app.repositories.base import BaseRepository

class ProfileRepository(BaseRepository[Profile]):
    def __init__(self, session):
        super().__init__(Profile, session)

    async def get_by_user_name(self, user_name: str) -> Profile:
        result = await self.session.execute(
            select(Profile).where(Profile.name == user_name)
        )
        return result.scalars().first()
    async def get(self) -> Profile:
        result = await self.session.execute(
            select(Profile).limit(1)
        )
        return result.scalars().first()
    async def update_image(self, profile: Profile,image_url: str,) -> Profile:
        profile.image = image_url

        await self.session.commit()
        await self.session.refresh(profile)

        return profile