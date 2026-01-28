from pydantic import IPvAnyAddress

from dr_ctf.domain.entities.base_object import BaseObject


class CyberRange(BaseObject):
    bastion_ip: IPvAnyAddress
