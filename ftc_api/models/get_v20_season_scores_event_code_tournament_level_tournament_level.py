from enum import Enum


class GetV20SeasonScoresEventCodeTournamentLevelTournamentLevel(str, Enum):
    PLAYOFF = "playoff"
    QUAL = "qual"

    def __str__(self) -> str:
        return str(self.value)
