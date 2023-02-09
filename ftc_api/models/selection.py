from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.selection_result import SelectionResult
from ..types import UNSET, Unset

T = TypeVar("T", bound="Selection")


@attr.s(auto_attribs=True)
class Selection:
    """
    Attributes:
        index (Union[Unset, int]):
        team (Union[Unset, int]):
        result (Union[Unset, SelectionResult]):
    """

    index: Union[Unset, int] = UNSET
    team: Union[Unset, int] = UNSET
    result: Union[Unset, SelectionResult] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        index = self.index
        team = self.team
        result: Union[Unset, str] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if index is not UNSET:
            field_dict["index"] = index
        if team is not UNSET:
            field_dict["team"] = team
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        index = d.pop("index", UNSET)

        team = d.pop("team", UNSET)

        _result = d.pop("result", UNSET)
        result: Union[Unset, SelectionResult]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = SelectionResult(_result)

        selection = cls(
            index=index,
            team=team,
            result=result,
        )

        return selection
