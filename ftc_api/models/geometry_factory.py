from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coordinate_sequence_factory import CoordinateSequenceFactory
    from ..models.nts_geometry_services import NtsGeometryServices
    from ..models.precision_model import PrecisionModel


T = TypeVar("T", bound="GeometryFactory")


@_attrs_define
class GeometryFactory:
    """
    Attributes:
        precision_model (Union[Unset, PrecisionModel]):
        coordinate_sequence_factory (Union[Unset, CoordinateSequenceFactory]):
        srid (Union[Unset, int]):
        geometry_services (Union[Unset, NtsGeometryServices]):
    """

    precision_model: Union[Unset, "PrecisionModel"] = UNSET
    coordinate_sequence_factory: Union[Unset, "CoordinateSequenceFactory"] = UNSET
    srid: Union[Unset, int] = UNSET
    geometry_services: Union[Unset, "NtsGeometryServices"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        precision_model: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.precision_model, Unset):
            precision_model = self.precision_model.to_dict()

        coordinate_sequence_factory: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.coordinate_sequence_factory, Unset):
            coordinate_sequence_factory = self.coordinate_sequence_factory.to_dict()

        srid = self.srid
        geometry_services: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.geometry_services, Unset):
            geometry_services = self.geometry_services.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if precision_model is not UNSET:
            field_dict["precisionModel"] = precision_model
        if coordinate_sequence_factory is not UNSET:
            field_dict["coordinateSequenceFactory"] = coordinate_sequence_factory
        if srid is not UNSET:
            field_dict["srid"] = srid
        if geometry_services is not UNSET:
            field_dict["geometryServices"] = geometry_services

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.coordinate_sequence_factory import CoordinateSequenceFactory
        from ..models.nts_geometry_services import NtsGeometryServices
        from ..models.precision_model import PrecisionModel

        d = src_dict.copy()
        _precision_model = d.pop("precisionModel", UNSET)
        precision_model: Union[Unset, PrecisionModel]
        if isinstance(_precision_model, Unset):
            precision_model = UNSET
        else:
            precision_model = PrecisionModel.from_dict(_precision_model)

        _coordinate_sequence_factory = d.pop("coordinateSequenceFactory", UNSET)
        coordinate_sequence_factory: Union[Unset, CoordinateSequenceFactory]
        if isinstance(_coordinate_sequence_factory, Unset):
            coordinate_sequence_factory = UNSET
        else:
            coordinate_sequence_factory = CoordinateSequenceFactory.from_dict(_coordinate_sequence_factory)

        srid = d.pop("srid", UNSET)

        _geometry_services = d.pop("geometryServices", UNSET)
        geometry_services: Union[Unset, NtsGeometryServices]
        if isinstance(_geometry_services, Unset):
            geometry_services = UNSET
        else:
            geometry_services = NtsGeometryServices.from_dict(_geometry_services)

        geometry_factory = cls(
            precision_model=precision_model,
            coordinate_sequence_factory=coordinate_sequence_factory,
            srid=srid,
            geometry_services=geometry_services,
        )

        return geometry_factory
