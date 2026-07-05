from fastapi import APIRouter, Depends, HTTPException

from app.core.logging import get_logger
from app.deps import (
    get_contact_message_repo,
    get_email_service,
    get_notification_service,
)
from app.repositories.contact_message_repository import (
    ContactMessageRepository,
)
from app.schemas.ContactForm.form import (
    ContactMessageAdminOut,
    ContactMessageCreate,
    ContactMessageOut,
    ContactMessageReplyCreate,
    ContactMessageReplyOut,
)
from app.schemas.response import ResponseDTO
from app.services.email_service import EmailService
from app.services.notification_service import NotificationService

router = APIRouter(
    prefix="/messages",
    tags=["Contact Messages"],
)

logger = get_logger()

@router.post(
    "/send",
    response_model=ResponseDTO[ContactMessageOut],
    status_code=201,
)
async def send_message(
    message: ContactMessageCreate,
    notification_service: NotificationService = Depends(get_notification_service),
    messages_repo: ContactMessageRepository = Depends(get_contact_message_repo),
):
    msg = await messages_repo.create(message.model_dump())

    await notification_service.notify_admin(
        title="New Contact Message",
        content=f"{msg.name} sent a message"
    )

    return ResponseDTO(
        status=True,
        code=201,
        message="Message sent successfully",
        data=ContactMessageOut.model_validate(msg),
    )

@router.get( "/",response_model=ResponseDTO[list[ContactMessageAdminOut]],)
async def get_messages(
    messages_repo: ContactMessageRepository = Depends(
        get_contact_message_repo
    ),
):
    messages = await messages_repo.get_all()

    return ResponseDTO(
        status=True,
        code=200,
        message="Messages retrieved successfully",
        data=messages,
    )


@router.get("/unread",    response_model=ResponseDTO[list[ContactMessageAdminOut]],)
async def get_unread_messages(
    messages_repo: ContactMessageRepository = Depends(
        get_contact_message_repo
    ),
):
    messages = await messages_repo.get_unread_messages()

    return ResponseDTO(
        status=True,
        code=200,
        message="Unread messages retrieved successfully",
        data=messages,
    )


@router.get("/{message_id}",response_model=ResponseDTO[ContactMessageAdminOut],)
async def get_message(
    message_id: str,
    messages_repo: ContactMessageRepository = Depends(
        get_contact_message_repo
    ),
):
    message = await messages_repo.get(message_id)

    if not message:
        raise HTTPException(
            status_code=404,
            detail="Message not found",
        )

    return ResponseDTO(
        status=True,
        code=200,
        message="Message retrieved successfully",
        data=message,
    )


@router.patch("/{message_id}/read",response_model=ResponseDTO[bool],)
async def mark_message_as_read(
    message_id: str,
    messages_repo: ContactMessageRepository = Depends(
        get_contact_message_repo
    ),
):
    message = await messages_repo.get(message_id)

    if not message:
        raise HTTPException(
            status_code=404,
            detail="Message not found",
        )

    await messages_repo.mark_as_read(message)

    return ResponseDTO(
        status=True,
        code=200,
        message="Message marked as read",
        data=True,
    )


# @router.patch("/{message_id}/unread",response_model=ResponseDTO[bool],)
# async def mark_message_as_unread(
#     message_id: str,
#     messages_repo: ContactMessageRepository = Depends(
#         get_contact_message_repo
#     ),
# ):
#     message = await messages_repo.get(message_id)

#     if not message:
#         raise HTTPException(
#             status_code=404,
#             detail="Message not found",
#         )

#     await messages_repo.mark_as_unread(message)

#     return ResponseDTO(
#         status=True,
#         code=200,
#         message="Message marked as unread",
#         data=True,
#     )


@router.delete("/{message_id}",response_model=ResponseDTO[bool],)
async def delete_message(
    message_id: str,
    messages_repo: ContactMessageRepository = Depends(
        get_contact_message_repo
    ),
):
    message = await messages_repo.get(message_id)

    if not message:
        raise HTTPException(
            status_code=404,
            detail="Message not found",
        )

    await messages_repo.delete_message(message)

    return ResponseDTO(
        status=True,
        code=200,
        message="Message deleted successfully",
        data=True,
    )


@router.get("/{message_id}/replies",response_model=ResponseDTO[list[ContactMessageReplyOut]],)
async def get_message_replies(
    message_id: str,
    messages_repo: ContactMessageRepository = Depends(
        get_contact_message_repo
    ),
):
    message = await messages_repo.get(message_id)

    if not message:
        raise HTTPException(
            status_code=404,
            detail="Message not found",
        )

    replies = await messages_repo.get_replies(
        message_id
    )

    return ResponseDTO(
        status=True,
        code=200,
        message="Replies retrieved successfully",
        data=replies,
    )


@router.post("/{message_id}/replies",response_model=ResponseDTO[ContactMessageReplyOut],status_code=201,)
async def send_reply(
    message_id: str,
    reply_data: ContactMessageReplyCreate,
    messages_repo: ContactMessageRepository = Depends(
        get_contact_message_repo
    ),
    email_service: EmailService = Depends(
        get_email_service
    ),
):
    original_message = await messages_repo.get(
        message_id
    )

    if not original_message:
        raise HTTPException(
            status_code=404,
            detail="Message not found",
        )

    payload = reply_data.model_dump()

    payload["message_id"] = message_id

    reply = await messages_repo.create_reply(
        payload
    )

    await email_service.send_email(
        recipients=[
            original_message.email
        ],
        subject=reply.subject,
        body=reply.message,
    )

    return ResponseDTO(
        status=True,
        code=201,
        message="Reply sent successfully",
        data=reply,
    )


@router.get("/replies/{reply_id}",response_model=ResponseDTO[ContactMessageReplyOut],)
async def get_reply(
    reply_id: str,
    messages_repo: ContactMessageRepository = Depends(
        get_contact_message_repo
    ),
):
    reply = await messages_repo.get_reply(
        reply_id
    )

    if not reply:
        raise HTTPException(
            status_code=404,
            detail="Reply not found",
        )

    return ResponseDTO(
        status=True,
        code=200,
        message="Reply retrieved successfully",
        data=reply,
    )


@router.delete("/replies/{reply_id}",response_model=ResponseDTO[bool],)
async def delete_reply(
    reply_id: str,
    messages_repo: ContactMessageRepository = Depends(
        get_contact_message_repo
    ),
):
    reply = await messages_repo.get_reply(
        reply_id
    )

    if not reply:
        raise HTTPException(
            status_code=404,
            detail="Reply not found",
        )

    await messages_repo.delete_reply(reply)

    return ResponseDTO(
        status=True,
        code=200,
        message="Reply deleted successfully",
        data=True,
    )