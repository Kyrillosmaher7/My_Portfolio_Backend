from datetime import datetime
from typing import Optional, TYPE_CHECKING

from sqlalchemy import (
    JSON,
    DateTime,
    String,
    Text,
    func,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.models.base import Base, _uuid

if TYPE_CHECKING:
    from app.models.skill import Skill
    from app.models.notification import Notification

class Profile(Base):
    __tablename__ = "profiles"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=_uuid,
    )

    name: Mapped[str] = mapped_column(String(200), nullable=False)
    role: Mapped[str] = mapped_column(String(200), nullable=False)
    tagline: Mapped[str] = mapped_column(Text, nullable=False)
    location: Mapped[str] = mapped_column(String(150), nullable=False)
    status: Mapped[str] = mapped_column(String(200), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)

    image: Mapped[Optional[str]] = mapped_column(
        String(500),
        nullable=True,
        default=None,
    )

    links: Mapped[dict] = mapped_column(
        JSON,
        nullable=False,
        default=dict,
    )

    bio: Mapped[list] = mapped_column(
        JSON,
        nullable=False,
        default=list,
    )

    highlights: Mapped[list] = mapped_column(
        JSON,
        nullable=False,
        default=list,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    skills: Mapped[list["Skill"]] = relationship(
        back_populates="profile",
        cascade="all, delete-orphan",
    )

    notifications: Mapped[list["Notification"]] = relationship(
        back_populates="profile",
        cascade="all, delete-orphan",
    )
