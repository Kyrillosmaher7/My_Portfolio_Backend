from datetime import datetime
from typing import Optional
from app.models.Enums.ChatRole import ChatRole
from app.schemas.profile.Profile import ProfileHighlight, ProfileLinks
from pydantic import BaseModel, ConfigDict, EmailStr, Field

class ChatMessageIn(BaseModel):
    """One entry of the `history` array sent by ChatbotWidget.jsx."""
    role: ChatRole
    content: str


class ChatRequest(BaseModel):
    """Request body for POST /chat — matches sendChatMessage(message, history)."""
    message: str
    history: list[ChatMessageIn] = []
    session_id: Optional[str] = None


class ChatReplyOut(BaseModel):
    """Response for POST /chat — matches the `{ reply }` shape the
    frontend already expects from services/chatbotService.js."""
    reply: str
    session_id: Optional[str] = None


class ChatMessageOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    role: ChatRole
    content: str
    created_at: datetime


class ChatSessionOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    visitor_id: Optional[str] = None
    created_at: datetime
    messages: list[ChatMessageOut] = []
