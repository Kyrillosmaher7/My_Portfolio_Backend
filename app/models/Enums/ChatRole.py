import enum


class ChatRole(str, enum.Enum):
    """Enum for chat roles."""
    USER = "user"
    ASSISTANT = "assistant"