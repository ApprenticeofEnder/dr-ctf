from datetime import datetime
from typing import Any

import pytest

from dr_ctf.application.features.challenge.challenge_service import (
    ChallengeService,
)
from dr_ctf.domain.entities import Challenge

pytestmark = pytest.mark.asyncio()


async def test_challenge_create(challenge: Challenge, mock_uow: Any):
    mock_challenge_repo = mock_uow.__aenter__.return_value.challenges
    mock_challenge_repo.save.return_value = Challenge(
        **challenge.data_dump(),
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )

    async with mock_uow:
        service = ChallengeService(mock_uow)
        created_challenge = await service.create_challenge(
            **challenge.data_dump()
        )

        assert created_challenge.name == challenge.name

        mock_uow.__aenter__.return_value.commit.assert_called_once()
