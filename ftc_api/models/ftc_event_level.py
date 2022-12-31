from enum import Enum


class FTCEventLevel(str, Enum):
    OTHER = "OTHER"
    QUALIFICATION = "QUALIFICATION"
    SEMIFINAL = "SEMIFINAL"
    FINAL = "FINAL"
    PLAYOFF = "PLAYOFF"

    def __str__(self) -> str:
        return str(self.value)
