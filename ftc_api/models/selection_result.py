from enum import Enum


class SelectionResult(str, Enum):
    ACCEPT = "ACCEPT"
    CAPTAIN = "CAPTAIN"
    DECLINE = "DECLINE"

    def __str__(self) -> str:
        return str(self.value)
