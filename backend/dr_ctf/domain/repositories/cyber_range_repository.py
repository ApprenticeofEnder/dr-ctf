from abc import ABC

from dr_ctf.domain.entities.cyber_range import CyberRange
from dr_ctf.domain.repositories.base_repository import IBaseRepository


class ICyberRangeRepository(IBaseRepository[CyberRange], ABC):
    pass
