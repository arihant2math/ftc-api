from enum import Enum


class EndgameParkedStatus(str, Enum):
    NONE = "NONE"
    IN_WAREHOUSE = "IN_WAREHOUSE"
    COMPLETELY_IN_WAREHOUSE = "COMPLETELY_IN_WAREHOUSE"

    def __str__(self) -> str:
        return str(self.value)
