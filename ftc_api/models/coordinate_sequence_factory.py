from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.ordinates import Ordinates
from ..types import UNSET, Unset

T = TypeVar("T", bound="CoordinateSequenceFactory")


@_attrs_define
class CoordinateSequenceFactory:
    """
    Attributes:
        ordinates (Union[Unset, Ordinates]):
    """

    ordinates: Union[Unset, Ordinates] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        ordinates: Union[Unset, str] = UNSET
        if not isinstance(self.ordinates, Unset):
            ordinates = self.ordinates.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if ordinates is not UNSET:
            field_dict["ordinates"] = ordinates

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _ordinates = d.pop("ordinates", UNSET)
        ordinates: Union[Unset, Ordinates]
        if isinstance(_ordinates, Unset):
            ordinates = UNSET
        else:
            ordinates = Ordinates(_ordinates)

        coordinate_sequence_factory = cls(
            ordinates=ordinates,
        )

        return coordinate_sequence_factory
