import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.match_result_team import MatchResultTeam


T = TypeVar("T", bound="MatchResult")


@attr.s(auto_attribs=True)
class MatchResult:
    """
    Attributes:
        actual_start_time (Union[Unset, None, datetime.datetime]):
        description (Union[Unset, None, str]):
        tournament_level (Union[Unset, None, str]):
        series (Union[Unset, int]):
        match_number (Union[Unset, int]):
        score_red_final (Union[Unset, int]):
        score_red_foul (Union[Unset, int]):
        score_red_auto (Union[Unset, int]):
        score_blue_final (Union[Unset, int]):
        score_blue_foul (Union[Unset, int]):
        score_blue_auto (Union[Unset, int]):
        post_result_time (Union[Unset, None, datetime.datetime]):
        teams (Union[Unset, None, List['MatchResultTeam']]):
        modified_on (Union[Unset, None, datetime.datetime]):
    """

    actual_start_time: Union[Unset, None, datetime.datetime] = UNSET
    description: Union[Unset, None, str] = UNSET
    tournament_level: Union[Unset, None, str] = UNSET
    series: Union[Unset, int] = UNSET
    match_number: Union[Unset, int] = UNSET
    score_red_final: Union[Unset, int] = UNSET
    score_red_foul: Union[Unset, int] = UNSET
    score_red_auto: Union[Unset, int] = UNSET
    score_blue_final: Union[Unset, int] = UNSET
    score_blue_foul: Union[Unset, int] = UNSET
    score_blue_auto: Union[Unset, int] = UNSET
    post_result_time: Union[Unset, None, datetime.datetime] = UNSET
    teams: Union[Unset, None, List["MatchResultTeam"]] = UNSET
    modified_on: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        actual_start_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.actual_start_time, Unset):
            actual_start_time = self.actual_start_time.isoformat() if self.actual_start_time else None

        description = self.description
        tournament_level = self.tournament_level
        series = self.series
        match_number = self.match_number
        score_red_final = self.score_red_final
        score_red_foul = self.score_red_foul
        score_red_auto = self.score_red_auto
        score_blue_final = self.score_blue_final
        score_blue_foul = self.score_blue_foul
        score_blue_auto = self.score_blue_auto
        post_result_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.post_result_time, Unset):
            post_result_time = self.post_result_time.isoformat() if self.post_result_time else None

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
        if actual_start_time is not UNSET:
            field_dict["actualStartTime"] = actual_start_time
        if description is not UNSET:
            field_dict["description"] = description
        if tournament_level is not UNSET:
            field_dict["tournamentLevel"] = tournament_level
        if series is not UNSET:
            field_dict["series"] = series
        if match_number is not UNSET:
            field_dict["matchNumber"] = match_number
        if score_red_final is not UNSET:
            field_dict["scoreRedFinal"] = score_red_final
        if score_red_foul is not UNSET:
            field_dict["scoreRedFoul"] = score_red_foul
        if score_red_auto is not UNSET:
            field_dict["scoreRedAuto"] = score_red_auto
        if score_blue_final is not UNSET:
            field_dict["scoreBlueFinal"] = score_blue_final
        if score_blue_foul is not UNSET:
            field_dict["scoreBlueFoul"] = score_blue_foul
        if score_blue_auto is not UNSET:
            field_dict["scoreBlueAuto"] = score_blue_auto
        if post_result_time is not UNSET:
            field_dict["postResultTime"] = post_result_time
        if teams is not UNSET:
            field_dict["teams"] = teams
        if modified_on is not UNSET:
            field_dict["modifiedOn"] = modified_on

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.match_result_team import MatchResultTeam

        d = src_dict.copy()
        _actual_start_time = d.pop("actualStartTime", UNSET)
        actual_start_time: Union[Unset, None, datetime.datetime]
        if _actual_start_time is None:
            actual_start_time = None
        elif isinstance(_actual_start_time, Unset):
            actual_start_time = UNSET
        else:
            actual_start_time = isoparse(_actual_start_time)

        description = d.pop("description", UNSET)

        tournament_level = d.pop("tournamentLevel", UNSET)

        series = d.pop("series", UNSET)

        match_number = d.pop("matchNumber", UNSET)

        score_red_final = d.pop("scoreRedFinal", UNSET)

        score_red_foul = d.pop("scoreRedFoul", UNSET)

        score_red_auto = d.pop("scoreRedAuto", UNSET)

        score_blue_final = d.pop("scoreBlueFinal", UNSET)

        score_blue_foul = d.pop("scoreBlueFoul", UNSET)

        score_blue_auto = d.pop("scoreBlueAuto", UNSET)

        _post_result_time = d.pop("postResultTime", UNSET)
        post_result_time: Union[Unset, None, datetime.datetime]
        if _post_result_time is None:
            post_result_time = None
        elif isinstance(_post_result_time, Unset):
            post_result_time = UNSET
        else:
            post_result_time = isoparse(_post_result_time)

        teams = []
        _teams = d.pop("teams", UNSET)
        for teams_item_data in _teams or []:
            teams_item = MatchResultTeam.from_dict(teams_item_data)

            teams.append(teams_item)

        _modified_on = d.pop("modifiedOn", UNSET)
        modified_on: Union[Unset, None, datetime.datetime]
        if _modified_on is None:
            modified_on = None
        elif isinstance(_modified_on, Unset):
            modified_on = UNSET
        else:
            modified_on = isoparse(_modified_on)

        match_result = cls(
            actual_start_time=actual_start_time,
            description=description,
            tournament_level=tournament_level,
            series=series,
            match_number=match_number,
            score_red_final=score_red_final,
            score_red_foul=score_red_foul,
            score_red_auto=score_red_auto,
            score_blue_final=score_blue_final,
            score_blue_foul=score_blue_foul,
            score_blue_auto=score_blue_auto,
            post_result_time=post_result_time,
            teams=teams,
            modified_on=modified_on,
        )

        return match_result
