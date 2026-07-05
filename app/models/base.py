import uuid

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """Shared declarative base for every table in this file."""
    pass


def _uuid() -> str:
    """Default id generator — string UUIDs, so ids stay JSON-friendly
    and match the frontend's existing string ids ('pub-01', 'repo-01')."""
    return str(uuid.uuid4())