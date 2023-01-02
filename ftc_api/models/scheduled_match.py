import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from .._types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scheduled_match_team import ScheduledMatchTeam


T = TypeVar("T", bound="ScheduledMatch")


@attr.s(auto_attribs=True)
class ScheduledMatch:
    """
    Attributes:
        description (Union[Unset, None, str]):
        field (Union[Unset, None, str]):
        tournament_level (Union[Unset, None, str]):
        start_time (Union[Unset, None, datetime.datetime]):
        series (Union[Unset, int]):
        match_number (Union[Unset, int]):
        teams (Union[Unset, None, List['ScheduledMatchTeam']]):
        modified_on (Union[Unset, None, datetime.datetime]):
    """

    description: Union[Unset, None, str] = UNSET
    field: Union[Unset, None, str] = UNSET
    tournament_level: Union[Unset, None, str] = UNSET
    start_time: Union[Unset, None, datetime.datetime] = UNSET
    series: Union[Unset, int] = UNSET
    match_number: Union[Unset, int] = UNSET
    teams: Union[Unset, None, List["ScheduledMatchTeam"]] = UNSET
    modified_on: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        field = self.field
        tournament_level = self.tournament_level
        start_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat() if self.start_time else None

        series = self.series
        match_number = self.match_number
        teams: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.teams, Unset):
            if self.teams is None:
                teams = None
            else:
                teams = []
                for teams_item_data in self.teams:
                    teams_item = teams_item_data.to_dict()

                    teams.append(teams_item)

        modified_on: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_on, Unset):
            modified_on = self.modified_on.isoformat() if self.modified_on else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if field is not UNSET:
            field_dict["field"] = field
        if tournament_level is not UNSET:
            field_dict["tournamentLevel"] = tournament_level
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if series is not UNSET:
            field_dict["series"] = series
        if match_number is not UNSET:
            field_dict["matchNumber"] = match_number
        if teams is not UNSET:
            field_dict["teams"] = teams
        if modified_on is not UNSET:
            field_dict["modifiedOn"] = modified_on

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scheduled_match_team import ScheduledMatchTeam

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        field = d.pop("field", UNSET)

        tournament_level = d.pop("tournamentLevel", UNSET)

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, None, datetime.datetime]
        if _start_time is None:
            start_time = None
        elif isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        series = d.pop("series", UNSET)

        match_number = d.pop("matchNumber", UNSET)

        teams = []
        _teams = d.pop("teams", UNSET)
        for teams_item_data in _teams or []:
            teams_item = ScheduledMatchTeam.from_dict(teams_item_data)

            teams.append(teams_item)

        _modified_on = d.pop("modifiedOn", UNSET)
        modified_on: Union[Unset, None, datetime.datetime]
        if _modified_on is None:
            modified_on = None
        elif isinstance(_modified_on, Unset):
            modified_on = UNSET
        else:
            modified_on = isoparse(_modified_on)

        scheduled_match = cls(
            description=description,
            field=field,
            tournament_level=tournament_level,
            start_time=start_time,
            series=series,
            match_number=match_number,
            teams=teams,
            modified_on=modified_on,
        )

        return scheduled_match
