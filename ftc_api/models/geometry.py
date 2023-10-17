from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.dimension import Dimension
from ..models.ogc_geometry_type import OgcGeometryType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coordinate import Coordinate
    from ..models.envelope import Envelope
    from ..models.geometry_factory import GeometryFactory
    from ..models.point import Point
    from ..models.precision_model import PrecisionModel


T = TypeVar("T", bound="Geometry")


@_attrs_define
class Geometry:
    """
    Attributes:
        coordinates (Union[Unset, None, List['Coordinate']]):
        num_points (Union[Unset, int]):
        is_empty (Union[Unset, bool]):
        dimension (Union[Unset, Dimension]):
        boundary_dimension (Union[Unset, Dimension]):
        coordinate (Union[Unset, Coordinate]):
        geometry_type (Union[Unset, None, str]):
        ogc_geometry_type (Union[Unset, OgcGeometryType]):
        boundary (Union[Unset, Geometry]):
        factory (Union[Unset, GeometryFactory]):
        user_data (Union[Unset, Any]):
        srid (Union[Unset, int]):
        precision_model (Union[Unset, PrecisionModel]):
        num_geometries (Union[Unset, int]):
        is_simple (Union[Unset, bool]):
        is_valid (Union[Unset, bool]):
        area (Union[Unset, float]):
        length (Union[Unset, float]):
        centroid (Union[Unset, Point]):
        interior_point (Union[Unset, Point]):
        point_on_surface (Union[Unset, Point]):
        envelope (Union[Unset, Geometry]):
        envelope_internal (Union[Unset, Envelope]):
        is_rectangle (Union[Unset, bool]):
    """

    coordinates: Union[Unset, None, List["Coordinate"]] = UNSET
    num_points: Union[Unset, int] = UNSET
    is_empty: Union[Unset, bool] = UNSET
    dimension: Union[Unset, Dimension] = UNSET
    boundary_dimension: Union[Unset, Dimension] = UNSET
    coordinate: Union[Unset, "Coordinate"] = UNSET
    geometry_type: Union[Unset, None, str] = UNSET
    ogc_geometry_type: Union[Unset, OgcGeometryType] = UNSET
    boundary: Union[Unset, "Geometry"] = UNSET
    factory: Union[Unset, "GeometryFactory"] = UNSET
    user_data: Union[Unset, Any] = UNSET
    srid: Union[Unset, int] = UNSET
    precision_model: Union[Unset, "PrecisionModel"] = UNSET
    num_geometries: Union[Unset, int] = UNSET
    is_simple: Union[Unset, bool] = UNSET
    is_valid: Union[Unset, bool] = UNSET
    area: Union[Unset, float] = UNSET
    length: Union[Unset, float] = UNSET
    centroid: Union[Unset, "Point"] = UNSET
    interior_point: Union[Unset, "Point"] = UNSET
    point_on_surface: Union[Unset, "Point"] = UNSET
    envelope: Union[Unset, "Geometry"] = UNSET
    envelope_internal: Union[Unset, "Envelope"] = UNSET
    is_rectangle: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        coordinates: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.coordinates, Unset):
            if self.coordinates is None:
                coordinates = None
            else:
                coordinates = []
                for coordinates_item_data in self.coordinates:
                    coordinates_item = coordinates_item_data.to_dict()

                    coordinates.append(coordinates_item)

        num_points = self.num_points
        is_empty = self.is_empty
        dimension: Union[Unset, str] = UNSET
        if not isinstance(self.dimension, Unset):
            dimension = self.dimension.value

        boundary_dimension: Union[Unset, str] = UNSET
        if not isinstance(self.boundary_dimension, Unset):
            boundary_dimension = self.boundary_dimension.value

        coordinate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.coordinate, Unset):
            coordinate = self.coordinate.to_dict()

        geometry_type = self.geometry_type
        ogc_geometry_type: Union[Unset, str] = UNSET
        if not isinstance(self.ogc_geometry_type, Unset):
            ogc_geometry_type = self.ogc_geometry_type.value

        boundary: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.boundary, Unset):
            boundary = self.boundary.to_dict()

        factory: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.factory, Unset):
            factory = self.factory.to_dict()

        user_data = self.user_data
        srid = self.srid
        precision_model: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.precision_model, Unset):
            precision_model = self.precision_model.to_dict()

        num_geometries = self.num_geometries
        is_simple = self.is_simple
        is_valid = self.is_valid
        area = self.area
        length = self.length
        centroid: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.centroid, Unset):
            centroid = self.centroid.to_dict()

        interior_point: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.interior_point, Unset):
            interior_point = self.interior_point.to_dict()

        point_on_surface: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.point_on_surface, Unset):
            point_on_surface = self.point_on_surface.to_dict()

        envelope: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.envelope, Unset):
            envelope = self.envelope.to_dict()

        envelope_internal: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.envelope_internal, Unset):
            envelope_internal = self.envelope_internal.to_dict()

        is_rectangle = self.is_rectangle

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if coordinates is not UNSET:
            field_dict["coordinates"] = coordinates
        if num_points is not UNSET:
            field_dict["numPoints"] = num_points
        if is_empty is not UNSET:
            field_dict["isEmpty"] = is_empty
        if dimension is not UNSET:
            field_dict["dimension"] = dimension
        if boundary_dimension is not UNSET:
            field_dict["boundaryDimension"] = boundary_dimension
        if coordinate is not UNSET:
            field_dict["coordinate"] = coordinate
        if geometry_type is not UNSET:
            field_dict["geometryType"] = geometry_type
        if ogc_geometry_type is not UNSET:
            field_dict["ogcGeometryType"] = ogc_geometry_type
        if boundary is not UNSET:
            field_dict["boundary"] = boundary
        if factory is not UNSET:
            field_dict["factory"] = factory
        if user_data is not UNSET:
            field_dict["userData"] = user_data
        if srid is not UNSET:
            field_dict["srid"] = srid
        if precision_model is not UNSET:
            field_dict["precisionModel"] = precision_model
        if num_geometries is not UNSET:
            field_dict["numGeometries"] = num_geometries
        if is_simple is not UNSET:
            field_dict["isSimple"] = is_simple
        if is_valid is not UNSET:
            field_dict["isValid"] = is_valid
        if area is not UNSET:
            field_dict["area"] = area
        if length is not UNSET:
            field_dict["length"] = length
        if centroid is not UNSET:
            field_dict["centroid"] = centroid
        if interior_point is not UNSET:
            field_dict["interiorPoint"] = interior_point
        if point_on_surface is not UNSET:
            field_dict["pointOnSurface"] = point_on_surface
        if envelope is not UNSET:
            field_dict["envelope"] = envelope
        if envelope_internal is not UNSET:
            field_dict["envelopeInternal"] = envelope_internal
        if is_rectangle is not UNSET:
            field_dict["isRectangle"] = is_rectangle

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.coordinate import Coordinate
        from ..models.envelope import Envelope
        from ..models.geometry_factory import GeometryFactory
        from ..models.point import Point
        from ..models.precision_model import PrecisionModel

        d = src_dict.copy()
        coordinates = []
        _coordinates = d.pop("coordinates", UNSET)
        for coordinates_item_data in _coordinates or []:
            coordinates_item = Coordinate.from_dict(coordinates_item_data)

            coordinates.append(coordinates_item)

        num_points = d.pop("numPoints", UNSET)

        is_empty = d.pop("isEmpty", UNSET)

        _dimension = d.pop("dimension", UNSET)
        dimension: Union[Unset, Dimension]
        if isinstance(_dimension, Unset):
            dimension = UNSET
        else:
            dimension = Dimension(_dimension)

        _boundary_dimension = d.pop("boundaryDimension", UNSET)
        boundary_dimension: Union[Unset, Dimension]
        if isinstance(_boundary_dimension, Unset):
            boundary_dimension = UNSET
        else:
            boundary_dimension = Dimension(_boundary_dimension)

        _coordinate = d.pop("coordinate", UNSET)
        coordinate: Union[Unset, Coordinate]
        if isinstance(_coordinate, Unset):
            coordinate = UNSET
        else:
            coordinate = Coordinate.from_dict(_coordinate)

        geometry_type = d.pop("geometryType", UNSET)

        _ogc_geometry_type = d.pop("ogcGeometryType", UNSET)
        ogc_geometry_type: Union[Unset, OgcGeometryType]
        if isinstance(_ogc_geometry_type, Unset):
            ogc_geometry_type = UNSET
        else:
            ogc_geometry_type = OgcGeometryType(_ogc_geometry_type)

        _boundary = d.pop("boundary", UNSET)
        boundary: Union[Unset, Geometry]
        if isinstance(_boundary, Unset):
            boundary = UNSET
        else:
            boundary = Geometry.from_dict(_boundary)

        _factory = d.pop("factory", UNSET)
        factory: Union[Unset, GeometryFactory]
        if isinstance(_factory, Unset):
            factory = UNSET
        else:
            factory = GeometryFactory.from_dict(_factory)

        user_data = d.pop("userData", UNSET)

        srid = d.pop("srid", UNSET)

        _precision_model = d.pop("precisionModel", UNSET)
        precision_model: Union[Unset, PrecisionModel]
        if isinstance(_precision_model, Unset):
            precision_model = UNSET
        else:
            precision_model = PrecisionModel.from_dict(_precision_model)

        num_geometries = d.pop("numGeometries", UNSET)

        is_simple = d.pop("isSimple", UNSET)

        is_valid = d.pop("isValid", UNSET)

        area = d.pop("area", UNSET)

        length = d.pop("length", UNSET)

        _centroid = d.pop("centroid", UNSET)
        centroid: Union[Unset, Point]
        if isinstance(_centroid, Unset):
            centroid = UNSET
        else:
            centroid = Point.from_dict(_centroid)

        _interior_point = d.pop("interiorPoint", UNSET)
        interior_point: Union[Unset, Point]
        if isinstance(_interior_point, Unset):
            interior_point = UNSET
        else:
            interior_point = Point.from_dict(_interior_point)

        _point_on_surface = d.pop("pointOnSurface", UNSET)
        point_on_surface: Union[Unset, Point]
        if isinstance(_point_on_surface, Unset):
            point_on_surface = UNSET
        else:
            point_on_surface = Point.from_dict(_point_on_surface)

        _envelope = d.pop("envelope", UNSET)
        envelope: Union[Unset, Geometry]
        if isinstance(_envelope, Unset):
            envelope = UNSET
        else:
            envelope = Geometry.from_dict(_envelope)

        _envelope_internal = d.pop("envelopeInternal", UNSET)
        envelope_internal: Union[Unset, Envelope]
        if isinstance(_envelope_internal, Unset):
            envelope_internal = UNSET
        else:
            envelope_internal = Envelope.from_dict(_envelope_internal)

        is_rectangle = d.pop("isRectangle", UNSET)

        geometry = cls(
            coordinates=coordinates,
            num_points=num_points,
            is_empty=is_empty,
            dimension=dimension,
            boundary_dimension=boundary_dimension,
            coordinate=coordinate,
            geometry_type=geometry_type,
            ogc_geometry_type=ogc_geometry_type,
            boundary=boundary,
            factory=factory,
            user_data=user_data,
            srid=srid,
            precision_model=precision_model,
            num_geometries=num_geometries,
            is_simple=is_simple,
            is_valid=is_valid,
            area=area,
            length=length,
            centroid=centroid,
            interior_point=interior_point,
            point_on_surface=point_on_surface,
            envelope=envelope,
            envelope_internal=envelope_internal,
            is_rectangle=is_rectangle,
        )

        return geometry
