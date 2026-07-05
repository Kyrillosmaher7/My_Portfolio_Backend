from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import (
    JSON,
    Boolean,
    DateTime,
    Enum as SAEnum,
    ForeignKey,
    Integer,
    String,
    Text,
    func,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.models.Enums.SkillCategory import SkillCategory
from app.models.base import Base, _uuid

if TYPE_CHECKING:
    from app.models.profile import Profile


class Notification(Base):
    __tablename__ = "notifications"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=_uuid,
    )

    title: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    content: Mapped[Optional[str]] = mapped_column(
        String(500),
        nullable=True,
    )

    is_read: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    profile_id: Mapped[str] = mapped_column(
        ForeignKey("profiles.id"),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    profile: Mapped["Profile"] = relationship(
        back_populates="notifications"
    )

