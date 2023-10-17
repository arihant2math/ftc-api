from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="HybridScheduleTeam")


@_attrs_define
class HybridScheduleTeam:
    """
    Attributes:
        team_number (Union[Unset, None, int]):
        station (Union[Unset, None, str]):
        surrogate (Union[Unset, bool]):
        no_show (Union[Unset, bool]):
        dq (Union[Unset, None, bool]):
        on_field (Union[Unset, None, bool]):
        team_name (Union[Unset, None, str]):
    """

    team_number: Union[Unset, None, int] = UNSET
    station: Union[Unset, None, str] = UNSET
    surrogate: Union[Unset, bool] = UNSET
    no_show: Union[Unset, bool] = UNSET
    dq: Union[Unset, None, bool] = UNSET
    on_field: Union[Unset, None, bool] = UNSET
    team_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        team_number = self.team_number
        station = self.station
        surrogate = self.surrogate
        no_show = self.no_show
        dq = self.dq
        on_field = self.on_field
        team_name = self.team_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if team_number is not UNSET:
            field_dict["teamNumber"] = team_number
        if station is not UNSET:
            field_dict["station"] = station
        if surrogate is not UNSET:
            field_dict["surrogate"] = surrogate
        if no_show is not UNSET:
            field_dict["noShow"] = no_show
        if dq is not UNSET:
            field_dict["dq"] = dq
        if on_field is not UNSET:
            field_dict["onField"] = on_field
        if team_name is not UNSET:
            field_dict["teamName"] = team_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        team_number = d.pop("teamNumber", UNSET)

        station = d.pop("station", UNSET)

        surrogate = d.pop("surrogate", UNSET)

        no_show = d.pop("noShow", UNSET)

        dq = d.pop("dq", UNSET)

        on_field = d.pop("onField", UNSET)

        team_name = d.pop("teamName", UNSET)

        hybrid_schedule_team = cls(
            team_number=team_number,
            station=station,
            surrogate=surrogate,
            no_show=no_show,
            dq=dq,
            on_field=on_field,
            team_name=team_name,
        )

        return hybrid_schedule_team
