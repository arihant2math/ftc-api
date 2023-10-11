from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.ordinates import Ordinates
from ..types import UNSET, Unset

T = TypeVar("T", bound="CoordinateSequence")


@attr.s(auto_attribs=True)
class CoordinateSequence:
    """
    Attributes:
        dimension (Union[Unset, int]):
        measures (Union[Unset, int]):
        spatial (Union[Unset, int]):
        ordinates (Union[Unset, Ordinates]):
        has_z (Union[Unset, bool]):
        has_m (Union[Unset, bool]):
        z_ordinate_index (Union[Unset, int]):
        m_ordinate_index (Union[Unset, int]):
        count (Union[Unset, int]):
    """

    dimension: Union[Unset, int] = UNSET
    measures: Union[Unset, int] = UNSET
    spatial: Union[Unset, int] = UNSET
    ordinates: Union[Unset, Ordinates] = UNSET
    has_z: Union[Unset, bool] = UNSET
    has_m: Union[Unset, bool] = UNSET
    z_ordinate_index: Union[Unset, int] = UNSET
    m_ordinate_index: Union[Unset, int] = UNSET
    count: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        dimension = self.dimension
        measures = self.measures
        spatial = self.spatial
        ordinates: Union[Unset, str] = UNSET
        if not isinstance(self.ordinates, Unset):
            ordinates = self.ordinates.value

        has_z = self.has_z
        has_m = self.has_m
        z_ordinate_index = self.z_ordinate_index
        m_ordinate_index = self.m_ordinate_index
        count = self.count

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if dimension is not UNSET:
            field_dict["dimension"] = dimension
        if measures is not UNSET:
            field_dict["measures"] = measures
        if spatial is not UNSET:
            field_dict["spatial"] = spatial
        if ordinates is not UNSET:
            field_dict["ordinates"] = ordinates
        if has_z is not UNSET:
            field_dict["hasZ"] = has_z
        if has_m is not UNSET:
            field_dict["hasM"] = has_m
        if z_ordinate_index is not UNSET:
            field_dict["zOrdinateIndex"] = z_ordinate_index
        if m_ordinate_index is not UNSET:
            field_dict["mOrdinateIndex"] = m_ordinate_index
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dimension = d.pop("dimension", UNSET)

        measures = d.pop("measures", UNSET)

        spatial = d.pop("spatial", UNSET)

        _ordinates = d.pop("ordinates", UNSET)
        ordinates: Union[Unset, Ordinates]
        if isinstance(_ordinates, Unset):
            ordinates = UNSET
        else:
            ordinates = Ordinates(_ordinates)

        has_z = d.pop("hasZ", UNSET)

        has_m = d.pop("hasM", UNSET)

        z_ordinate_index = d.pop("zOrdinateIndex", UNSET)

        m_ordinate_index = d.pop("mOrdinateIndex", UNSET)

        count = d.pop("count", UNSET)

        coordinate_sequence = cls(
            dimension=dimension,
            measures=measures,
            spatial=spatial,
            ordinates=ordinates,
            has_z=has_z,
            has_m=has_m,
            z_ordinate_index=z_ordinate_index,
            m_ordinate_index=m_ordinate_index,
            count=count,
        )

        return coordinate_sequence
