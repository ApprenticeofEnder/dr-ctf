from typing import Any
from unittest.mock import create_autospec

import pytest

from dr_ctf.application.common.unit_of_work import IUnitOfWork
from dr_ctf.domain.repositories import IChallengeRepository, IUserRepository


@pytest.fixture(name="mock_uow")
def fixture_mock_uow():
    mock_user_repo = create_autospec(IUserRepository, instance=True)
    mock_challenge_repo = create_autospec(IChallengeRepository, instance=True)

    mock_uow = create_autospec(IUnitOfWork, instance=True)
    mock_uow_context = mock_uow.__aenter__.return_value
    mock_uow_context.users = mock_user_repo
    mock_uow_context.challenges = mock_challenge_repo

    return mock_uow


@pytest.fixture(name="mock_user_repo")
def fixture_mock_user_repo(mock_uow: Any):
    mock_user_repo = mock_uow.__aenter__.return_value.users
    return mock_user_repo


@pytest.fixture(name="mock_challenge_repo")
def fixture_mock_challenge_repo(mock_uow: Any):
    mock_challenge_repo = mock_uow.__aenter__.return_value.challenges
    return mock_challenge_repo
