from dr_ctf.application.common.unit_of_work import IUnitOfWork
from dr_ctf.domain.entities import User


class UserService:
    _uow: IUnitOfWork

    def __init__(self, uow: IUnitOfWork):
        self._uow = uow

    async def create_user(self, display_name: str, email: str) -> User:
        async with self._uow as uow:
            user = User(display_name=display_name, email=email)
            saved = await uow.users.save(user)
            await uow.commit()
            return saved
