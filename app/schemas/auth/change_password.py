from pydantic import BaseModel
from pydantic import Field


class ChangePasswordRequest(BaseModel):

    old_password: str

    new_password: str = Field(
        min_length=8
    )