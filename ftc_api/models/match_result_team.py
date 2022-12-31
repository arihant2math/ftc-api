from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchResultTeam")


@attr.s(auto_attribs=True)
class MatchResultTeam:
    """
    Attributes:
        team_number (Union[Unset, int]):
        station (Union[Unset, None, str]):
        dq (Union[Unset, bool]):
        on_field (Union[Unset, bool]):
    """

    team_number: Union[Unset, int] = UNSET
    station: Union[Unset, None, str] = UNSET
    dq: Union[Unset, bool] = UNSET
    on_field: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        team_number = self.team_number
        station = self.station
        dq = self.dq
        on_field = self.on_field

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if team_number is not UNSET:
            field_dict["teamNumber"] = team_number
        if station is not UNSET:
            field_dict["station"] = station
        if dq is not UNSET:
            field_dict["dq"] = dq
        if on_field is not UNSET:
            field_dict["onField"] = on_field

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        team_number = d.pop("teamNumber", UNSET)

        station = d.pop("station", UNSET)

        dq = d.pop("dq", UNSET)

        on_field = d.pop("onField", UNSET)

        match_result_team = cls(
            team_number=team_number,
            station=station,
            dq=dq,
            on_field=on_field,
        )

        return match_result_team
