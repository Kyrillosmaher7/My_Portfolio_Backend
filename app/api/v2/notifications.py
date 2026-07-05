

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from app.deps import (
    get_notification_repo,
)
from app.repositories.notification_repository import (
    NotificationRepository,
)
from app.schemas.notification.notification_out import (
    NotificationOut,
)
from app.schemas.response import (
    ResponseDTO,
)


router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"],
)

@router.get(
    "/",
    response_model=ResponseDTO[
        list[NotificationOut]
    ],
)
async def get_notifications(
    profile_id: str,
    repo: NotificationRepository = Depends(
        get_notification_repo
    ),
):
    notifications = (
        await repo.get_all_notifications(
            profile_id
        )
    )

    return ResponseDTO(
        status=True,
        code=200,
        message="Notifications retrieved successfully",
        data=notifications,
    )
@router.get(
    "/unread",
    response_model=ResponseDTO[
        list[NotificationOut]
    ],
)
async def get_unread_notifications(
    profile_id: str,
    repo: NotificationRepository = Depends(
        get_notification_repo
    ),
):
    notifications = (
        await repo.get_unread_notifications(
            profile_id
        )
    )

    return ResponseDTO(
        status=True,
        code=200,
        message="Unread notifications retrieved successfully",
        data=notifications,
    )
@router.get(
    "/unread/count",
    response_model=ResponseDTO[int],
)
async def get_unread_count(
    profile_id: str,
    repo: NotificationRepository = Depends(
        get_notification_repo
    ),
):
    count = await repo.get_unread_count(
        profile_id
    )

    return ResponseDTO(
        status=True,
        code=200,
        message="Unread count retrieved successfully",
        data=count,
    )
@router.patch(
    "/{id}/read",
    response_model=ResponseDTO[bool],
)
async def mark_notification_read(
    id: str,
    repo: NotificationRepository = Depends(
        get_notification_repo
    ),
):
    notification = await repo.get(id)

    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found",
        )

    await repo.mark_read(notification)

    return ResponseDTO(
        status=True,
        code=200,
        message="Notification marked as read",
        data=True,
    )
@router.patch(
    "/{id}/unread",
    response_model=ResponseDTO[bool],
)
async def mark_notification_unread(
    id: str,
    repo: NotificationRepository = Depends(
        get_notification_repo
    ),
):
    notification = await repo.get(id)

    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found",
        )

    await repo.mark_unread(notification)

    return ResponseDTO(
        status=True,
        code=200,
        message="Notification marked as unread",
        data=True,
    )
@router.patch(
    "/read-all",
    response_model=ResponseDTO[bool],
)
async def mark_all_read(
    profile_id: str,
    repo: NotificationRepository = Depends(
        get_notification_repo
    ),
):
    await repo.mark_all_read(
        profile_id
    )

    return ResponseDTO(
        status=True,
        code=200,
        message="All notifications marked as read",
        data=True,
    )
@router.delete(
    "/{id}",
    response_model=ResponseDTO[bool],
)
async def delete_notification(
    id: str,
    repo: NotificationRepository = Depends(
        get_notification_repo
    ),
):
    notification = await repo.get(id)

    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found",
        )

    await repo.delete_notification(
        notification
    )

    return ResponseDTO(
        status=True,
        code=200,
        message="Notification deleted successfully",
        data=True,
    )