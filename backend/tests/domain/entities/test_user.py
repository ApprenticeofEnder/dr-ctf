from dr_ctf.domain.entities.user import User


def test_user_creation():
    user = User(email="test@test.com", name="Test User")
    assert user.email == "test@test.com"


# class User(BaseObject):
#     email: str
#     name: str
#     public_key: SshPublicKey | None = None
#
#     def add_public_key(self, new_key: SshPublicKey) -> bool:
#         is_replaced = self.public_key is not None
#         self.public_key = new_key
#         return is_replaced
