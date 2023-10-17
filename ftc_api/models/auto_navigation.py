from enum import Enum


class AutoNavigation(str, Enum):
    NONE = "NONE"
    SIGNAL_ZONE = "SIGNAL_ZONE"
    SUBSTATION_TERMINAL = "SUBSTATION_TERMINAL"

    def __str__(self) -> str:
        return str(self.value)
