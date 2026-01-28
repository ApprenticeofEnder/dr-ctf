from abc import abstractmethod
from uuid import UUID

from dr_ctf.domain.entities.challenge import Challenge
from dr_ctf.domain.enumerators.challenge_category import ChallengeCategory
from dr_ctf.domain.repositories.base_repository import IBaseRepository


class IChallengeRepository(IBaseRepository[Challenge]):
    @abstractmethod
    async def get_by_name(self, name: str) -> Challenge | None:
        pass

    @abstractmethod
    async def list_by_category(
        self, category: ChallengeCategory
    ) -> list[Challenge]:
        pass

    @abstractmethod
    async def list_by_author(self, author_id: UUID) -> list[Challenge]:
        pass
