from datetime import datetime
from typing import Optional
from app.models.Enums.ChatRole import ChatRole
from app.schemas.production_projects.Production_links import ProductionLinks
from app.schemas.profile.Profile import ProfileHighlight, ProfileLinks
from pydantic import BaseModel, ConfigDict, EmailStr, Field

class ProductionProjectCreate(BaseModel):
    title: str
    organization: str
    period: str
    summary: str
    role: str
    impact: list[str] = []
    stack: list[str] = []
    links: ProductionLinks = ProductionLinks()
    image: Optional[str] = None
    confidential: bool = False
    sort_order: int = 0
