from enum import Enum


class EndgameParkedStatus(str, Enum):
    COMPLETELY_IN_WAREHOUSE = "COMPLETELY_IN_WAREHOUSE"
    IN_WAREHOUSE = "IN_WAREHOUSE"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
