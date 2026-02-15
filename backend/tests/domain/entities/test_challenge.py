from ipaddress import IPv4Address

from faker import Faker

from dr_ctf.domain.entities.challenge import Challenge
from dr_ctf.domain.entities.user import User
from dr_ctf.domain.enumerators.challenge_category import ChallengeCategory
from dr_ctf.domain.value_objects.port import HttpPort, HttpsPort


def test_challenge_creation(faker: Faker):
    name = faker.text(max_nb_chars=80)
    author_name = faker.name()
    author_email = faker.email()
    challenge_category = faker.random_element(ChallengeCategory)
    ip = IPv4Address(faker.ipv4())
    ports = [HttpPort(), HttpsPort()]
    author = User(name=author_name, email=author_email)
    challenge = Challenge(
        name=name,
        author=author,
        category=challenge_category,
        ip=ip,
        ports=ports,
    )

    assert challenge.name == name
    assert challenge.author == author
    assert challenge.ip == ip
    assert challenge.ports
    assert challenge.ports[0].value == 80
    assert challenge.ports[1].value == 443


# class Challenge(BaseObject):
#     name: str
#     category: ChallengeCategory
#     author: User
#     ip: IPvAnyAddress
#     ports: list[Port] | None
#     ssh_port: SshPort | None
