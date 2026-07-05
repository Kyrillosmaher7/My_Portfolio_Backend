from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.core.logging import get_logger
from app.deps import get_production_project_repo
from app.repositories.production_project_repository import ProductionProjectRepository

from app.schemas.response import ResponseDTO
from app.schemas.production_projects.production_project_create import ProductionProjectCreate
from app.schemas.production_projects.ProductionProjectUpdate import ProductionProjectUpdate
from app.schemas.production_projects.ProductionProjectOut import ProductionProjectOut


router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)

logger = get_logger()


@router.get("/", response_model=ResponseDTO[list[ProductionProjectOut]])
async def get_projects(
    projects_repo: ProductionProjectRepository = Depends(get_production_project_repo)
):
    projects = await projects_repo.get_all()

    return ResponseDTO(
        status=True,
        message="Projects retrieved successfully",
        code=200,
        data=projects
    )


@router.get("/{project_id}", response_model=ResponseDTO[ProductionProjectOut])
async def get_project(
    project_id: str,
    projects_repo: ProductionProjectRepository = Depends(get_production_project_repo)
):
    project = await projects_repo.get(project_id)

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return ResponseDTO(
        status=True,
        message="Project retrieved successfully",
        code=200,
        data=project
    )


@router.post("/", response_model=ResponseDTO[ProductionProjectOut], status_code=201)
async def create_project(
    project_data: ProductionProjectCreate,
    projects_repo: ProductionProjectRepository = Depends(get_production_project_repo)
):
    project_data = project_data.model_dump()
    project = await projects_repo.create(project_data)

    return ResponseDTO(
        status=True,
        message="Project created successfully",
        code=201,
        data=project
    )


@router.put("/{project_id}", response_model=ResponseDTO[ProductionProjectOut])
async def update_project(
    project_id: str,
    project_data: ProductionProjectUpdate,
    projects_repo: ProductionProjectRepository = Depends(get_production_project_repo)
):
    existing_project = await projects_repo.get(project_id)

    if not existing_project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    updated_project = await projects_repo.update(
        existing_project,
        project_data
    )

    return ResponseDTO(
        status=True,
        message="Project updated successfully",
        code=200,
        data=updated_project
    )


@router.delete("/{project_id}", response_model=ResponseDTO[None])
async def delete_project(
    project_id: str,
    projects_repo: ProductionProjectRepository = Depends(get_production_project_repo)
):
    project = await projects_repo.get(project_id)

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    await projects_repo.delete(project)

    return ResponseDTO(
        status=True,
        message="Project deleted successfully",
        code=200,
        data=None
    )