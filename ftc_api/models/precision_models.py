from enum import Enum


class PrecisionModels(str, Enum):
    FIXED = "Fixed"
    FLOATING = "Floating"
    FLOATINGSINGLE = "FloatingSingle"

    def __str__(self) -> str:
        return str(self.value)
