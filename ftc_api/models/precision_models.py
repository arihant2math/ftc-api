from enum import Enum


class PrecisionModels(str, Enum):
    FLOATING = "Floating"
    FLOATINGSINGLE = "FloatingSingle"
    FIXED = "Fixed"

    def __str__(self) -> str:
        return str(self.value)
