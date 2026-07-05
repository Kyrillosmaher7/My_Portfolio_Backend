from pydantic import BaseModel
from typing import Optional

from app.models.Enums.PublicationStatus import PublicationStatus
from app.models.Enums.PublicationType import PublicationType
from app.schemas.Publication.publication_out import PublicationLinks


class PublicationUpdate(BaseModel):
    type: Optional[PublicationType] = None
    status: Optional[PublicationStatus] = None
    title: Optional[str] = None
    venue: Optional[str] = None
    year: Optional[int] = None
    authors: Optional[list[str]] = None
    abstract: Optional[str] = None
    tags: Optional[list[str]] = None
    links: Optional[PublicationLinks] = None
    image: Optional[str] = None 