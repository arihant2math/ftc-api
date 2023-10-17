from enum import Enum


class JunctionElement(str, Enum):
    MY_CONE = "MY_CONE"
    MY_R1_BEACON = "MY_R1_BEACON"
    MY_R2_BEACON = "MY_R2_BEACON"
    OTHER_CONE = "OTHER_CONE"
    OTHER_R1_BEACON = "OTHER_R1_BEACON"
    OTHER_R2_BEACON = "OTHER_R2_BEACON"

    def __str__(self) -> str:
        return str(self.value)
