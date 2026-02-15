from enum import StrEnum


class ProbeType(StrEnum):
    HTTP = "HTTP"
    TCP = "TCP"
    DOCKER = "Docker"
    COMMAND = "Command"
