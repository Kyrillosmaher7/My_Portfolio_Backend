from typing import Generic, TypeVar, Type, Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Any

from app.models.base import _uuid

T = TypeVar("T")

class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T], session: AsyncSession):
        self.model = model
        self.session = session

    async def get(self, id:str) -> Optional[T]:
        result = await self.session.get(self.model, id)
        return result

    async def get_all(self) -> List[T]:
        result = await self.session.execute(select(self.model))
        return result.scalars().all()

    async def create(self, obj_in: dict) -> T:
        obj = self.model(**obj_in)
        self.session.add(obj)
        await self.session.commit()
        await self.session.refresh(obj)
        return obj

    async def delete(self, obj: T):
        await self.session.delete(obj)
        await self.session.commit()
        


    async def update(self, obj: T, obj_in: Any) -> T:
        # Convert Pydantic model → dict if needed
        if hasattr(obj_in, "model_dump"):
            obj_in = obj_in.model_dump(exclude_unset=True)
        elif hasattr(obj_in, "dict"):
            obj_in = obj_in.dict(exclude_unset=True)

        for field, value in obj_in.items():
            if hasattr(obj, field):
                setattr(obj, field, value)

        await self.session.commit()
        await self.session.refresh(obj)
        return obj