from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from .._types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.match_result import MatchResult


T = TypeVar("T", bound="MatchResultList")


@attr.s(auto_attribs=True)
class MatchResultList:
    """
    Attributes:
        matches (Union[Unset, None, List['MatchResult']]):
    """

    matches: Union[Unset, None, List["MatchResult"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        matches: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.matches, Unset):
            if self.matches is None:
                matches = None
            else:
                matches = []
                for matches_item_data in self.matches:
                    matches_item = matches_item_data.to_dict()

                    matches.append(matches_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if matches is not UNSET:
            field_dict["matches"] = matches

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.match_result import MatchResult

        d = src_dict.copy()
        matches = []
        _matches = d.pop("matches", UNSET)
        for matches_item_data in _matches or []:
            matches_item = MatchResult.from_dict(matches_item_data)

            matches.append(matches_item)

        match_result_list = cls(
            matches=matches,
        )

        return match_result_list
