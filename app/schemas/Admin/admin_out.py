

from datetime import datetime

from pydantic import BaseModel, ConfigDict, ConfigDict


class AdminOut(BaseModel):
    id: int
    email: str
    created_at: datetime
    updated_at: datetime
    password: str
    model_config = ConfigDict(from_attributes=True)