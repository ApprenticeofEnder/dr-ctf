from copy import deepcopy
from typing import Any, override

from dr_ctf.application.common.unit_of_work import IUnitOfWork
from dr_ctf.domain.entities import User
from tests.application.fixtures.in_memory_user_repository import (
    InMemoryUserRepository,
)


class InMemoryUnitOfWork(IUnitOfWork):
    _saved_users_state: dict[str, User]

    def __init__(self) -> None:
        self.users: InMemoryUserRepository = InMemoryUserRepository()  # pyright:ignore[reportIncompatibleVariableOverride]
        self._saved_users_state = {}

    @override
    async def __aenter__(self) -> "IUnitOfWork":
        self._saved_users_state = deepcopy(self.users.users)

        return self

    @override
    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: Any,  # pyright:ignore[reportExplicitAny, reportAny]
    ):
        await self.rollback()

    @override
    async def commit(self) -> None:
        self._saved_users_state = deepcopy(self.users.users)

    @override
    async def rollback(self) -> None:
        self.users.users = self._saved_users_state
