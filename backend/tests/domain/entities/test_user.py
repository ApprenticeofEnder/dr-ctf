from faker import Faker

from dr_ctf.domain.entities import User


def test_user_creation(faker: Faker):
    email = faker.email()
    name = faker.name()

    user = User(email=email, display_name=name)
    assert user.email == email
    assert user.display_name == name
    assert user.id is not None
