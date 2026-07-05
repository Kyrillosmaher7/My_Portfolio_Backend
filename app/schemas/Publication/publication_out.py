from typing import Optional

from pydantic import BaseModel, ConfigDict

from app.models.Enums.PublicationStatus import PublicationStatus
from app.models.Enums.PublicationType import PublicationType


class PublicationLinks(BaseModel):
    pdf: Optional[str] = None
    doi: Optional[str] = None
    code: Optional[str] = None


class PublicationOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    type: PublicationType
    status: PublicationStatus
    title: str
    venue: str
    year: int
    authors: list[str]
    abstract: str
    tags: list[str]
    links: PublicationLinks
    image: Optional[str] = None