from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Coordinate")


@attr.s(auto_attribs=True)
class Coordinate:
    """
    Attributes:
        x (Union[Unset, float]):
        y (Union[Unset, float]):
        z (Union[Unset, float]):
        m (Union[Unset, float]):
        coordinate_value (Union[Unset, Coordinate]):
    """

    x: Union[Unset, float] = UNSET
    y: Union[Unset, float] = UNSET
    z: Union[Unset, float] = UNSET
    m: Union[Unset, float] = UNSET
    coordinate_value: Union[Unset, "Coordinate"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        x = self.x
        y = self.y
        z = self.z
        m = self.m
        coordinate_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.coordinate_value, Unset):
            coordinate_value = self.coordinate_value.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y
        if z is not UNSET:
            field_dict["z"] = z
        if m is not UNSET:
            field_dict["m"] = m
        if coordinate_value is not UNSET:
            field_dict["coordinateValue"] = coordinate_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        x = d.pop("x", UNSET)

        y = d.pop("y", UNSET)

        z = d.pop("z", UNSET)

        m = d.pop("m", UNSET)

        _coordinate_value = d.pop("coordinateValue", UNSET)
        coordinate_value: Union[Unset, Coordinate]
        if isinstance(_coordinate_value, Unset):
            coordinate_value = UNSET
        else:
            coordinate_value = Coordinate.from_dict(_coordinate_value)

        coordinate = cls(
            x=x,
            y=y,
            z=z,
            m=m,
            coordinate_value=coordinate_value,
        )

        return coordinate
