from dr_ctf.domain.entities.base_object import BaseObject
from dr_ctf.domain.value_objects.ssh_public_key import SshPublicKey


class User(BaseObject):
    email: str
    name: str
    public_key: SshPublicKey | None = None

    def add_public_key(self, new_key: SshPublicKey) -> bool:
        is_replaced = self.public_key is not None
        self.public_key = new_key
        return is_replaced
