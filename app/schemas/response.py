# app/schemas/response.py

from pydantic import BaseModel
from typing import Generic, TypeVar, Optional, List

T = TypeVar("T")


class ResponseDTO(BaseModel, Generic[T]):
    status: bool
    message: str
    code: int = 200
    data: Optional[T] = None
    errors: Optional[List[str]] = None