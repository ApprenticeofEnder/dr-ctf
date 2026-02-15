from faker import Faker

from dr_ctf.domain.entities.user import User


def test_user_creation(faker: Faker):
    email = faker.email()
    name = faker.name()

    user = User(email=email, name=name)
    assert user.email == email
    assert user.name == name
    assert user.id is not None


# class User(BaseObject):
#     email: str
#     name: str
#     public_key: SshPublicKey | None = None
#
#     def add_public_key(self, new_key: SshPublicKey) -> bool:
#         is_replaced = self.public_key is not None
#         self.public_key = new_key
#         return is_replaced
