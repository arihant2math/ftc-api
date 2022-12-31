from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.freight_frenzy_alliance_score_details import FreightFrenzyAllianceScoreDetails
    from ..models.freight_frenzy_single_team_score_details import FreightFrenzySingleTeamScoreDetails
    from ..models.power_play_alliance_score_details import PowerPlayAllianceScoreDetails
    from ..models.power_play_single_team_score_details import PowerPlaySingleTeamScoreDetails
    from ..models.sky_stone_score_details import SkyStoneScoreDetails
    from ..models.ultimate_goal_alliance_score_details import UltimateGoalAllianceScoreDetails
    from ..models.ultimate_goal_single_team_score_details import UltimateGoalSingleTeamScoreDetails


T = TypeVar("T", bound="MatchScoreList")


@attr.s(auto_attribs=True)
class MatchScoreList:
    """
    Attributes:
        match_scores (Union[Unset, None, List[Union['FreightFrenzyAllianceScoreDetails',
            'FreightFrenzySingleTeamScoreDetails', 'PowerPlayAllianceScoreDetails', 'PowerPlaySingleTeamScoreDetails',
            'SkyStoneScoreDetails', 'UltimateGoalAllianceScoreDetails', 'UltimateGoalSingleTeamScoreDetails']]]):
    """

    match_scores: Union[
        Unset,
        None,
        List[
            Union[
                "FreightFrenzyAllianceScoreDetails",
                "FreightFrenzySingleTeamScoreDetails",
                "PowerPlayAllianceScoreDetails",
                "PowerPlaySingleTeamScoreDetails",
                "SkyStoneScoreDetails",
                "UltimateGoalAllianceScoreDetails",
                "UltimateGoalSingleTeamScoreDetails",
            ]
        ],
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.freight_frenzy_alliance_score_details import FreightFrenzyAllianceScoreDetails
        from ..models.freight_frenzy_single_team_score_details import FreightFrenzySingleTeamScoreDetails
        from ..models.power_play_alliance_score_details import PowerPlayAllianceScoreDetails
        from ..models.sky_stone_score_details import SkyStoneScoreDetails
        from ..models.ultimate_goal_alliance_score_details import UltimateGoalAllianceScoreDetails
        from ..models.ultimate_goal_single_team_score_details import UltimateGoalSingleTeamScoreDetails

        match_scores: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.match_scores, Unset):
            if self.match_scores is None:
                match_scores = None
            else:
                match_scores = []
                for match_scores_item_data in self.match_scores:
                    match_scores_item: Dict[str, Any]

                    if isinstance(match_scores_item_data, SkyStoneScoreDetails):
                        match_scores_item = match_scores_item_data.to_dict()

                    elif isinstance(match_scores_item_data, UltimateGoalAllianceScoreDetails):
                        match_scores_item = match_scores_item_data.to_dict()

                    elif isinstance(match_scores_item_data, UltimateGoalSingleTeamScoreDetails):
                        match_scores_item = match_scores_item_data.to_dict()

                    elif isinstance(match_scores_item_data, FreightFrenzyAllianceScoreDetails):
                        match_scores_item = match_scores_item_data.to_dict()

                    elif isinstance(match_scores_item_data, FreightFrenzySingleTeamScoreDetails):
                        match_scores_item = match_scores_item_data.to_dict()

                    elif isinstance(match_scores_item_data, PowerPlayAllianceScoreDetails):
                        match_scores_item = match_scores_item_data.to_dict()

                    else:
                        match_scores_item = match_scores_item_data.to_dict()

                    match_scores.append(match_scores_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if match_scores is not UNSET:
            field_dict["MatchScores"] = match_scores

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.freight_frenzy_alliance_score_details import FreightFrenzyAllianceScoreDetails
        from ..models.freight_frenzy_single_team_score_details import FreightFrenzySingleTeamScoreDetails
        from ..models.power_play_alliance_score_details import PowerPlayAllianceScoreDetails
        from ..models.power_play_single_team_score_details import PowerPlaySingleTeamScoreDetails
        from ..models.sky_stone_score_details import SkyStoneScoreDetails
        from ..models.ultimate_goal_alliance_score_details import UltimateGoalAllianceScoreDetails
        from ..models.ultimate_goal_single_team_score_details import UltimateGoalSingleTeamScoreDetails

        d = src_dict.copy()
        match_scores = []
        _match_scores = d.pop("MatchScores", UNSET)
        for match_scores_item_data in _match_scores or []:

            def _parse_match_scores_item(
                data: object,
            ) -> Union[
                "FreightFrenzyAllianceScoreDetails",
                "FreightFrenzySingleTeamScoreDetails",
                "PowerPlayAllianceScoreDetails",
                "PowerPlaySingleTeamScoreDetails",
                "SkyStoneScoreDetails",
                "UltimateGoalAllianceScoreDetails",
                "UltimateGoalSingleTeamScoreDetails",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    match_scores_item_type_0 = SkyStoneScoreDetails.from_dict(data)

                    return match_scores_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    match_scores_item_type_1 = UltimateGoalAllianceScoreDetails.from_dict(data)

                    return match_scores_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    match_scores_item_type_2 = UltimateGoalSingleTeamScoreDetails.from_dict(data)

                    return match_scores_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    match_scores_item_type_3 = FreightFrenzyAllianceScoreDetails.from_dict(data)

                    return match_scores_item_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    match_scores_item_type_4 = FreightFrenzySingleTeamScoreDetails.from_dict(data)

                    return match_scores_item_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    match_scores_item_type_5 = PowerPlayAllianceScoreDetails.from_dict(data)

                    return match_scores_item_type_5
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                match_scores_item_type_6 = PowerPlaySingleTeamScoreDetails.from_dict(data)

                return match_scores_item_type_6

            match_scores_item = _parse_match_scores_item(match_scores_item_data)

            match_scores.append(match_scores_item)

        match_score_list = cls(
            match_scores=match_scores,
        )

        return match_score_list
