from dr_ctf.domain.entities.base_object import BaseObject
from dr_ctf.domain.entities.cyber_range import CyberRange


# TODO: Flesh this out with players, etc.
class Team(BaseObject):
    name: str
    cyber_range: CyberRange
