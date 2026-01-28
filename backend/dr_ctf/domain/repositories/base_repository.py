from abc import ABC, abstractmethod
from typing import TypeVar
from uuid import UUID

T = TypeVar("T")


class IBaseRepository[T](ABC):
    @abstractmethod
    async def get_by_id(self, id: UUID) -> T | None:
        pass

    @abstractmethod
    async def save(self, entity: T) -> T:
        pass

    @abstractmethod
    async def list_all(self) -> list[T]:
        pass
