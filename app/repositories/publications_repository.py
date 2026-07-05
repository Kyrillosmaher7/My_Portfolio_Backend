
from app.models.publication import Publication
from app.repositories.base import BaseRepository


class PublicationsRepository(BaseRepository[Publication]):
    def __init__(self, session):
        super().__init__(Publication, session)