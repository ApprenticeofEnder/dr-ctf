from typing import Any

import pytest

from dr_ctf.application.features.challenge.challenge_service import (
    ChallengeService,
)
from dr_ctf.domain.entities import Challenge

pytestmark = pytest.mark.asyncio()


async def test_challenge_create(
    challenge: Challenge,
    persisted_challenge: Challenge,
    mock_uow: Any,
    mock_challenge_repo: Any,
):
    mock_challenge_repo.save.return_value = persisted_challenge

    async with mock_uow:
        service = ChallengeService(mock_uow)
        created_challenge = await service.create_challenge(
            **challenge.data_dump()
        )

        assert created_challenge.name == challenge.name
        assert (
            created_challenge.author.display_name
            == challenge.author.display_name
        )

        mock_uow.__aenter__.return_value.commit.assert_called_once()
