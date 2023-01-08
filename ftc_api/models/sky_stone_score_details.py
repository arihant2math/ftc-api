from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.ftc_event_level import FTCEventLevel
from .._types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sky_stone_alliance_score_details import SkyStoneAllianceScoreDetails


T = TypeVar("T", bound="SkyStoneScoreDetails")


@attr.s(auto_attribs=True)
class SkyStoneScoreDetails:
    """
    Attributes:
        match_level (Union[Unset, FTCEventLevel]):
        match_series (Union[Unset, int]):
        match_number (Union[Unset, int]):
        alliances (Union[Unset, None, List['SkyStoneAllianceScoreDetails']]):
    """

    match_level: Union[Unset, FTCEventLevel] = UNSET
    match_series: Union[Unset, int] = UNSET
    match_number: Union[Unset, int] = UNSET
    alliances: Union[Unset, None, List["SkyStoneAllianceScoreDetails"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        match_level: Union[Unset, str] = UNSET
        if not isinstance(self.match_level, Unset):
            match_level = self.match_level.value

        match_series = self.match_series
        match_number = self.match_number
        alliances: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.alliances, Unset):
            if self.alliances is None:
                alliances = None
            else:
                alliances = []
                for alliances_item_data in self.alliances:
                    alliances_item = alliances_item_data.to_dict()

                    alliances.append(alliances_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if match_level is not UNSET:
            field_dict["matchLevel"] = match_level
        if match_series is not UNSET:
            field_dict["matchSeries"] = match_series
        if match_number is not UNSET:
            field_dict["matchNumber"] = match_number
        if alliances is not UNSET:
            field_dict["alliances"] = alliances

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sky_stone_alliance_score_details import (
            SkyStoneAllianceScoreDetails,
        )

        d = src_dict.copy()
        _match_level = d.pop("matchLevel", UNSET)
        match_level: Union[Unset, FTCEventLevel]
        if isinstance(_match_level, Unset):
            match_level = UNSET
        else:
            match_level = FTCEventLevel(_match_level)

        match_series = d.pop("matchSeries", UNSET)

        match_number = d.pop("matchNumber", UNSET)

        alliances = []
        _alliances = d.pop("alliances", UNSET)
        for alliances_item_data in _alliances or []:
            alliances_item = SkyStoneAllianceScoreDetails.from_dict(alliances_item_data)

            alliances.append(alliances_item)

        sky_stone_score_details = cls(
            match_level=match_level,
            match_series=match_series,
            match_number=match_number,
            alliances=alliances,
        )

        return sky_stone_score_details
