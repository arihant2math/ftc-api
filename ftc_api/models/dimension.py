from enum import Enum


class Dimension(str, Enum):
    A = "A"
    COLLAPSE = "Collapse"
    CURVE = "Curve"
    DONTCARE = "Dontcare"
    P = "P"
    TRUE = "True"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
