from enum import Enum


class AutoNavigation(str, Enum):
    NONE = "NONE"
    SUBSTATION_TERMINAL = "SUBSTATION_TERMINAL"
    SIGNAL_ZONE = "SIGNAL_ZONE"

    def __str__(self) -> str:
        return str(self.value)
