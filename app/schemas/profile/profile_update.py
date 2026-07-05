from typing import Optional
from app.schemas.profile.Profile import ProfileHighlight, ProfileLinks
from pydantic import BaseModel, ConfigDict, EmailStr, Field

class ProfileUpdate(BaseModel):
    """For PUT/PATCH /profile (admin use)."""
    name: Optional[str] = None
    role: Optional[str] = None
    tagline: Optional[str] = None
    location: Optional[str] = None
    status: Optional[str] = None
    email: Optional[EmailStr] = None
    links: Optional[ProfileLinks] = None
    bio: Optional[list[str]] = None
    highlights: Optional[list[ProfileHighlight]] = None