import firebase_admin

from firebase_admin import credentials
from firebase_admin import messaging

from app.core.logging import get_logger
logger = get_logger()

class FirebasePushService:

    def __init__(self):

        if not firebase_admin._apps:
            cred = credentials.Certificate(
                "firebase-service-account.json"
            )

            firebase_admin.initialize_app(cred)

    async def send_to_token(
        self,
        token: str,
        title: str,
        body: str,
        data: dict | None = None,
    ):
        logger.info(f"FirebasePushService: send_to_token called with token: {token}, title: {title}, body: {body}")
        message = messaging.Message(
            token=token,
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            data=data or {},
        )

        return messaging.send(message)

    async def send_to_many(
        self,
        tokens: list[str],
        title: str,
        body: str,
        data: dict | None = None,
    ):
        if not tokens:
            return

        message = messaging.MulticastMessage(
            tokens=tokens,
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            data=data or {},
        )

        return messaging.send_each_for_multicast(
            message
        )