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
from app.models.Enums.PublicationStatus import PublicationStatus
from app.models.Enums.PublicationType import PublicationType
from app.models.base import Base, _uuid
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
)

class Publication(Base):
    """
     Represents a single publication for the portfolio.
    """
    __tablename__ = "publications"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=_uuid)

    type: Mapped[PublicationType] = mapped_column(SAEnum(PublicationType), nullable=False)
    status: Mapped[PublicationStatus] = mapped_column(SAEnum(PublicationStatus), nullable=False)
    title: Mapped[str] = mapped_column(Text, nullable=False)
    venue: Mapped[str] = mapped_column(String(255), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)

    # JS: authors: [string, ...]
    authors: Mapped[list] = mapped_column(JSON, nullable=False, default=list)

    abstract: Mapped[str] = mapped_column(Text, nullable=False)

    # JS: tags: [string, ...]
    tags: Mapped[list] = mapped_column(JSON, nullable=False, default=list)

    # JS: links: { pdf, doi, code } — any of which may be null
    links: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)

    # JS: image: string | null
    image: Mapped[Optional[str]] = mapped_column(String(500), nullable=True, default=None)

    sort_order: Mapped[int] = mapped_column(Integer, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

