from abc import abstractmethod

from dr_ctf.domain.entities.user import User
from dr_ctf.domain.repositories.base_repository import IBaseRepository


class IUserRepository(IBaseRepository[User]):
    @abstractmethod
    async def get_by_email(self, email: str) -> User | None:
        pass
