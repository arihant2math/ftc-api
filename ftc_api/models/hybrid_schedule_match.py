import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hybrid_schedule_team import HybridScheduleTeam


T = TypeVar("T", bound="HybridScheduleMatch")


@_attrs_define
class HybridScheduleMatch:
    """
    Attributes:
        description (Union[Unset, None, str]):
        tournament_level (Union[Unset, None, str]):
        series (Union[Unset, int]):
        match_number (Union[Unset, int]):
        start_time (Union[Unset, None, datetime.datetime]):
        actual_start_time (Union[Unset, None, datetime.datetime]):
        post_result_time (Union[Unset, None, datetime.datetime]):
        score_red_final (Union[Unset, None, int]):
        score_red_foul (Union[Unset, None, int]):
        score_red_auto (Union[Unset, None, int]):
        score_blue_final (Union[Unset, None, int]):
        score_blue_foul (Union[Unset, None, int]):
        score_blue_auto (Union[Unset, None, int]):
        score_blue_drive_controlled (Union[Unset, None, int]):
        score_blue_endgame (Union[Unset, None, int]):
        red_wins (Union[Unset, None, bool]):
        blue_wins (Union[Unset, None, bool]):
        teams (Union[Unset, None, List['HybridScheduleTeam']]):
    """

    description: Union[Unset, None, str] = UNSET
    tournament_level: Union[Unset, None, str] = UNSET
    series: Union[Unset, int] = UNSET
    match_number: Union[Unset, int] = UNSET
    start_time: Union[Unset, None, datetime.datetime] = UNSET
    actual_start_time: Union[Unset, None, datetime.datetime] = UNSET
    post_result_time: Union[Unset, None, datetime.datetime] = UNSET
    score_red_final: Union[Unset, None, int] = UNSET
    score_red_foul: Union[Unset, None, int] = UNSET
    score_red_auto: Union[Unset, None, int] = UNSET
    score_blue_final: Union[Unset, None, int] = UNSET
    score_blue_foul: Union[Unset, None, int] = UNSET
    score_blue_auto: Union[Unset, None, int] = UNSET
    score_blue_drive_controlled: Union[Unset, None, int] = UNSET
    score_blue_endgame: Union[Unset, None, int] = UNSET
    red_wins: Union[Unset, None, bool] = UNSET
    blue_wins: Union[Unset, None, bool] = UNSET
    teams: Union[Unset, None, List["HybridScheduleTeam"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        tournament_level = self.tournament_level
        series = self.series
        match_number = self.match_number
        start_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat() if self.start_time else None

        actual_start_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.actual_start_time, Unset):
            actual_start_time = self.actual_start_time.isoformat() if self.actual_start_time else None

        post_result_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.post_result_time, Unset):
            post_result_time = self.post_result_time.isoformat() if self.post_result_time else None

        score_red_final = self.score_red_final
        score_red_foul = self.score_red_foul
        score_red_auto = self.score_red_auto
        score_blue_final = self.score_blue_final
        score_blue_foul = self.score_blue_foul
        score_blue_auto = self.score_blue_auto
        score_blue_drive_controlled = self.score_blue_drive_controlled
        score_blue_endgame = self.score_blue_endgame
        red_wins = self.red_wins
        blue_wins = self.blue_wins
        teams: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.teams, Unset):
            if self.teams is None:
                teams = None
            else:
                teams = []
                for teams_item_data in self.teams:
                    teams_item = teams_item_data.to_dict()

                    teams.append(teams_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if tournament_level is not UNSET:
            field_dict["tournamentLevel"] = tournament_level
        if series is not UNSET:
            field_dict["series"] = series
        if match_number is not UNSET:
            field_dict["matchNumber"] = match_number
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if actual_start_time is not UNSET:
            field_dict["actualStartTime"] = actual_start_time
        if post_result_time is not UNSET:
            field_dict["postResultTime"] = post_result_time
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
        if score_blue_drive_controlled is not UNSET:
            field_dict["scoreBlueDriveControlled"] = score_blue_drive_controlled
        if score_blue_endgame is not UNSET:
            field_dict["scoreBlueEndgame"] = score_blue_endgame
        if red_wins is not UNSET:
            field_dict["redWins"] = red_wins
        if blue_wins is not UNSET:
            field_dict["blueWins"] = blue_wins
        if teams is not UNSET:
            field_dict["teams"] = teams

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.hybrid_schedule_team import HybridScheduleTeam

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        tournament_level = d.pop("tournamentLevel", UNSET)

        series = d.pop("series", UNSET)

        match_number = d.pop("matchNumber", UNSET)

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, None, datetime.datetime]
        if _start_time is None:
            start_time = None
        elif isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _actual_start_time = d.pop("actualStartTime", UNSET)
        actual_start_time: Union[Unset, None, datetime.datetime]
        if _actual_start_time is None:
            actual_start_time = None
        elif isinstance(_actual_start_time, Unset):
            actual_start_time = UNSET
        else:
            actual_start_time = isoparse(_actual_start_time)

        _post_result_time = d.pop("postResultTime", UNSET)
        post_result_time: Union[Unset, None, datetime.datetime]
        if _post_result_time is None:
            post_result_time = None
        elif isinstance(_post_result_time, Unset):
            post_result_time = UNSET
        else:
            post_result_time = isoparse(_post_result_time)

        score_red_final = d.pop("scoreRedFinal", UNSET)

        score_red_foul = d.pop("scoreRedFoul", UNSET)

        score_red_auto = d.pop("scoreRedAuto", UNSET)

        score_blue_final = d.pop("scoreBlueFinal", UNSET)

        score_blue_foul = d.pop("scoreBlueFoul", UNSET)

        score_blue_auto = d.pop("scoreBlueAuto", UNSET)

        score_blue_drive_controlled = d.pop("scoreBlueDriveControlled", UNSET)

        score_blue_endgame = d.pop("scoreBlueEndgame", UNSET)

        red_wins = d.pop("redWins", UNSET)

        blue_wins = d.pop("blueWins", UNSET)

        teams = []
        _teams = d.pop("teams", UNSET)
        for teams_item_data in _teams or []:
            teams_item = HybridScheduleTeam.from_dict(teams_item_data)

            teams.append(teams_item)

        hybrid_schedule_match = cls(
            description=description,
            tournament_level=tournament_level,
            series=series,
            match_number=match_number,
            start_time=start_time,
            actual_start_time=actual_start_time,
            post_result_time=post_result_time,
            score_red_final=score_red_final,
            score_red_foul=score_red_foul,
            score_red_auto=score_red_auto,
            score_blue_final=score_blue_final,
            score_blue_foul=score_blue_foul,
            score_blue_auto=score_blue_auto,
            score_blue_drive_controlled=score_blue_drive_controlled,
            score_blue_endgame=score_blue_endgame,
            red_wins=red_wins,
            blue_wins=blue_wins,
            teams=teams,
        )

        return hybrid_schedule_match
