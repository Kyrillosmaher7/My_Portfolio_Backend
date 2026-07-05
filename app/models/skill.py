from typing import TYPE_CHECKING

from sqlalchemy import (
    Enum as SAEnum,
    ForeignKey,
    Integer,
    String,
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


class Skill(Base):
    """
    Represents a skill or technology that a profile has experience with.
    Used to populate the SkillsSection on the frontend.
    """

    __tablename__ = "skills"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=_uuid,
    )

    profile_id: Mapped[str] = mapped_column(
        ForeignKey("profiles.id"),
        nullable=False,
    )

    category: Mapped[SkillCategory] = mapped_column(
        SAEnum(SkillCategory),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    sort_order: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    profile: Mapped["Profile"] = relationship(
        back_populates="skills"
    )