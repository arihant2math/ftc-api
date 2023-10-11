from enum import Enum


class OgcGeometryType(str, Enum):
    POINT = "Point"
    LINESTRING = "LineString"
    POLYGON = "Polygon"
    MULTIPOINT = "MultiPoint"
    MULTILINESTRING = "MultiLineString"
    MULTIPOLYGON = "MultiPolygon"
    GEOMETRYCOLLECTION = "GeometryCollection"
    CIRCULARSTRING = "CircularString"
    COMPOUNDCURVE = "CompoundCurve"
    CURVEPOLYGON = "CurvePolygon"
    MULTICURVE = "MultiCurve"
    MULTISURFACE = "MultiSurface"
    CURVE = "Curve"
    SURFACE = "Surface"
    POLYHEDRALSURFACE = "PolyhedralSurface"
    TIN = "TIN"

    def __str__(self) -> str:
        return str(self.value)
