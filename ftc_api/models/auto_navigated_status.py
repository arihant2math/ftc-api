from enum import Enum


class AutoNavigatedStatus(str, Enum):
    COMPLETELY_IN_STORAGE = "COMPLETELY_IN_STORAGE"
    COMPLETELY_IN_WAREHOUSE = "COMPLETELY_IN_WAREHOUSE"
    IN_STORAGE = "IN_STORAGE"
    IN_WAREHOUSE = "IN_WAREHOUSE"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
