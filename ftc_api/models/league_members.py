from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ftc_api.types import UNSET, Unset

T = TypeVar("T", bound="LeagueMembers")


@attr.s(auto_attribs=True)
class LeagueMembers:
    """
    Attributes:
        members (Union[Unset, None, List[int]]):
    """

    members: Union[Unset, None, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        members: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.members, Unset):
            if self.members is None:
                members = None
            else:
                members = self.members

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if members is not UNSET:
            field_dict["members"] = members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        members = cast(List[int], d.pop("members", UNSET))

        league_members = cls(
            members=members,
        )

        return league_members
