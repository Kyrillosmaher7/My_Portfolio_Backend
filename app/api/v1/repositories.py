from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.core.logging import get_logger
from app.deps import get_repositories_repo
from app.repositories.repositories_repository import RepositoriesRepository

from app.schemas.Repositories.repo import (
    RepositoryOut,
    RepositoryCreate,
    RepositoryUpdate,
)
from app.schemas.response import ResponseDTO


router = APIRouter(
    prefix="/repositories",
    tags=["Repositories"]
)

logger = get_logger()


@router.get("/", response_model=ResponseDTO[list[RepositoryOut]])
async def get_repositories(
    repositories_repo: RepositoriesRepository = Depends(get_repositories_repo)
):
    repos = await repositories_repo.get_all()

    return ResponseDTO(
        status=True,
        message="Repositories retrieved successfully",
        code=200,
        data=repos
    )


@router.get("/{repo_id}", response_model=ResponseDTO[RepositoryOut])
async def get_repository(
    repo_id: str,
    repositories_repo: RepositoriesRepository = Depends(get_repositories_repo)
):
    repo = await repositories_repo.get(repo_id)

    if not repo:
        raise HTTPException(
            status_code=404,
            detail="Repository not found"
        )

    return ResponseDTO(
        status=True,
        message="Repository retrieved successfully",
        code=200,
        data=repo
    )


@router.post("/", response_model=ResponseDTO[RepositoryOut], status_code=201)
async def create_repository(
    repo_data: RepositoryCreate,
    repositories_repo: RepositoriesRepository = Depends(get_repositories_repo)
):
    repo_data = repo_data.model_dump()
    repo = await repositories_repo.create(repo_data)

    return ResponseDTO(
        status=True,
        message="Repository created successfully",
        code=201,
        data=repo
    )


@router.patch("/{repo_id}", response_model=ResponseDTO[RepositoryOut])
async def update_repository(
    repo_id: str,
    repo_data: RepositoryUpdate,
    repositories_repo: RepositoriesRepository = Depends(get_repositories_repo)
):
    existing_repo = await repositories_repo.get(repo_id)

    if not existing_repo:
        raise HTTPException(
            status_code=404,
            detail="Repository not found"
        )

    updated_repo = await repositories_repo.update(
        existing_repo,
        repo_data
    )

    return ResponseDTO(
        status=True,
        message="Repository updated successfully",
        code=200,
        data=updated_repo
    )


@router.delete("/{repo_id}", response_model=ResponseDTO[None])
async def delete_repository(
    repo_id: str,
    repositories_repo: RepositoriesRepository = Depends(get_repositories_repo)
):
    repo = await repositories_repo.get(repo_id)

    if not repo:
        raise HTTPException(
            status_code=404,
            detail="Repository not found"
        )

    await repositories_repo.delete(repo)

    return ResponseDTO(
        status=True,
        message="Repository deleted successfully",
        code=200,
        data=None
    )