from abc import abstractmethod

from dr_ctf.domain.entities.probe import Probe
from dr_ctf.domain.enumerators.challenge_status import ChallengeStatus
from dr_ctf.domain.repositories.base_repository import IBaseRepository


class IProbeRepository(IBaseRepository[Probe]):
    @abstractmethod
    async def list_by_challenge(self, challenge_id: str) -> list[Probe]:
        pass

    @abstractmethod
    async def list_by_status(
        self, challenge_status: ChallengeStatus
    ) -> list[Probe]:
        pass
