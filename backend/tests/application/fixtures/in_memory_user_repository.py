from datetime import datetime
from typing import override

from dr_ctf.domain.entities import User
from dr_ctf.domain.repositories import IUserRepository


class InMemoryUserRepository(IUserRepository):
    users: dict[str, User]

    def __init__(self) -> None:
        self.users = {}

    @override
    async def list_all(self) -> list[User]:
        return sorted(
            list(self.users.values()),
            key=lambda x: x.created_at or datetime.fromtimestamp(0),
        )

    @override
    async def save(self, entity: User) -> User:
        current_time = datetime.now()

        if entity.created_at is None:
            entity.created_at = current_time

        entity.updated_at = current_time

        self.users[entity.id] = entity

        return self.users[entity.id]

    @override
    async def get_by_id(self, id: str) -> User | None:
        return self.users.get(id)

    @override
    async def get_by_email(self, email: str) -> User | None:
        for _, user in self.users.items():
            if user.email == email:
                return user
        return None
