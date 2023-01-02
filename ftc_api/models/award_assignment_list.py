from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from .._types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.award_assignment import AwardAssignment


T = TypeVar("T", bound="AwardAssignmentList")


@attr.s(auto_attribs=True)
class AwardAssignmentList:
    """
    Attributes:
        awards (Union[Unset, None, List['AwardAssignment']]):
    """

    awards: Union[Unset, None, List["AwardAssignment"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        awards: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.awards, Unset):
            if self.awards is None:
                awards = None
            else:
                awards = []
                for awards_item_data in self.awards:
                    awards_item = awards_item_data.to_dict()

                    awards.append(awards_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if awards is not UNSET:
            field_dict["awards"] = awards

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.award_assignment import AwardAssignment

        d = src_dict.copy()
        awards = []
        _awards = d.pop("awards", UNSET)
        for awards_item_data in _awards or []:
            awards_item = AwardAssignment.from_dict(awards_item_data)

            awards.append(awards_item)

        award_assignment_list = cls(
            awards=awards,
        )

        return award_assignment_list
