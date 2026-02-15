from ipaddress import IPv4Address

import pytest
from faker import Faker

from dr_ctf.domain.entities.challenge import Challenge
from dr_ctf.domain.entities.user import User
from dr_ctf.domain.enumerators.challenge_category import ChallengeCategory
from dr_ctf.domain.value_objects.port import HttpPort, HttpsPort


@pytest.fixture(name="user")
def fixture_user(faker: Faker) -> User:
    user = User(name=faker.name(), email=faker.email())
    return user


@pytest.fixture(name="challenge")
def fixture_challenge(faker: Faker, user: User) -> Challenge:
    name = faker.text(max_nb_chars=80)
    author = user
    challenge_category = faker.random_element(ChallengeCategory)
    ip = IPv4Address(faker.ipv4())
    ports = [HttpPort(), HttpsPort()]
    challenge = Challenge(
        name=name,
        author=author,
        category=challenge_category,
        ip=ip,
        ports=ports,
    )
    return challenge
