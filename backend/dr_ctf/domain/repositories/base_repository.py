from abc import ABC, abstractmethod
from typing import TypeVar

T = TypeVar("T")


class IBaseRepository[T](ABC):
    @abstractmethod
    async def get_by_id(self, id: str) -> T | None:
        pass

    @abstractmethod
    async def save(self, entity: T) -> T:
        pass

    @abstractmethod
    async def list_all(self) -> list[T]:
        pass
