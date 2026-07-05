from pydantic import BaseModel
from typing import Optional

from app.models.Enums.PublicationStatus import PublicationStatus
from app.models.Enums.PublicationType import PublicationType
from app.schemas.Publication.publication_out import PublicationLinks

class PublicationCreate(BaseModel):
    type: PublicationType
    status: PublicationStatus
    title: str
    venue: str
    year: int
    authors: list[str] = []
    abstract: str
    tags: list[str] = []
    links: PublicationLinks = PublicationLinks()
    image: Optional[str] = None
    sort_order: int = 0