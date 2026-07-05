from app.models.production_project import ProductionProject
from app.repositories.base import BaseRepository


class ProductionProjectRepository(BaseRepository[ProductionProject]):
    def __init__(self, session):
        super().__init__(ProductionProject, session)