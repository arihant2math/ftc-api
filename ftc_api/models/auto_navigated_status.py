from enum import Enum


class AutoNavigatedStatus(str, Enum):
    NONE = "NONE"
    IN_STORAGE = "IN_STORAGE"
    COMPLETELY_IN_STORAGE = "COMPLETELY_IN_STORAGE"
    IN_WAREHOUSE = "IN_WAREHOUSE"
    COMPLETELY_IN_WAREHOUSE = "COMPLETELY_IN_WAREHOUSE"

    def __str__(self) -> str:
        return str(self.value)
