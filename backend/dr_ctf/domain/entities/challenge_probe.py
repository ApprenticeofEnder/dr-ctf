from pydantic import computed_field

from dr_ctf.domain.entities.base_object import BaseObject
from dr_ctf.domain.entities.cyber_range import CyberRange
from dr_ctf.domain.entities.probe import Probe
from dr_ctf.domain.enumerators.challenge_status import ChallengeStatus


class ChallengeProbe(BaseObject):
    probe: Probe
    range: CyberRange
    failed_checks: int = 0

    def add_check(self, success: bool):
        if success:
            self.failed_checks = 0
            return
        self.failed_checks += 1

    @computed_field
    def status(self) -> ChallengeStatus:
        if self.failed_checks > 3:
            return ChallengeStatus.DOWN
        if self.failed_checks == 0:
            return ChallengeStatus.HEALTHY

        return ChallengeStatus.FLAKY
