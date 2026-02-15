from faker import Faker

from dr_ctf.domain.entities.user import User


def test_user_creation(faker: Faker):
    email = faker.email()
    name = faker.name()

    user = User(email=email, name=name)
    assert user.email == email
    assert user.name == name
    assert user.id is not None
