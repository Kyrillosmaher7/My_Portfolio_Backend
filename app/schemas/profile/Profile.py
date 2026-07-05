
from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class ProfileLinks(BaseModel):
    github: Optional[str] = None
    linkedin: Optional[str] = None
    scholar: Optional[str] = None
    orcid: Optional[str] = None
    huggingface: Optional[str] = None
    cv: Optional[str] = None


class ProfileHighlight(BaseModel):
    label: str
    value: str


class ProfileOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    role: str
    tagline: str
    location: str
    status: str
    email: EmailStr
    links: ProfileLinks
    bio: list[str]
    highlights: list[ProfileHighlight]



