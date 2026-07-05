
from pydantic import BaseModel, ConfigDict, Field

from app.models.Enums.SkillCategory import SkillCategory


class SkillOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    category: SkillCategory
    name: str


class SkillCreate(BaseModel):
    profile_id : str 
    category: SkillCategory
    name: str = Field(..., max_length=150)
    sort_order: int = 0


class SkillGroupsOut(BaseModel):
    """
    Re-grouped shape matching `skills` export in profile.js exactly:
        { research: [...], ml_frameworks: [...], languages_tools: [...],
          data_infra: [...], soft: [...] }
    Build this in the route handler from a list[Skill] ORM rows, e.g.:

        groups = {cat.value: [] for cat in SkillCategory}
        for s in skills:
            groups[s.category.value].append(s.name)
        return SkillGroupsOut(**groups)
    """
    research: list[str] = []
    ml_frameworks: list[str] = []
    languages_tools: list[str] = []
    data_infra: list[str] = []
    soft: list[str] = []