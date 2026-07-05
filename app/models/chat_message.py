from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    DateTime,
    Enum as SAEnum,
    ForeignKey,
    String,
    Text,
    func,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.models.Enums.ChatRole import ChatRole
from app.models.base import Base, _uuid

if TYPE_CHECKING:
    from app.models.chat_session import ChatSession


class ChatMessage(Base):
    """
    Represents a single message in a chat session.
    One turn in a ChatSession.
    """

    __tablename__ = "chat_messages"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=_uuid,
    )

    session_id: Mapped[str] = mapped_column(
        ForeignKey("chat_sessions.id"),
        nullable=False,
    )

    role: Mapped[ChatRole] = mapped_column(
        SAEnum(ChatRole),
        nullable=False,
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    session: Mapped["ChatSession"] = relationship(
        back_populates="messages"
    )