from abc import ABC, abstractmethod

from dr_ctf.domain.entities.base_object import BaseObject
from dr_ctf.domain.entities.challenge import Challenge
from dr_ctf.domain.enumerators.probe_type import ProbeType


class Probe(BaseObject, ABC):
    challenge: Challenge
    timeout_seconds: int
    delay_seconds: int
    probe_type: ProbeType

    @abstractmethod
    def run_check(self):
        pass
