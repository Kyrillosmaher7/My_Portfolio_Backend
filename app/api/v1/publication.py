from fastapi import APIRouter, Depends, HTTPException

from app.core.logging import get_logger
from app.deps import get_publications_repo
from app.models.Enums.PublicationStatus import PublicationStatus
from app.models.Enums.PublicationType import PublicationType
from app.repositories.publications_repository import PublicationsRepository

from app.schemas.Publication.PublicationCreate import PublicationCreate
from app.schemas.Publication.PublicationUpdate import PublicationUpdate
from app.schemas.Publication.publication_out import PublicationOut
from app.schemas.response import ResponseDTO

router = APIRouter(
    prefix="/publications",
    tags=["Publications"]
)

logger = get_logger()

@router.get("/publication-types", response_model=ResponseDTO[list[str]])
async def get_publication_types():
    return ResponseDTO(
        status=True,
        message="Publication types retrieved successfully",
        code=200,
        data=[type.value for type in PublicationType]
)

@router.get("/publication-statues", response_model=ResponseDTO[list[str]])
async def get_publication_status():
    return ResponseDTO(
        status=True,
        message="Publication statues retrieved successfully",
        code=200,
        data=[status.value for status in PublicationStatus]
)


@router.get("/", response_model=ResponseDTO[list[PublicationOut]])
async def get_publications(
    publication_repo: PublicationsRepository = Depends(get_publications_repo)
):
    publications = await publication_repo.get_all()

    return ResponseDTO(
        status=True,
        message="Publications retrieved successfully",
        code=200,
        data=publications
    )


@router.get("/{publication_id}", response_model=ResponseDTO[PublicationOut])
async def get_publication(
    publication_id: str,
    publication_repo: PublicationsRepository = Depends(get_publications_repo)
):
    publication = await publication_repo.get(publication_id)

    if not publication:
        raise HTTPException(
            status_code=404,
            detail="Publication not found"
        )

    return ResponseDTO(
        status=True,
        message="Publication retrieved successfully",
        code=200,
        data=publication
    )


@router.post("/", response_model=ResponseDTO[PublicationOut])
async def add_publication(
    publication: PublicationCreate,
    publication_repo: PublicationsRepository = Depends(get_publications_repo)
):
    publication_dict = publication.model_dump()

    new_publication = await publication_repo.create(publication_dict)

    return ResponseDTO(
        status=True,
        message="Publication created successfully",
        code=201,
        data=new_publication
    )


@router.put("/{publication_id}", response_model=ResponseDTO[PublicationOut])
async def update_publication(
    publication_id: str,
    publication: PublicationUpdate,
    publication_repo: PublicationsRepository = Depends(get_publications_repo)
):
    existing_publication = await publication_repo.get(publication_id)

    if not existing_publication:
        raise HTTPException(
            status_code=404,
            detail="Publication not found"
        )

    update_data = publication.model_dump(exclude_unset=True)

    updated_publication = await publication_repo.update(
        existing_publication,
        update_data
    )

    return ResponseDTO(
        status=True,
        message="Publication updated successfully",
        code=200,
        data=updated_publication
    )


@router.delete("/{publication_id}", response_model=ResponseDTO[bool])
async def delete_publication(
    publication_id: str,
    publication_repo: PublicationsRepository = Depends(get_publications_repo)
):
    publication = await publication_repo.get(publication_id)

    if not publication:
        raise HTTPException(
            status_code=404,
            detail="Publication not found"
        )

    await publication_repo.delete(publication)

    return ResponseDTO(
        status=True,
        message="Publication deleted successfully",
        code=200,
        data=True
    )