from enum import Enum


class Ordinates(str, Enum):
    ALLMEASUREORDINATES = "AllMeasureOrdinates"
    ALLORDINATES = "AllOrdinates"
    ALLSPATIALORDINATES = "AllSpatialOrdinates"
    MEASURE1 = "Measure1"
    MEASURE10 = "Measure10"
    MEASURE11 = "Measure11"
    MEASURE12 = "Measure12"
    MEASURE13 = "Measure13"
    MEASURE14 = "Measure14"
    MEASURE15 = "Measure15"
    MEASURE16 = "Measure16"
    MEASURE2 = "Measure2"
    MEASURE3 = "Measure3"
    MEASURE4 = "Measure4"
    MEASURE5 = "Measure5"
    MEASURE6 = "Measure6"
    MEASURE7 = "Measure7"
    MEASURE8 = "Measure8"
    MEASURE9 = "Measure9"
    NONE = "None"
    SPATIAL10 = "Spatial10"
    SPATIAL11 = "Spatial11"
    SPATIAL12 = "Spatial12"
    SPATIAL13 = "Spatial13"
    SPATIAL14 = "Spatial14"
    SPATIAL15 = "Spatial15"
    SPATIAL16 = "Spatial16"
    SPATIAL3 = "Spatial3"
    SPATIAL4 = "Spatial4"
    SPATIAL5 = "Spatial5"
    SPATIAL6 = "Spatial6"
    SPATIAL7 = "Spatial7"
    SPATIAL8 = "Spatial8"
    SPATIAL9 = "Spatial9"
    X = "X"
    XY = "XY"
    XYM = "XYM"
    XYZ = "XYZ"
    XYZM = "XYZM"
    Y = "Y"

    def __str__(self) -> str:
        return str(self.value)