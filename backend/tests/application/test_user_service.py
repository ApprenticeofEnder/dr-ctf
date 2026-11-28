from typing import Any

import pytest

from dr_ctf.application.features.user import UserService
from dr_ctf.domain.entities import User
from dr_ctf.domain.entities.base_object import cuid_generator

pytestmark = pytest.mark.asyncio()


async def test_user_create(
    user: User, persisted_user: User, mock_uow: Any, mock_user_repo: Any
):
    mock_user_repo.save.return_value = persisted_user

    async with mock_uow:
        service = UserService(mock_uow)
        created_user = await service.create_user(
            **user.model_dump(include={"email", "display_name"})
        )

        assert created_user.display_name == user.display_name
        assert created_user.email == user.email
        assert created_user.id is not None
        assert created_user.created_at is not None
        assert created_user.updated_at is not None

        assert user.created_at is None
        assert user.updated_at is None

        mock_uow.__aenter__.return_value.commit.assert_called_once()


async def test_user_get_by_id_success(
    persisted_user: User, mock_uow: Any, mock_user_repo: Any
):
    mock_user_repo.get_by_id.return_value = persisted_user

    async with mock_uow:
        service = UserService(mock_uow)
        retrieved_user = await service.get_user_by_id(persisted_user.id)

        assert retrieved_user is not None
        assert retrieved_user.id == persisted_user.id
        assert retrieved_user.display_name == persisted_user.display_name


async def test_user_get_by_id_fail(mock_uow: Any, mock_user_repo: Any):
    mock_user_repo.get_by_id.return_value = None

    async with mock_uow:
        service = UserService(mock_uow)
        retrieved_user = await service.get_user_by_id(cuid_generator())

        assert retrieved_user is None


async def test_user_get_by_email_success(
    persisted_user: User, mock_uow: Any, mock_user_repo: Any
):
    mock_user_repo.get_by_email.return_value = persisted_user

    async with mock_uow:
        service = UserService(mock_uow)
        retrieved_user = await service.get_user_by_email(persisted_user.email)

        assert retrieved_user is not None
        assert retrieved_user.id == persisted_user.id
        assert retrieved_user.display_name == persisted_user.display_name


async def test_user_get_by_email_fail(mock_uow: Any, mock_user_repo: Any):
    mock_user_repo.get_by_email.return_value = None

    async with mock_uow:
        service = UserService(mock_uow)
        retrieved_user = await service.get_user_by_email("test@example.com")

        assert retrieved_user is None
