from typing import Annotated

from pydantic import Field, IPvAnyAddress

from dr_ctf.domain.entities.base_object import BaseObject
from dr_ctf.domain.entities.user import User
from dr_ctf.domain.enumerators.challenge_category import ChallengeCategory


class Challenge(BaseObject):
    name: str
    category: ChallengeCategory
    author: User
    ip: IPvAnyAddress
    port: Annotated[int, Field(gt=0, lt=65536)] | None
    ssh_port: Annotated[int, Field(gt=0, lt=65536)] | None
