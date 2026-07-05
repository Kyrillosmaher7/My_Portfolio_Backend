from fastapi import APIRouter
from fastapi import WebSocket

from app.services.websocket_service import (
    manager
)

router = APIRouter()


@router.websocket(
    "/ws/notifications"
)
async def notification_socket(
    websocket: WebSocket
):

    await manager.connect(
        websocket
    )

    try:

        while True:
            await websocket.receive_text()

    except Exception:

        manager.disconnect(
            websocket
        )