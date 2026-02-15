from abc import ABC, abstractmethod
from http import HTTPStatus

from dr_ctf.domain.entities.base_object import BaseObject
from dr_ctf.domain.entities.challenge import Challenge
from dr_ctf.domain.enumerators.probe_type import ProbeType
from dr_ctf.domain.value_objects.port import Port


class Probe(BaseObject, ABC):
    challenge: Challenge
    timeout_seconds: int
    delay_seconds: int
    probe_type: ProbeType

    @abstractmethod
    def run_check(self):
        pass


class HttpProbe(Probe):
    port: Port
    endpoint: str
    expected_status_code: HTTPStatus


# class TcpProbe(Probe):
#     pass
#
#
# class DockerProbe(Probe):
#     pass
#
#
# class CommandProbe(Probe):
#     pass
