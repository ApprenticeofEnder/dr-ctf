import pytest

from dr_ctf.application.features.user import UserService
from dr_ctf.domain.entities import User
from tests.application.fixtures.in_memory_unit_of_work import InMemoryUnitOfWork

pytestmark = pytest.mark.asyncio()


async def test_user_create(user: User):
    uow = InMemoryUnitOfWork()
    user_service = UserService(uow)

    name = user.display_name
    email = user.email

    user = await user_service.create_user(user.display_name, user.email)

    assert user.display_name == name
    assert user.email == email
    assert user.id is not None
    assert user.created_at is not None
    assert user.updated_at is not None
