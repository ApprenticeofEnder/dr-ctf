from abc import ABC, abstractmethod

from dr_ctf.domain.entities.challenge_probe import ChallengeProbe
from dr_ctf.domain.enumerators.challenge_status import ChallengeStatus
from dr_ctf.domain.repositories.base_repository import IBaseRepository


class IChallengeProbeRepository(IBaseRepository[ChallengeProbe], ABC):
    @abstractmethod
    async def get_by_challenge_name(self, name: str) -> ChallengeProbe | None:
        pass

    @abstractmethod
    async def list_for_challenge(
        self, challenge_id: str
    ) -> list[ChallengeProbe]:
        pass

    @abstractmethod
    async def list_for_author(self, author_id: str) -> list[ChallengeProbe]:
        pass

    @abstractmethod
    async def list_for_status(
        self, challenge_status: ChallengeStatus
    ) -> list[ChallengeProbe]:
        pass
