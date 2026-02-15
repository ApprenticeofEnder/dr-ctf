from pydantic import IPvAnyAddress

from dr_ctf.domain.entities.base_object import BaseObject
from dr_ctf.domain.entities.user import User
from dr_ctf.domain.enumerators import ChallengeCategory
from dr_ctf.domain.value_objects import Port, SshPort


class Challenge(BaseObject):
    name: str
    category: ChallengeCategory
    author: User
    ip: IPvAnyAddress
    ports: list[Port] | None
    ssh_port: SshPort = SshPort()
