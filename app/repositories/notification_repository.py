from sqlalchemy import func, select, update

from app.models.notification import Notification
from app.repositories.base import BaseRepository


class NotificationRepository(
    BaseRepository[Notification]
):
    def __init__(self, session):
        super().__init__(Notification, session)

    async def get_all_notifications(
        self,
        profile_id: str,
    ):
        result = await self.session.execute(
            select(Notification)
            .where(
                Notification.profile_id == profile_id
            )
            .order_by(
                Notification.created_at.desc()
            )
        )

        return result.scalars().all()

    async def get_unread_notifications(
        self,
        profile_id: str,
    ):
        result = await self.session.execute(
            select(Notification)
            .where(
                Notification.profile_id == profile_id,
                Notification.is_read.is_(False),
            )
            .order_by(
                Notification.created_at.desc()
            )
        )

        return result.scalars().all()

    async def get_unread_count(
        self,
        profile_id: str,
    ) -> int:
        result = await self.session.execute(
            select(func.count(Notification.id))
            .where(
                Notification.profile_id == profile_id,
                Notification.is_read.is_(False),
            )
        )

        return result.scalar() or 0

    async def mark_read(
        self,
        notification: Notification,
    ):
        notification.is_read = True

        await self.session.commit()
        await self.session.refresh(notification)

        return notification

    async def mark_unread(
        self,
        notification: Notification,
    ):
        notification.is_read = False

        await self.session.commit()
        await self.session.refresh(notification)

        return notification

    async def mark_all_read(
        self,
        profile_id: str,
    ):
        await self.session.execute(
            update(Notification)
            .where(
                Notification.profile_id == profile_id,
                Notification.is_read.is_(False),
            )
            .values(is_read=True)
        )

        await self.session.commit()

    async def delete_notification(
        self,
        notification: Notification,
    ):
        await self.session.delete(notification)
        await self.session.commit()