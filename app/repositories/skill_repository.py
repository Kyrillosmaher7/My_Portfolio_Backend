


from app.models.skill import Skill
from app.repositories.base import BaseRepository


class SkillRepository(BaseRepository[Skill]):
    def __init__(self, session):
        super().__init__(Skill, session)
        self.model = Skill
        
    async def get_by_name(self, name: str):
     result = await self.session.execute(self.model.__table__.select().where(self.model.name == name))
     return result.first()
    