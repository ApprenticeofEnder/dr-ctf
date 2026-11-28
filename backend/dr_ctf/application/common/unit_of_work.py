from abc import ABC, abstractmethod
from typing import Any

from dr_ctf.domain.repositories import (
    IChallengeProbeRepository,
    IChallengeRepository,
    ICyberRangeRepository,
    IRangeChallengeProbeRepository,
    IUserRepository,
)


class IUnitOfWork(ABC):
    # keep-sorted start
    challenge_probes: IChallengeProbeRepository
    challenges: IChallengeRepository
    cyber_ranges: ICyberRangeRepository
    range_challenge_probes: IRangeChallengeProbeRepository
    users: IUserRepository
    # keep-sorted end

    @abstractmethod
    async def __aenter__(self) -> "IUnitOfWork":
        return self

    @abstractmethod
    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: Any,
    ):
        pass

    @abstractmethod
    async def commit(self) -> None:
        pass

    @abstractmethod
    async def rollback(self) -> None:
        pass
