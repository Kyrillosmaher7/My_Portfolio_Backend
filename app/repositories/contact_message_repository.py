from sqlalchemy import select

from app.models.contact_message import ContactMessage
from app.models.message_reply import ContactMessageReply
from app.repositories.base import BaseRepository

from sqlalchemy import select

class ContactMessageRepository(BaseRepository[ContactMessage]):

    def __init__(self, session):
        super().__init__(ContactMessage, session)

    async def get_unread_messages(self):
        result = await self.session.execute(
            select(ContactMessage)
            .where(ContactMessage.is_read.is_(False))
            .order_by(ContactMessage.created_at.desc())
        )

        return result.scalars().all()

    async def mark_as_read(self, message: ContactMessage):
        message.is_read = True

        await self.session.commit()
        await self.session.refresh(message)

        return message

    async def get_replies(self, message_id: str):
        result = await self.session.execute(
            select(ContactMessageReply)
            .where(ContactMessageReply.message_id == message_id)
            .order_by(ContactMessageReply.created_at.asc())
        )

        return result.scalars().all()

    async def get_reply(self, reply_id: str):
        result = await self.session.execute(
            select(ContactMessageReply)
            .where(ContactMessageReply.id == reply_id)
        )

        return result.scalar_one_or_none()

    async def create_reply(self, data: dict):
        reply = ContactMessageReply(**data)

        self.session.add(reply)

        await self.session.commit()
        await self.session.refresh(reply)

        return reply

    async def delete_reply(self, reply: ContactMessageReply):
        await self.session.delete(reply)
        await self.session.commit()

    async def delete_message(self, message: ContactMessage):
        await self.session.delete(message)
        await self.session.commit()