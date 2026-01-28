from dr_ctf.domain.entities.base_object import BaseObject


class User(BaseObject):
    email: str
    name: str
    public_key: str | None = None

    def add_public_key(self, new_key: str) -> bool:
        is_replaced = self.public_key is not None
        self.public_key = new_key
        return is_replaced
