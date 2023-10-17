from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coordinate_equality_comparer import CoordinateEqualityComparer
    from ..models.coordinate_sequence_factory import CoordinateSequenceFactory
    from ..models.geometry_overlay import GeometryOverlay
    from ..models.precision_model import PrecisionModel


T = TypeVar("T", bound="NtsGeometryServices")


@_attrs_define
class NtsGeometryServices:
    """
    Attributes:
        geometry_overlay (Union[Unset, GeometryOverlay]):
        coordinate_equality_comparer (Union[Unset, CoordinateEqualityComparer]):
        default_srid (Union[Unset, int]):
        default_coordinate_sequence_factory (Union[Unset, CoordinateSequenceFactory]):
        default_precision_model (Union[Unset, PrecisionModel]):
    """

    geometry_overlay: Union[Unset, "GeometryOverlay"] = UNSET
    coordinate_equality_comparer: Union[Unset, "CoordinateEqualityComparer"] = UNSET
    default_srid: Union[Unset, int] = UNSET
    default_coordinate_sequence_factory: Union[Unset, "CoordinateSequenceFactory"] = UNSET
    default_precision_model: Union[Unset, "PrecisionModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        geometry_overlay: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.geometry_overlay, Unset):
            geometry_overlay = self.geometry_overlay.to_dict()

        coordinate_equality_comparer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.coordinate_equality_comparer, Unset):
            coordinate_equality_comparer = self.coordinate_equality_comparer.to_dict()

        default_srid = self.default_srid
        default_coordinate_sequence_factory: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.default_coordinate_sequence_factory, Unset):
            default_coordinate_sequence_factory = self.default_coordinate_sequence_factory.to_dict()

        default_precision_model: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.default_precision_model, Unset):
            default_precision_model = self.default_precision_model.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if geometry_overlay is not UNSET:
            field_dict["geometryOverlay"] = geometry_overlay
        if coordinate_equality_comparer is not UNSET:
            field_dict["coordinateEqualityComparer"] = coordinate_equality_comparer
        if default_srid is not UNSET:
            field_dict["defaultSRID"] = default_srid
        if default_coordinate_sequence_factory is not UNSET:
            field_dict["defaultCoordinateSequenceFactory"] = default_coordinate_sequence_factory
        if default_precision_model is not UNSET:
            field_dict["defaultPrecisionModel"] = default_precision_model

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.coordinate_equality_comparer import CoordinateEqualityComparer
        from ..models.coordinate_sequence_factory import CoordinateSequenceFactory
        from ..models.geometry_overlay import GeometryOverlay
        from ..models.precision_model import PrecisionModel

        d = src_dict.copy()
        _geometry_overlay = d.pop("geometryOverlay", UNSET)
        geometry_overlay: Union[Unset, GeometryOverlay]
        if isinstance(_geometry_overlay, Unset):
            geometry_overlay = UNSET
        else:
            geometry_overlay = GeometryOverlay.from_dict(_geometry_overlay)

        _coordinate_equality_comparer = d.pop("coordinateEqualityComparer", UNSET)
        coordinate_equality_comparer: Union[Unset, CoordinateEqualityComparer]
        if isinstance(_coordinate_equality_comparer, Unset):
            coordinate_equality_comparer = UNSET
        else:
            coordinate_equality_comparer = CoordinateEqualityComparer.from_dict(_coordinate_equality_comparer)

        default_srid = d.pop("defaultSRID", UNSET)

        _default_coordinate_sequence_factory = d.pop("defaultCoordinateSequenceFactory", UNSET)
        default_coordinate_sequence_factory: Union[Unset, CoordinateSequenceFactory]
        if isinstance(_default_coordinate_sequence_factory, Unset):
            default_coordinate_sequence_factory = UNSET
        else:
            default_coordinate_sequence_factory = CoordinateSequenceFactory.from_dict(
                _default_coordinate_sequence_factory
            )

        _default_precision_model = d.pop("defaultPrecisionModel", UNSET)
        default_precision_model: Union[Unset, PrecisionModel]
        if isinstance(_default_precision_model, Unset):
            default_precision_model = UNSET
        else:
            default_precision_model = PrecisionModel.from_dict(_default_precision_model)

        nts_geometry_services = cls(
            geometry_overlay=geometry_overlay,
            coordinate_equality_comparer=coordinate_equality_comparer,
            default_srid=default_srid,
            default_coordinate_sequence_factory=default_coordinate_sequence_factory,
            default_precision_model=default_precision_model,
        )

        return nts_geometry_services
