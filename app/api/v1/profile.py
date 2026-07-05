from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from app.core.logging import get_logger
from app.deps import get_profile_repo
from app.schemas.profile.profile_update import ProfileUpdate
from app.schemas.profile.Profile import ProfileOut
from app.schemas.response import ResponseDTO
from app.repositories.profile_repository import ProfileRepository
from app.services.image_service import ProfileImageService

router = APIRouter(
 prefix="/profile",
 tags=["Profile"]
)

logger = get_logger()


@router.get("/", response_model=ResponseDTO[ProfileOut])
async def get_profile(
    repo: ProfileRepository = Depends(get_profile_repo)
):
    logger.info("Get profile called")
    profile = await repo.get()
    if not profile:
        return ResponseDTO(
            status=False,
            message="Profile not found",
            code=404,
            data=None
        )
    return ResponseDTO(
        status=True,
        message="Profile retrieved successfully",
        code=200,
        data=ProfileOut.model_validate(profile)
    )

@router.put("/update" , response_model=ResponseDTO[ProfileOut])
async def update_profile(
    profile_data: ProfileUpdate,
    repo: ProfileRepository = Depends(get_profile_repo),
):
    profile = await repo.get()

    if profile is None:
        raise HTTPException(
            status_code=404,
            detail="Profile not found"
        )

    updated_profile = await repo.update(
        profile,
        profile_data
    )

    return ResponseDTO(
        status=True,
        message="Profile updated successfully",
        code=200,
        data=ProfileOut.model_validate(updated_profile)
    )

@router.put("/image" , response_model=ResponseDTO[str])
async def update_profile_image(
    file: UploadFile = File(...),
    repo: ProfileRepository = Depends(get_profile_repo),
):
    profile = await repo.get()

    if profile is None:
        raise HTTPException(
            status_code=404,
            detail="Profile not found"
        )

    image_url = await ProfileImageService.upload_or_update_image(
        email=profile.email,
        file=file,
    )

    profile =await repo.update_image(
        profile,
        image_url,
    )

    return ResponseDTO(
        status=True,
        message="Profile retrieved successfully",
        code=200,
        data=profile.image
    )