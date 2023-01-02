from typing import Any, Dict, Type, TypeVar, Union

import attr

from .._types import UNSET, Unset

T = TypeVar("T", bound="League")


@attr.s(auto_attribs=True)
class League:
    """
    Attributes:
        region (Union[Unset, None, str]):
        code (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        parent_league_code (Union[Unset, None, str]):
        location (Union[Unset, None, str]):
    """

    region: Union[Unset, None, str] = UNSET
    code: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    parent_league_code: Union[Unset, None, str] = UNSET
    location: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        region = self.region
        code = self.code
        name = self.name
        parent_league_code = self.parent_league_code
        location = self.location

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if region is not UNSET:
            field_dict["region"] = region
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name
        if parent_league_code is not UNSET:
            field_dict["parentLeagueCode"] = parent_league_code
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        region = d.pop("region", UNSET)

        code = d.pop("code", UNSET)

        name = d.pop("name", UNSET)

        parent_league_code = d.pop("parentLeagueCode", UNSET)

        location = d.pop("location", UNSET)

        league = cls(
            region=region,
            code=code,
            name=name,
            parent_league_code=parent_league_code,
            location=location,
        )

        return league
