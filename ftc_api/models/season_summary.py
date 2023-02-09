import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ftc_api.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.summary_championship_description import SummaryChampionshipDescription


T = TypeVar("T", bound="SeasonSummary")


@attr.s(auto_attribs=True)
class SeasonSummary:
    """
    Attributes:
        event_count (Union[Unset, int]):
        game_name (Union[Unset, None, str]):
        kickoff (Union[Unset, None, datetime.datetime]):
        rookie_start (Union[Unset, int]):
        team_count (Union[Unset, int]):
        frc_championships (Union[Unset, None, List['SummaryChampionshipDescription']]):
    """

    event_count: Union[Unset, int] = UNSET
    game_name: Union[Unset, None, str] = UNSET
    kickoff: Union[Unset, None, datetime.datetime] = UNSET
    rookie_start: Union[Unset, int] = UNSET
    team_count: Union[Unset, int] = UNSET
    frc_championships: Union[
        Unset, None, List["SummaryChampionshipDescription"]
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        event_count = self.event_count
        game_name = self.game_name
        kickoff: Union[Unset, None, str] = UNSET
        if not isinstance(self.kickoff, Unset):
            kickoff = self.kickoff.isoformat() if self.kickoff else None

        rookie_start = self.rookie_start
        team_count = self.team_count
        frc_championships: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.frc_championships, Unset):
            if self.frc_championships is None:
                frc_championships = None
            else:
                frc_championships = []
                for frc_championships_item_data in self.frc_championships:
                    frc_championships_item = frc_championships_item_data.to_dict()

                    frc_championships.append(frc_championships_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if event_count is not UNSET:
            field_dict["eventCount"] = event_count
        if game_name is not UNSET:
            field_dict["gameName"] = game_name
        if kickoff is not UNSET:
            field_dict["kickoff"] = kickoff
        if rookie_start is not UNSET:
            field_dict["rookieStart"] = rookie_start
        if team_count is not UNSET:
            field_dict["teamCount"] = team_count
        if frc_championships is not UNSET:
            field_dict["frcChampionships"] = frc_championships

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.summary_championship_description import (
            SummaryChampionshipDescription,
        )

        d = src_dict.copy()
        event_count = d.pop("eventCount", UNSET)

        game_name = d.pop("gameName", UNSET)

        _kickoff = d.pop("kickoff", UNSET)
        kickoff: Union[Unset, None, datetime.datetime]
        if _kickoff is None:
            kickoff = None
        elif isinstance(_kickoff, Unset):
            kickoff = UNSET
        else:
            kickoff = isoparse(_kickoff)

        rookie_start = d.pop("rookieStart", UNSET)

        team_count = d.pop("teamCount", UNSET)

        frc_championships = []
        _frc_championships = d.pop("frcChampionships", UNSET)
        for frc_championships_item_data in _frc_championships or []:
            frc_championships_item = SummaryChampionshipDescription.from_dict(
                frc_championships_item_data
            )

            frc_championships.append(frc_championships_item)

        season_summary = cls(
            event_count=event_count,
            game_name=game_name,
            kickoff=kickoff,
            rookie_start=rookie_start,
            team_count=team_count,
            frc_championships=frc_championships,
        )

        return season_summary
