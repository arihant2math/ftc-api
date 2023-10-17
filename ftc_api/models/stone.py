from enum import Enum


class Stone(str, Enum):
    NONE = "NONE"
    SKYSTONE = "SKYSTONE"
    STONE = "STONE"

    def __str__(self) -> str:
        return str(self.value)
