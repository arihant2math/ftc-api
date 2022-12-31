from enum import Enum


class GetV20SeasonScheduleEventCodeTournamentLevelHybridTournamentLevel(str, Enum):
    QUAL = "qual"
    PLAYOFF = "playoff"

    def __str__(self) -> str:
        return str(self.value)
