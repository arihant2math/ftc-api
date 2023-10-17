from enum import Enum


class FieldSide(str, Enum):
    AUDIENCE_SIDE = "AUDIENCE_SIDE"
    SCORING_SIDE = "SCORING_SIDE"

    def __str__(self) -> str:
        return str(self.value)
