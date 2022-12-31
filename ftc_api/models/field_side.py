from enum import Enum


class FieldSide(str, Enum):
    SCORING_SIDE = "SCORING_SIDE"
    AUDIENCE_SIDE = "AUDIENCE_SIDE"

    def __str__(self) -> str:
        return str(self.value)
