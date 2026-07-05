from app.models.repositories import Repository
from app.repositories.base import BaseRepository

class RepositoriesRepository(BaseRepository[Repository]):
    def __init__(self, session):
        super().__init__(Repository, session)