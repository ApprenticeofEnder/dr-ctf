from abc import ABC, abstractmethod

from dr_ctf.domain.repositories import (
    IChallengeProbeRepository,
    IChallengeRepository,
    ICyberRangeRepository,
    IProbeRepository,
    IUserRepository,
)


class IUnitOfWork(ABC):
    challenge_probes: IChallengeProbeRepository
    challenges: IChallengeRepository
    probes: IProbeRepository
    cyber_ranges: ICyberRangeRepository
    users: IUserRepository

    @abstractmethod
    async def __aenter__(self) -> "IUnitOfWork":
        return self

    @abstractmethod
    async def __aexit__(self, *args):
        pass

    @abstractmethod
    async def commit(self) -> None:
        pass

    @abstractmethod
    async def rollback(self) -> None:
        pass
