from sqlalchemy import select

from app.models.admin import Admin
from app.repositories.base import BaseRepository


class AdminRepository(BaseRepository[Admin]):

    def __init__(self, session):
        super().__init__(Admin, session)

    async def get_by_email(self,email: str,) -> Admin | None:
        result = await self.session.execute(
            select(Admin).where(
                Admin.email == email
            )
        )

        return result.scalar_one_or_none()
    async def get_admin(self) -> Admin | None:
        result = await self.session.execute(
            select(Admin).limit(1)
        )
        return result.scalar_one_or_none()
    
    async def email_exists(self,email: str,) -> bool:
        admin = await self.get_by_email(email)

        return admin is not None

    async def update_password( self,admin: Admin,password_hash: str,) -> Admin:
        admin.password_hash = password_hash

        await self.session.commit()
        await self.session.refresh(admin)

        return admin