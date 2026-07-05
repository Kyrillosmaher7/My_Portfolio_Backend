from fastapi import APIRouter, Depends

from app.core.logging import get_logger
from app.deps import get_admin_repo
from app.repositories.admin_repo import AdminRepository
from app.repositories.admin_repo import AdminRepository
from app.schemas.Admin.admin_out import AdminOut
from app.schemas.response import ResponseDTO
from app.schemas.response import ResponseDTO
from app.schemas.Admin.create_admin import CreateAdmin
from app.services.password_service import PasswordService

router = APIRouter(
    prefix="/admins",
    tags=["Admins"]
)

logger = get_logger()

@router.post("/", response_model=ResponseDTO[AdminOut], status_code=201)
async def create_admin(
    admin_data: CreateAdmin,
    admin_repo: AdminRepository = Depends(get_admin_repo),
    password_service: PasswordService = Depends(PasswordService)
):
    """
    Create a new admin.
    """
    logger.info("Creating a new admin with email: %s", admin_data.email)
    hashed_password = password_service.hash_password(admin_data.password)

    admin_dict = admin_data.model_dump(exclude={"password"})
    admin_dict["password_hash"] = hashed_password

    new_admin = await admin_repo.create(admin_dict)
    return ResponseDTO(
         status=True,
         code=201,
         data=new_admin,
         message="Admin created successfully."
        )