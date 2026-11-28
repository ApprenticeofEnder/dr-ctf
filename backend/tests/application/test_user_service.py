from datetime import datetime
from typing import Any

import pytest

from dr_ctf.application.features.user import UserService
from dr_ctf.domain.entities import User

pytestmark = pytest.mark.asyncio()


async def test_user_create(user: User, mock_uow: Any):

    mock_user_repo = mock_uow.__aenter__.return_value.users
    mock_user_repo.save.return_value = User(
        **user.data_dump(),
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )

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
