from datetime import datetime
from ipaddress import IPv4Address

import pytest
from faker import Faker

from dr_ctf.domain.entities.challenge import Challenge
from dr_ctf.domain.entities.user import User
from dr_ctf.domain.enumerators.challenge_category import ChallengeCategory
from dr_ctf.domain.value_objects.port import HttpPort, HttpsPort, Port


@pytest.fixture(name="user")
def fixture_user(faker: Faker) -> User:
    user = User(display_name=faker.name(), email=faker.email())
    return user


@pytest.fixture(name="persisted_user")
def fixture_persisted_user(user: User) -> User:
    persisted_user = User(
        **user.data_dump(),
        id=user.id,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    return persisted_user


@pytest.fixture(name="challenge")
def fixture_challenge(faker: Faker, user: User) -> Challenge:
    name = faker.text(max_nb_chars=80)
    author = user
    challenge_category = faker.random_element(ChallengeCategory)
    ip = IPv4Address(faker.ipv4())
    ports: list[Port] = [HttpPort(), HttpsPort()]
    challenge = Challenge(
        name=name,
        author=author,
        category=challenge_category,
        ip=ip,
        ports=ports,
    )
    return challenge


@pytest.fixture(name="persisted_challenge")
def fixture_persisted_challenge(challenge: Challenge) -> Challenge:
    persisted_challenge = Challenge(
        **challenge.data_dump(),
        id=challenge.id,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    return persisted_challenge
