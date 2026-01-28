from abc import ABC
from http import HTTPStatus

from dr_ctf.domain.entities.base_object import BaseObject
from dr_ctf.domain.entities.challenge import Challenge


class Probe(BaseObject, ABC):
    challenge: Challenge
    timeout_seconds: int
    delay_seconds: int


class HttpProbe(Probe):
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
