from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamRanking")


@attr.s(auto_attribs=True)
class TeamRanking:
    """
    Attributes:
        rank (Union[Unset, int]):
        team_number (Union[Unset, int]):
        team_name (Union[Unset, None, str]):
        sort_order_1 (Union[Unset, float]):
        sort_order_2 (Union[Unset, float]):
        sort_order_3 (Union[Unset, float]):
        sort_order_4 (Union[Unset, float]):
        sort_order_5 (Union[Unset, float]):
        sort_order_6 (Union[Unset, float]):
        wins (Union[Unset, int]):
        losses (Union[Unset, int]):
        ties (Union[Unset, int]):
        qual_average (Union[Unset, float]):
        dq (Union[Unset, int]):
        matches_played (Union[Unset, int]):
        matches_counted (Union[Unset, int]):
    """

    rank: Union[Unset, int] = UNSET
    team_number: Union[Unset, int] = UNSET
    team_name: Union[Unset, None, str] = UNSET
    sort_order_1: Union[Unset, float] = UNSET
    sort_order_2: Union[Unset, float] = UNSET
    sort_order_3: Union[Unset, float] = UNSET
    sort_order_4: Union[Unset, float] = UNSET
    sort_order_5: Union[Unset, float] = UNSET
    sort_order_6: Union[Unset, float] = UNSET
    wins: Union[Unset, int] = UNSET
    losses: Union[Unset, int] = UNSET
    ties: Union[Unset, int] = UNSET
    qual_average: Union[Unset, float] = UNSET
    dq: Union[Unset, int] = UNSET
    matches_played: Union[Unset, int] = UNSET
    matches_counted: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        rank = self.rank
        team_number = self.team_number
        team_name = self.team_name
        sort_order_1 = self.sort_order_1
        sort_order_2 = self.sort_order_2
        sort_order_3 = self.sort_order_3
        sort_order_4 = self.sort_order_4
        sort_order_5 = self.sort_order_5
        sort_order_6 = self.sort_order_6
        wins = self.wins
        losses = self.losses
        ties = self.ties
        qual_average = self.qual_average
        dq = self.dq
        matches_played = self.matches_played
        matches_counted = self.matches_counted

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if rank is not UNSET:
            field_dict["rank"] = rank
        if team_number is not UNSET:
            field_dict["teamNumber"] = team_number
        if team_name is not UNSET:
            field_dict["teamName"] = team_name
        if sort_order_1 is not UNSET:
            field_dict["sortOrder1"] = sort_order_1
        if sort_order_2 is not UNSET:
            field_dict["sortOrder2"] = sort_order_2
        if sort_order_3 is not UNSET:
            field_dict["sortOrder3"] = sort_order_3
        if sort_order_4 is not UNSET:
            field_dict["sortOrder4"] = sort_order_4
        if sort_order_5 is not UNSET:
            field_dict["sortOrder5"] = sort_order_5
        if sort_order_6 is not UNSET:
            field_dict["sortOrder6"] = sort_order_6
        if wins is not UNSET:
            field_dict["wins"] = wins
        if losses is not UNSET:
            field_dict["losses"] = losses
        if ties is not UNSET:
            field_dict["ties"] = ties
        if qual_average is not UNSET:
            field_dict["qualAverage"] = qual_average
        if dq is not UNSET:
            field_dict["dq"] = dq
        if matches_played is not UNSET:
            field_dict["matchesPlayed"] = matches_played
        if matches_counted is not UNSET:
            field_dict["matchesCounted"] = matches_counted

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rank = d.pop("rank", UNSET)

        team_number = d.pop("teamNumber", UNSET)

        team_name = d.pop("teamName", UNSET)

        sort_order_1 = d.pop("sortOrder1", UNSET)

        sort_order_2 = d.pop("sortOrder2", UNSET)

        sort_order_3 = d.pop("sortOrder3", UNSET)

        sort_order_4 = d.pop("sortOrder4", UNSET)

        sort_order_5 = d.pop("sortOrder5", UNSET)

        sort_order_6 = d.pop("sortOrder6", UNSET)

        wins = d.pop("wins", UNSET)

        losses = d.pop("losses", UNSET)

        ties = d.pop("ties", UNSET)

        qual_average = d.pop("qualAverage", UNSET)

        dq = d.pop("dq", UNSET)

        matches_played = d.pop("matchesPlayed", UNSET)

        matches_counted = d.pop("matchesCounted", UNSET)

        team_ranking = cls(
            rank=rank,
            team_number=team_number,
            team_name=team_name,
            sort_order_1=sort_order_1,
            sort_order_2=sort_order_2,
            sort_order_3=sort_order_3,
            sort_order_4=sort_order_4,
            sort_order_5=sort_order_5,
            sort_order_6=sort_order_6,
            wins=wins,
            losses=losses,
            ties=ties,
            qual_average=qual_average,
            dq=dq,
            matches_played=matches_played,
            matches_counted=matches_counted,
        )

        return team_ranking
