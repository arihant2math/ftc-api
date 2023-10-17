from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team_ranking import TeamRanking


T = TypeVar("T", bound="EventRankingList")


@_attrs_define
class EventRankingList:
    """
    Attributes:
        rankings (Union[Unset, None, List['TeamRanking']]):
    """

    rankings: Union[Unset, None, List["TeamRanking"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        rankings: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rankings, Unset):
            if self.rankings is None:
                rankings = None
            else:
                rankings = []
                for rankings_item_data in self.rankings:
                    rankings_item = rankings_item_data.to_dict()

                    rankings.append(rankings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if rankings is not UNSET:
            field_dict["Rankings"] = rankings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team_ranking import TeamRanking

        d = src_dict.copy()
        rankings = []
        _rankings = d.pop("Rankings", UNSET)
        for rankings_item_data in _rankings or []:
            rankings_item = TeamRanking.from_dict(rankings_item_data)

            rankings.append(rankings_item)

        event_ranking_list = cls(
            rankings=rankings,
        )

        return event_ranking_list
