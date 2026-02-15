from ipaddress import IPv4Address

from dr_ctf.application.common.unit_of_work import IUnitOfWork
from dr_ctf.domain.entities import Challenge, User
from dr_ctf.domain.enumerators import ChallengeCategory
from dr_ctf.domain.value_objects import Port, SshPort


class ChallengeService:
    def __init__(self, uow: IUnitOfWork):
        self._uow = uow

    async def create_challenge(
        self,
        name: str,
        category: ChallengeCategory,
        author: User,
        ip: IPv4Address,
        ports: list[Port],
        ssh_port: SshPort | None,
    ) -> Challenge:
        async with self._uow as uow:
            challenge = Challenge(
                name=name,
                category=category,
                author=author,
                ip=ip,
                ports=ports,
                ssh_port=ssh_port,
            )
            saved = await uow.challenges.save(challenge)
            await uow.commit()
            return saved
