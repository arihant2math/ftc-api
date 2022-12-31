from enum import Enum


class Stone(str, Enum):
    NONE = "NONE"
    STONE = "STONE"
    SKYSTONE = "SKYSTONE"

    def __str__(self) -> str:
        return str(self.value)
