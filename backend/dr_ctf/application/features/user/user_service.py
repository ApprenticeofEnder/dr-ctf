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

    async def get_user_by_id(self, id: str) -> User | None:
        async with self._uow as uow:
            user = await uow.users.get_by_id(id=id)
            return user

    async def get_user_by_email(self, email: str) -> User | None:
        async with self._uow as uow:
            user = await uow.users.get_by_email(email=email)
            return user
