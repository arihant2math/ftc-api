from enum import Enum


class BarcodeElement(str, Enum):
    DUCK = "DUCK"
    TEAM_SHIPPING_ELEMENT = "TEAM_SHIPPING_ELEMENT"

    def __str__(self) -> str:
        return str(self.value)
