from enum import Enum


class SelectionResult(str, Enum):
    ACCEPT = "ACCEPT"
    DECLINE = "DECLINE"
    CAPTAIN = "CAPTAIN"

    def __str__(self) -> str:
        return str(self.value)
