from enum import Enum


class OgcGeometryType(str, Enum):
    CIRCULARSTRING = "CircularString"
    COMPOUNDCURVE = "CompoundCurve"
    CURVE = "Curve"
    CURVEPOLYGON = "CurvePolygon"
    GEOMETRYCOLLECTION = "GeometryCollection"
    LINESTRING = "LineString"
    MULTICURVE = "MultiCurve"
    MULTILINESTRING = "MultiLineString"
    MULTIPOINT = "MultiPoint"
    MULTIPOLYGON = "MultiPolygon"
    MULTISURFACE = "MultiSurface"
    POINT = "Point"
    POLYGON = "Polygon"
    POLYHEDRALSURFACE = "PolyhedralSurface"
    SURFACE = "Surface"
    TIN = "TIN"

    def __str__(self) -> str:
        return str(self.value)
