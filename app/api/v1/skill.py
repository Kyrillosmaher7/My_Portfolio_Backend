
from app.models.base import _uuid
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from app.core.logging import get_logger
from app.deps import get_skill_repo
from app.schemas.Skill.SkillOut import SkillCreate, SkillGroupsOut, SkillOut
from app.schemas.response import ResponseDTO
from app.repositories.skill_repository import SkillRepository
from app.models.Enums.SkillCategory import SkillCategory
router = APIRouter(
 prefix="/skills",
 tags=["Skills"]
)

logger = get_logger()


from app.models.Enums.SkillCategory import SkillCategory


@router.get("/skills-category", response_model=ResponseDTO[list[str]])
async def get_skills_categories():
    return ResponseDTO(
        status=True,
        message="Skill categories retrieved successfully",
        code=200,
        data=[category.value for category in SkillCategory]
    )


@router.get("/", response_model=ResponseDTO[SkillGroupsOut])
async def get_skills(skill_repo: SkillRepository = Depends(get_skill_repo)):

    skills = await skill_repo.get_all()

    # build groups from ENUM, not Pydantic fields
    groups = {cat.value: [] for cat in SkillCategory}

    for s in skills:
        groups[s.category.value].append(s.name)

    return ResponseDTO(
        status=True,
        message="Skills retrieved successfully",
        code=200,
        data=SkillGroupsOut(**groups)
    )


@router.get("/{skill_id}", response_model=ResponseDTO[SkillOut])
async def get_skill(skill_id: str, skill_repo: SkillRepository = Depends(get_skill_repo)):
    skill = await skill_repo.get(skill_id)
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    return ResponseDTO(
        status=True,
        message="Skill retrieved successfully",
        code=200,
        data=skill
    )

@router.post("/add", response_model=ResponseDTO[SkillOut])
async def add_skill(skill: SkillCreate, skill_repo: SkillRepository = Depends(get_skill_repo)):
        existing_skill = await skill_repo.get_by_name(skill.name)
        if existing_skill:
            raise HTTPException(status_code=400, detail="Skill already exists")
        #convert skill to dict and remove id field if present
        skill_dict = skill.dict()
        skill_dict.pop("id", None)
        new_skill = await skill_repo.create(skill_dict)
        return ResponseDTO(
            status=True,
            message="Skill added successfully",
            code=201,
            data=new_skill
        )


@router.put("/{skill_id}", response_model=ResponseDTO[SkillOut])
async def update_skill(skill_id: str, skill: SkillCreate, skill_repo: SkillRepository = Depends(get_skill_repo)):
    existing_skill = await skill_repo.get(skill_id)
    if not existing_skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    #convert skill to dict and remove id field if present
    skill_dict = skill.dict()
    skill_dict.pop("id", None)
    skill = SkillCreate(**skill_dict)
    updated_skill = await skill_repo.update(existing_skill, skill)
    return ResponseDTO(
        status=True,       
        message="Skill updated successfully",
        code=200,
        data=updated_skill
    )


@router.delete("/{skill_id}", response_model=ResponseDTO[bool])
async def delete_skill(skill_id: str, skill_repo: SkillRepository = Depends(get_skill_repo)):
    skill = await skill_repo.get(skill_id)
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    await skill_repo.delete(skill)
    return ResponseDTO(
        status=True,
        message="Skill deleted successfully",
        code=200,
        data=True
    )