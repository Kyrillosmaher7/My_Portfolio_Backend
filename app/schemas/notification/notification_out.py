from datetime import datetime

from pydantic import BaseModel


class NotificationOut(BaseModel):
    id: str
    title: str
    content: str
    is_read: bool
    created_at: datetime

    model_config = {
        "from_attributes": True
    }