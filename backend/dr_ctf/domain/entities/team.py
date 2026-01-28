from dr_ctf.domain.entities.base_object import BaseObject
from dr_ctf.domain.entities.cyber_range import CyberRange


class Team(BaseObject):
    name: str
    cyber_range: CyberRange
