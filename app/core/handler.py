from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from app.schemas.response import ResponseDTO
from app.core.exceptions import AppException
from app.core.logging import get_logger

logger = get_logger()


async def app_exception_handler(request: Request, exc: AppException):
    logger.error(f"AppException: {exc.message} | {exc.errors}")

    return JSONResponse(
        status_code=exc.code,
        content=ResponseDTO(
            status=False,
            message=exc.message,
            code=exc.code,
            errors=exc.errors
        ).model_dump()
    )


async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled Exception: {str(exc)}")

    return JSONResponse(
        status_code=500,
        content=ResponseDTO(
            status=False,
            message="Internal Server Error",
            code=500,
            errors=[str(exc)]
        ).model_dump()
    )
async def http_exception_handler(request: Request, exc: HTTPException):

    logger.error(
        f"HTTPException | {request.method} {request.url.path} | "
        f"{exc.status_code} | {exc.detail}"
    )

    return JSONResponse(
        status_code=exc.status_code,
        content=ResponseDTO(
            status=False,
            message=str(exc.detail),
            code=exc.status_code,
            errors=[str(exc.detail)]
        ).model_dump()
    )