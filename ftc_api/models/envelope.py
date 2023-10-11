from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coordinate import Coordinate


T = TypeVar("T", bound="Envelope")


@attr.s(auto_attribs=True)
class Envelope:
    """
    Attributes:
        is_null (Union[Unset, bool]):
        width (Union[Unset, float]):
        height (Union[Unset, float]):
        diameter (Union[Unset, float]):
        min_x (Union[Unset, float]):
        max_x (Union[Unset, float]):
        min_y (Union[Unset, float]):
        max_y (Union[Unset, float]):
        area (Union[Unset, float]):
        min_extent (Union[Unset, float]):
        max_extent (Union[Unset, float]):
        centre (Union[Unset, Coordinate]):
    """

    is_null: Union[Unset, bool] = UNSET
    width: Union[Unset, float] = UNSET
    height: Union[Unset, float] = UNSET
    diameter: Union[Unset, float] = UNSET
    min_x: Union[Unset, float] = UNSET
    max_x: Union[Unset, float] = UNSET
    min_y: Union[Unset, float] = UNSET
    max_y: Union[Unset, float] = UNSET
    area: Union[Unset, float] = UNSET
    min_extent: Union[Unset, float] = UNSET
    max_extent: Union[Unset, float] = UNSET
    centre: Union[Unset, "Coordinate"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        is_null = self.is_null
        width = self.width
        height = self.height
        diameter = self.diameter
        min_x = self.min_x
        max_x = self.max_x
        min_y = self.min_y
        max_y = self.max_y
        area = self.area
        min_extent = self.min_extent
        max_extent = self.max_extent
        centre: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.centre, Unset):
            centre = self.centre.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if is_null is not UNSET:
            field_dict["isNull"] = is_null
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if diameter is not UNSET:
            field_dict["diameter"] = diameter
        if min_x is not UNSET:
            field_dict["minX"] = min_x
        if max_x is not UNSET:
            field_dict["maxX"] = max_x
        if min_y is not UNSET:
            field_dict["minY"] = min_y
        if max_y is not UNSET:
            field_dict["maxY"] = max_y
        if area is not UNSET:
            field_dict["area"] = area
        if min_extent is not UNSET:
            field_dict["minExtent"] = min_extent
        if max_extent is not UNSET:
            field_dict["maxExtent"] = max_extent
        if centre is not UNSET:
            field_dict["centre"] = centre

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.coordinate import Coordinate

        d = src_dict.copy()
        is_null = d.pop("isNull", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        diameter = d.pop("diameter", UNSET)

        min_x = d.pop("minX", UNSET)

        max_x = d.pop("maxX", UNSET)

        min_y = d.pop("minY", UNSET)

        max_y = d.pop("maxY", UNSET)

        area = d.pop("area", UNSET)

        min_extent = d.pop("minExtent", UNSET)

        max_extent = d.pop("maxExtent", UNSET)

        _centre = d.pop("centre", UNSET)
        centre: Union[Unset, Coordinate]
        if isinstance(_centre, Unset):
            centre = UNSET
        else:
            centre = Coordinate.from_dict(_centre)

        envelope = cls(
            is_null=is_null,
            width=width,
            height=height,
            diameter=diameter,
            min_x=min_x,
            max_x=max_x,
            min_y=min_y,
            max_y=max_y,
            area=area,
            min_extent=min_extent,
            max_extent=max_extent,
            centre=centre,
        )

        return envelope
