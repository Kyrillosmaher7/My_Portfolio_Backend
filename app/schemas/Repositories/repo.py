from datetime import datetime
from typing import Optional
from app.models.Enums.ChatRole import ChatRole
from app.schemas.profile.Profile import ProfileHighlight, ProfileLinks
from pydantic import BaseModel, ConfigDict, EmailStr, Field

class RepositoryOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    description: str
    language: str
    stars: int
    forks: int
    topics: list[str]
    url: str
    homepage: Optional[str] = None
    archived: bool
    image: Optional[str] = None


class RepositoryCreate(BaseModel):
    name: str
    description: str
    language: str
    stars: int = 0
    forks: int = 0
    topics: list[str] = []
    url: str
    homepage: Optional[str] = None
    archived: bool = False
    image: Optional[str] = None
    sort_order: int = 0


class RepositoryUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    language: Optional[str] = None
    stars: Optional[int] = None
    forks: Optional[int] = None
    topics: Optional[list[str]] = None
    url: Optional[str] = None
    homepage: Optional[str] = None
    archived: Optional[bool] = None
    image: Optional[str] = None