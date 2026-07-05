from typing import Optional

from pydantic import BaseModel


class ProductionLinks(BaseModel):
    caseStudy: Optional[str] = None
    demo: Optional[str] = None