
from app.models.chat_message import ChatMessage
from app.repositories.base import BaseRepository


class ChatMessageRepository(BaseRepository[ChatMessage]):
    def __init__(self, session):
        super().__init__(ChatMessage, session)