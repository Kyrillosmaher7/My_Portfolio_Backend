
from pydantic import BaseModel
from typing import Optional

from app.schemas.production_projects.Production_links import ProductionLinks


class ProductionProjectUpdate(BaseModel):
    title: Optional[str] = None
    organization: Optional[str] = None
    period: Optional[str] = None
    summary: Optional[str] = None
    role: Optional[str] = None
    impact: Optional[list[str]] = None
    stack: Optional[list[str]] = None
    links: Optional[ProductionLinks] = None
    image: Optional[str] = None
    confidential: Optional[bool] = None