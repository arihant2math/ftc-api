from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.selection import Selection


T = TypeVar("T", bound="AllianceSelectionDetails")


@attr.s(auto_attribs=True)
class AllianceSelectionDetails:
    """
    Attributes:
        selections (Union[Unset, None, List['Selection']]):
        count (Union[Unset, int]):
    """

    selections: Union[Unset, None, List["Selection"]] = UNSET
    count: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        selections: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.selections, Unset):
            if self.selections is None:
                selections = None
            else:
                selections = []
                for selections_item_data in self.selections:
                    selections_item = selections_item_data.to_dict()

                    selections.append(selections_item)

        count = self.count

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if selections is not UNSET:
            field_dict["selections"] = selections
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.selection import Selection

        d = src_dict.copy()
        selections = []
        _selections = d.pop("selections", UNSET)
        for selections_item_data in _selections or []:
            selections_item = Selection.from_dict(selections_item_data)

            selections.append(selections_item)

        count = d.pop("count", UNSET)

        alliance_selection_details = cls(
            selections=selections,
            count=count,
        )

        return alliance_selection_details
