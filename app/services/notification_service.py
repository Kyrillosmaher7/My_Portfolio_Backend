from app.core.logging import get_logger
from app.repositories.admin_repo import AdminRepository
from app.repositories.device_tokens_repository import DeviceTokenRepository
from app.repositories.notification_repository import NotificationRepository
from app.services.firebase_push_service import FirebasePushService
from app.services.websocket_service import manager

logger = get_logger()


class NotificationService:

    def __init__(
        self,
        notification_repo: NotificationRepository,
        device_token_repo: DeviceTokenRepository,
        push_service: FirebasePushService,
        admin_repo: AdminRepository,
    ):
        self.notification_repo = notification_repo
        self.device_token_repo = device_token_repo
        self.push_service = push_service
        self.admin_repo = admin_repo

    async def notify_admin(self, title: str, content: str):
        logger.info(
            f"NotificationService: notify_admin called with title={title}, content={content}"
        )

        #fetch admin
        admin = await self.admin_repo.get_admin() 

        if not admin:
            raise ValueError("Admin not found")

        admin_id = admin.id

        # create notification
        notification = await self.notification_repo.create({
            "title": title,
            "content": content,
            "profile_id": admin_id,
        })

        # get device tokens
        tokens = await self.device_token_repo.get_all_tokens()

        # send push notification
        if tokens:
            await self.push_service.send_to_many(
                tokens=tokens,
                title=title,
                body=content,
                data={
                    "notification_id": str(notification.id)
                },
            )

        # websocket broadcast
        await manager.broadcast({
            "type": "notification",
            "title": title,
            "content": content,
        })

        return notification