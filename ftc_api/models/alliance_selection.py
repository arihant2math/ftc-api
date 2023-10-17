from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alliance import Alliance


T = TypeVar("T", bound="AllianceSelection")


@_attrs_define
class AllianceSelection:
    """
    Attributes:
        alliances (Union[Unset, None, List['Alliance']]):
        count (Union[Unset, int]):
    """

    alliances: Union[Unset, None, List["Alliance"]] = UNSET
    count: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        alliances: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.alliances, Unset):
            if self.alliances is None:
                alliances = None
            else:
                alliances = []
                for alliances_item_data in self.alliances:
                    alliances_item = alliances_item_data.to_dict()

                    alliances.append(alliances_item)

        count = self.count

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if alliances is not UNSET:
            field_dict["alliances"] = alliances
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.alliance import Alliance

        d = src_dict.copy()
        alliances = []
        _alliances = d.pop("alliances", UNSET)
        for alliances_item_data in _alliances or []:
            alliances_item = Alliance.from_dict(alliances_item_data)

            alliances.append(alliances_item)

        count = d.pop("count", UNSET)

        alliance_selection = cls(
            alliances=alliances,
            count=count,
        )

        return alliance_selection
