from ipaddress import IPv4Address

from faker import Faker

from dr_ctf.domain.entities import Challenge, User
from dr_ctf.domain.enumerators import ChallengeCategory
from dr_ctf.domain.value_objects import HttpPort, HttpsPort
from dr_ctf.domain.value_objects.port import SshPort


def test_challenge_creation(faker: Faker, user: User):
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
        ssh_port=SshPort(),
    )

    assert challenge.name == name
    assert challenge.author == author
    assert challenge.ip == ip
    assert challenge.category == challenge_category
    assert challenge.ports
    assert challenge.ports[0].value == 80
    assert challenge.ports[1].value == 443
    assert challenge.ssh_port
    assert challenge.ssh_port.value == 22
    assert challenge.id is not None
