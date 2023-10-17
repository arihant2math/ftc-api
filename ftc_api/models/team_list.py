from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team import Team


T = TypeVar("T", bound="TeamList")


@_attrs_define
class TeamList:
    """
    Attributes:
        teams (Union[Unset, None, List['Team']]):
        team_count_total (Union[Unset, int]):
        team_count_page (Union[Unset, int]):
        page_current (Union[Unset, int]):
        page_total (Union[Unset, int]):
    """

    teams: Union[Unset, None, List["Team"]] = UNSET
    team_count_total: Union[Unset, int] = UNSET
    team_count_page: Union[Unset, int] = UNSET
    page_current: Union[Unset, int] = UNSET
    page_total: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        teams: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.teams, Unset):
            if self.teams is None:
                teams = None
            else:
                teams = []
                for teams_item_data in self.teams:
                    teams_item = teams_item_data.to_dict()

                    teams.append(teams_item)

        team_count_total = self.team_count_total
        team_count_page = self.team_count_page
        page_current = self.page_current
        page_total = self.page_total

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if teams is not UNSET:
            field_dict["teams"] = teams
        if team_count_total is not UNSET:
            field_dict["teamCountTotal"] = team_count_total
        if team_count_page is not UNSET:
            field_dict["teamCountPage"] = team_count_page
        if page_current is not UNSET:
            field_dict["pageCurrent"] = page_current
        if page_total is not UNSET:
            field_dict["pageTotal"] = page_total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team import Team

        d = src_dict.copy()
        teams = []
        _teams = d.pop("teams", UNSET)
        for teams_item_data in _teams or []:
            teams_item = Team.from_dict(teams_item_data)

            teams.append(teams_item)

        team_count_total = d.pop("teamCountTotal", UNSET)

        team_count_page = d.pop("teamCountPage", UNSET)

        page_current = d.pop("pageCurrent", UNSET)

        page_total = d.pop("pageTotal", UNSET)

        team_list = cls(
            teams=teams,
            team_count_total=team_count_total,
            team_count_page=team_count_page,
            page_current=page_current,
            page_total=page_total,
        )

        return team_list
