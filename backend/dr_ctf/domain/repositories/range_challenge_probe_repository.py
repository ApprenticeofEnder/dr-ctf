from abc import ABC, abstractmethod

from dr_ctf.domain.entities.range_challenge_probe import RangeChallengeProbe
from dr_ctf.domain.enumerators.challenge_status import ChallengeStatus
from dr_ctf.domain.repositories.base_repository import IBaseRepository


class IRangeChallengeProbeRepository(IBaseRepository[RangeChallengeProbe], ABC):
    @abstractmethod
    async def get_by_challenge_name(
        self, name: str
    ) -> RangeChallengeProbe | None:
        pass

    @abstractmethod
    async def list_for_challenge(
        self, challenge_id: str
    ) -> list[RangeChallengeProbe]:
        pass

    @abstractmethod
    async def list_for_cyber_range(
        self, cyber_range_id: str
    ) -> list[RangeChallengeProbe]:
        pass

    @abstractmethod
    async def list_for_author(
        self, author_id: str
    ) -> list[RangeChallengeProbe]:
        pass

    @abstractmethod
    async def list_for_status(
        self, challenge_status: ChallengeStatus
    ) -> list[RangeChallengeProbe]:
        pass
