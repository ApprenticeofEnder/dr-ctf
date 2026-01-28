from enum import StrEnum


class ChallengeStatus(StrEnum):
    HEALTHY = "Healthy"
    FLAKY = "Flaky"
    DOWN = "Down"
