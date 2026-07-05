from fastapi import APIRouter
from typing import Dict, Any

from app.schemas.response import ResponseDTO
from app.core.logging import get_logger

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)

logger = get_logger()


@router.get("/", response_model=ResponseDTO[Dict[str, Any]])
async def health_check():
    logger.info("Health check called")

    return ResponseDTO(
        status=True,
        message="Service is healthy",
        code=200,
        data={
            "service": "phd-portfolio-api",
            "status": "up"
        }
    )