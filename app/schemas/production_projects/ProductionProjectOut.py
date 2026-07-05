from datetime import datetime
from typing import Optional
from app.models.Enums.ChatRole import ChatRole
from app.schemas.profile.Profile import ProfileHighlight, ProfileLinks
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from app.schemas.production_projects.Production_links import ProductionLinks



class ProductionProjectOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    title: str
    organization: str
    period: str
    summary: str
    role: str
    impact: list[str]
    stack: list[str]
    links: ProductionLinks
    image: Optional[str] = None
    confidential: bool