from enum import Enum


class FTCEventLevel(str, Enum):
    FINAL = "FINAL"
    OTHER = "OTHER"
    PLAYOFF = "PLAYOFF"
    QUALIFICATION = "QUALIFICATION"
    SEMIFINAL = "SEMIFINAL"

    def __str__(self) -> str:
        return str(self.value)
