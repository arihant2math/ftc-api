from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.ftc_event_level import FTCEventLevel
from .._types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.freight_frenzy_remote_score_breakdown import FreightFrenzyRemoteScoreBreakdown


T = TypeVar("T", bound="FreightFrenzySingleTeamScoreDetails")


@attr.s(auto_attribs=True)
class FreightFrenzySingleTeamScoreDetails:
    """
    Attributes:
        match_level (Union[Unset, FTCEventLevel]):
        match_number (Union[Unset, int]):
        randomization (Union[Unset, int]):
        team_number (Union[Unset, int]):
        scores (Union[Unset, FreightFrenzyRemoteScoreBreakdown]):
    """

    match_level: Union[Unset, FTCEventLevel] = UNSET
    match_number: Union[Unset, int] = UNSET
    randomization: Union[Unset, int] = UNSET
    team_number: Union[Unset, int] = UNSET
    scores: Union[Unset, "FreightFrenzyRemoteScoreBreakdown"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        match_level: Union[Unset, str] = UNSET
        if not isinstance(self.match_level, Unset):
            match_level = self.match_level.value

        match_number = self.match_number
        randomization = self.randomization
        team_number = self.team_number
        scores: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.scores, Unset):
            scores = self.scores.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if match_level is not UNSET:
            field_dict["matchLevel"] = match_level
        if match_number is not UNSET:
            field_dict["matchNumber"] = match_number
        if randomization is not UNSET:
            field_dict["randomization"] = randomization
        if team_number is not UNSET:
            field_dict["teamNumber"] = team_number
        if scores is not UNSET:
            field_dict["scores"] = scores

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.freight_frenzy_remote_score_breakdown import FreightFrenzyRemoteScoreBreakdown

        d = src_dict.copy()
        _match_level = d.pop("matchLevel", UNSET)
        match_level: Union[Unset, FTCEventLevel]
        if isinstance(_match_level, Unset):
            match_level = UNSET
        else:
            match_level = FTCEventLevel(_match_level)

        match_number = d.pop("matchNumber", UNSET)

        randomization = d.pop("randomization", UNSET)

        team_number = d.pop("teamNumber", UNSET)

        _scores = d.pop("scores", UNSET)
        scores: Union[Unset, FreightFrenzyRemoteScoreBreakdown]
        if isinstance(_scores, Unset):
            scores = UNSET
        else:
            scores = FreightFrenzyRemoteScoreBreakdown.from_dict(_scores)

        freight_frenzy_single_team_score_details = cls(
            match_level=match_level,
            match_number=match_number,
            randomization=randomization,
            team_number=team_number,
            scores=scores,
        )

        return freight_frenzy_single_team_score_details
