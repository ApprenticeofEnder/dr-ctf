from abc import abstractmethod
from uuid import UUID

from dr_ctf.domain.entities.challenge_probe import ChallengeProbe
from dr_ctf.domain.enumerators.challenge_status import ChallengeStatus
from dr_ctf.domain.repositories.base_repository import IBaseRepository


class IChallengeProbeRepository(IBaseRepository[ChallengeProbe]):
    @abstractmethod
    async def get_by_name(self, name: str) -> ChallengeProbe | None:
        pass

    @abstractmethod
    async def list_by_challenge(
        self, challenge_id: UUID
    ) -> list[ChallengeProbe]:
        pass

    @abstractmethod
    async def list_by_cyber_range(
        self, cyber_range_id: UUID
    ) -> list[ChallengeProbe]:
        pass

    @abstractmethod
    async def list_by_author(self, author_id: UUID) -> list[ChallengeProbe]:
        pass

    @abstractmethod
    async def list_by_status(
        self, challenge_status: ChallengeStatus
    ) -> list[ChallengeProbe]:
        pass
