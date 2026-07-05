from datetime import datetime
from typing import Optional
from app.models.Enums.ChatRole import ChatRole
from app.schemas.profile.Profile import ProfileHighlight, ProfileLinks
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class ContactMessageCreate(BaseModel):
    """Request body for POST /contact — matches ContactPage.jsx form state."""
    name: str = Field(..., max_length=200)
    email: EmailStr
    subject: str = Field(..., max_length=300)
    message: str

class ContactMessageReplyCreate(BaseModel):
    message_id : str 
    name: str = Field(..., max_length=200)
    email: EmailStr
    subject: str = Field(..., max_length=300)
    message: str


class ContactMessageReplyOut(BaseModel):
    id : str
    message_id : str 
    name: str = Field(..., max_length=200)
    email: EmailStr
    subject:str
    message: str
    model_config = ConfigDict(from_attributes=True)
class ContactMessageOut(BaseModel):
    id: str
    name: str
    email: EmailStr
    subject: str
    message: str
    is_read: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ContactMessageAdminOut(BaseModel):
    """Full record shape for an admin inbox view (not used by the public site)."""
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    email: EmailStr
    subject: str
    message: str
    is_read: bool
    created_at: datetime