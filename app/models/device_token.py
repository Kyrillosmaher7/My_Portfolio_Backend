from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.admin import Admin
from app.models.base import Base, _uuid


class DeviceToken(Base):
    __tablename__ = "device_tokens"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=_uuid,
    )

    admin_id: Mapped[str] = mapped_column(
        ForeignKey("admins.id"),
        nullable=False,
    )

    token: Mapped[str] = mapped_column(
        String(500),
        unique=True,
        nullable=False,
    )

    platform: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    admin: Mapped["Admin"] = relationship(
        back_populates="device_tokens"
    )