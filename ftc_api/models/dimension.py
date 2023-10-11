from enum import Enum


class Dimension(str, Enum):
    P = "P"
    CURVE = "Curve"
    A = "A"
    COLLAPSE = "Collapse"
    DONTCARE = "Dontcare"
    TRUE = "True"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
