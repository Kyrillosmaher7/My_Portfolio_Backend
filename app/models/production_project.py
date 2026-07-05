
from datetime import datetime
from typing import Optional

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
from app.models.base import Base, _uuid
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
)

class ProductionProject(Base):
    """
    Represents a single production project for the portfolio.
    """

    __tablename__ = "production_projects"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=_uuid)

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    organization: Mapped[str] = mapped_column(String(255), nullable=False)
    period: Mapped[str] = mapped_column(String(100), nullable=False)
    summary: Mapped[str] = mapped_column(Text, nullable=False)
    role: Mapped[str] = mapped_column(String(150), nullable=False)

    # JS: impact: [string, ...]
    impact: Mapped[list] = mapped_column(JSON, nullable=False, default=list)

    # JS: stack: [string, ...]
    stack: Mapped[list] = mapped_column(JSON, nullable=False, default=list)

    # JS: links: { caseStudy, demo } — either may be null
    links: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)

    image: Mapped[Optional[str]] = mapped_column(String(500), nullable=True, default=None)
    confidential: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    sort_order: Mapped[int] = mapped_column(Integer, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )