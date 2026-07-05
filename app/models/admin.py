from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    DateTime,
    String,
    func,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.models.base import Base, _uuid
from app.models.device_token import DeviceToken

if TYPE_CHECKING:
    from app.models.tokens import RefreshToken


class Admin(Base):

    __tablename__ = "admins"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=_uuid,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    refresh_tokens: Mapped[list["RefreshToken"]] = relationship(
        back_populates="admin",
        cascade="all, delete-orphan",
    )
    device_tokens: Mapped[list["DeviceToken"]] = relationship(
        back_populates="admin",
        cascade="all, delete-orphan",
    )