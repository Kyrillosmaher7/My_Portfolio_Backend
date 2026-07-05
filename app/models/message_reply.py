from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, _uuid
if TYPE_CHECKING:   
    from app.models.contact_message import ContactMessage


class ContactMessageReply(Base):
    __tablename__ = "contact_message_replies"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=_uuid)

    message_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("contact_messages.id", ondelete="CASCADE"),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(String(200), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    subject: Mapped[str] = mapped_column(String(300), nullable=False)
    message: Mapped[str] = mapped_column(Text, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    contact_message: Mapped["ContactMessage"] = relationship(
        "ContactMessage",   # IMPORTANT: string
        back_populates="replies",
    )