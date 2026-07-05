
from pydantic import BaseModel


class CreateAdmin(BaseModel):
    email: str
    password: str