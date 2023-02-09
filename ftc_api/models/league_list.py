from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.league import League


T = TypeVar("T", bound="LeagueList")


@attr.s(auto_attribs=True)
class LeagueList:
    """
    Attributes:
        leagues (Union[Unset, None, List['League']]):
        league_count (Union[Unset, int]):
    """

    leagues: Union[Unset, None, List["League"]] = UNSET
    league_count: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        leagues: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.leagues, Unset):
            if self.leagues is None:
                leagues = None
            else:
                leagues = []
                for leagues_item_data in self.leagues:
                    leagues_item = leagues_item_data.to_dict()

                    leagues.append(leagues_item)

        league_count = self.league_count

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if leagues is not UNSET:
            field_dict["leagues"] = leagues
        if league_count is not UNSET:
            field_dict["leagueCount"] = league_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.league import League

        d = src_dict.copy()
        leagues = []
        _leagues = d.pop("leagues", UNSET)
        for leagues_item_data in _leagues or []:
            leagues_item = League.from_dict(leagues_item_data)

            leagues.append(leagues_item)

        league_count = d.pop("leagueCount", UNSET)

        league_list = cls(
            leagues=leagues,
            league_count=league_count,
        )

        return league_list
