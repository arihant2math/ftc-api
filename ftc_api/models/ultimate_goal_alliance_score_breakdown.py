from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UltimateGoalAllianceScoreBreakdown")


@_attrs_define
class UltimateGoalAllianceScoreBreakdown:
    """
    Attributes:
        adjust (Union[Unset, int]):
        dc_points (Union[Unset, int]):
        auto_points (Union[Unset, int]):
        dc_tower_low (Union[Unset, int]):
        dc_tower_mid (Union[Unset, int]):
        dc_tower_high (Union[Unset, int]):
        navigated1 (Union[Unset, bool]):
        navigated2 (Union[Unset, bool]):
        wobble_delivered_1 (Union[Unset, bool]):
        wobble_delivered_2 (Union[Unset, bool]):
        auto_tower_low (Union[Unset, int]):
        auto_tower_mid (Union[Unset, int]):
        auto_tower_high (Union[Unset, int]):
        auto_tower_points (Union[Unset, int]):
        auto_power_shot_left (Union[Unset, bool]):
        auto_power_shot_center (Union[Unset, bool]):
        auto_power_shot_right (Union[Unset, bool]):
        auto_power_shot_points (Union[Unset, int]):
        wobble_rings_1 (Union[Unset, int]):
        wobble_rings_2 (Union[Unset, int]):
        wobble_end_1 (Union[Unset, int]):
        wobble_end_2 (Union[Unset, int]):
        wobble_end_points (Union[Unset, int]):
        wobble_ring_points (Union[Unset, int]):
        auto_wobble_points (Union[Unset, int]):
        end_power_shot_left (Union[Unset, bool]):
        end_power_shot_center (Union[Unset, bool]):
        end_power_shot_right (Union[Unset, bool]):
        end_power_shot_points (Union[Unset, int]):
        penalty_points (Union[Unset, int]):
        major_penalties (Union[Unset, int]):
        minor_penalties (Union[Unset, int]):
        navigation_points (Union[Unset, int]):
        endgame_points (Union[Unset, int]):
        total_points (Union[Unset, int]):
        alliance (Union[Unset, None, str]):
        team (Union[Unset, int]):
    """

    adjust: Union[Unset, int] = UNSET
    dc_points: Union[Unset, int] = UNSET
    auto_points: Union[Unset, int] = UNSET
    dc_tower_low: Union[Unset, int] = UNSET
    dc_tower_mid: Union[Unset, int] = UNSET
    dc_tower_high: Union[Unset, int] = UNSET
    navigated1: Union[Unset, bool] = UNSET
    navigated2: Union[Unset, bool] = UNSET
    wobble_delivered_1: Union[Unset, bool] = UNSET
    wobble_delivered_2: Union[Unset, bool] = UNSET
    auto_tower_low: Union[Unset, int] = UNSET
    auto_tower_mid: Union[Unset, int] = UNSET
    auto_tower_high: Union[Unset, int] = UNSET
    auto_tower_points: Union[Unset, int] = UNSET
    auto_power_shot_left: Union[Unset, bool] = UNSET
    auto_power_shot_center: Union[Unset, bool] = UNSET
    auto_power_shot_right: Union[Unset, bool] = UNSET
    auto_power_shot_points: Union[Unset, int] = UNSET
    wobble_rings_1: Union[Unset, int] = UNSET
    wobble_rings_2: Union[Unset, int] = UNSET
    wobble_end_1: Union[Unset, int] = UNSET
    wobble_end_2: Union[Unset, int] = UNSET
    wobble_end_points: Union[Unset, int] = UNSET
    wobble_ring_points: Union[Unset, int] = UNSET
    auto_wobble_points: Union[Unset, int] = UNSET
    end_power_shot_left: Union[Unset, bool] = UNSET
    end_power_shot_center: Union[Unset, bool] = UNSET
    end_power_shot_right: Union[Unset, bool] = UNSET
    end_power_shot_points: Union[Unset, int] = UNSET
    penalty_points: Union[Unset, int] = UNSET
    major_penalties: Union[Unset, int] = UNSET
    minor_penalties: Union[Unset, int] = UNSET
    navigation_points: Union[Unset, int] = UNSET
    endgame_points: Union[Unset, int] = UNSET
    total_points: Union[Unset, int] = UNSET
    alliance: Union[Unset, None, str] = UNSET
    team: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        adjust = self.adjust
        dc_points = self.dc_points
        auto_points = self.auto_points
        dc_tower_low = self.dc_tower_low
        dc_tower_mid = self.dc_tower_mid
        dc_tower_high = self.dc_tower_high
        navigated1 = self.navigated1
        navigated2 = self.navigated2
        wobble_delivered_1 = self.wobble_delivered_1
        wobble_delivered_2 = self.wobble_delivered_2
        auto_tower_low = self.auto_tower_low
        auto_tower_mid = self.auto_tower_mid
        auto_tower_high = self.auto_tower_high
        auto_tower_points = self.auto_tower_points
        auto_power_shot_left = self.auto_power_shot_left
        auto_power_shot_center = self.auto_power_shot_center
        auto_power_shot_right = self.auto_power_shot_right
        auto_power_shot_points = self.auto_power_shot_points
        wobble_rings_1 = self.wobble_rings_1
        wobble_rings_2 = self.wobble_rings_2
        wobble_end_1 = self.wobble_end_1
        wobble_end_2 = self.wobble_end_2
        wobble_end_points = self.wobble_end_points
        wobble_ring_points = self.wobble_ring_points
        auto_wobble_points = self.auto_wobble_points
        end_power_shot_left = self.end_power_shot_left
        end_power_shot_center = self.end_power_shot_center
        end_power_shot_right = self.end_power_shot_right
        end_power_shot_points = self.end_power_shot_points
        penalty_points = self.penalty_points
        major_penalties = self.major_penalties
        minor_penalties = self.minor_penalties
        navigation_points = self.navigation_points
        endgame_points = self.endgame_points
        total_points = self.total_points
        alliance = self.alliance
        team = self.team

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if adjust is not UNSET:
            field_dict["adjust"] = adjust
        if dc_points is not UNSET:
            field_dict["dcPoints"] = dc_points
        if auto_points is not UNSET:
            field_dict["autoPoints"] = auto_points
        if dc_tower_low is not UNSET:
            field_dict["dcTowerLow"] = dc_tower_low
        if dc_tower_mid is not UNSET:
            field_dict["dcTowerMid"] = dc_tower_mid
        if dc_tower_high is not UNSET:
            field_dict["dcTowerHigh"] = dc_tower_high
        if navigated1 is not UNSET:
            field_dict["navigated1"] = navigated1
        if navigated2 is not UNSET:
            field_dict["navigated2"] = navigated2
        if wobble_delivered_1 is not UNSET:
            field_dict["wobbleDelivered1"] = wobble_delivered_1
        if wobble_delivered_2 is not UNSET:
            field_dict["wobbleDelivered2"] = wobble_delivered_2
        if auto_tower_low is not UNSET:
            field_dict["autoTowerLow"] = auto_tower_low
        if auto_tower_mid is not UNSET:
            field_dict["autoTowerMid"] = auto_tower_mid
        if auto_tower_high is not UNSET:
            field_dict["autoTowerHigh"] = auto_tower_high
        if auto_tower_points is not UNSET:
            field_dict["autoTowerPoints"] = auto_tower_points
        if auto_power_shot_left is not UNSET:
            field_dict["autoPowerShotLeft"] = auto_power_shot_left
        if auto_power_shot_center is not UNSET:
            field_dict["autoPowerShotCenter"] = auto_power_shot_center
        if auto_power_shot_right is not UNSET:
            field_dict["autoPowerShotRight"] = auto_power_shot_right
        if auto_power_shot_points is not UNSET:
            field_dict["autoPowerShotPoints"] = auto_power_shot_points
        if wobble_rings_1 is not UNSET:
            field_dict["wobbleRings1"] = wobble_rings_1
        if wobble_rings_2 is not UNSET:
            field_dict["wobbleRings2"] = wobble_rings_2
        if wobble_end_1 is not UNSET:
            field_dict["wobbleEnd1"] = wobble_end_1
        if wobble_end_2 is not UNSET:
            field_dict["wobbleEnd2"] = wobble_end_2
        if wobble_end_points is not UNSET:
            field_dict["wobbleEndPoints"] = wobble_end_points
        if wobble_ring_points is not UNSET:
            field_dict["wobbleRingPoints"] = wobble_ring_points
        if auto_wobble_points is not UNSET:
            field_dict["autoWobblePoints"] = auto_wobble_points
        if end_power_shot_left is not UNSET:
            field_dict["endPowerShotLeft"] = end_power_shot_left
        if end_power_shot_center is not UNSET:
            field_dict["endPowerShotCenter"] = end_power_shot_center
        if end_power_shot_right is not UNSET:
            field_dict["endPowerShotRight"] = end_power_shot_right
        if end_power_shot_points is not UNSET:
            field_dict["endPowerShotPoints"] = end_power_shot_points
        if penalty_points is not UNSET:
            field_dict["penaltyPoints"] = penalty_points
        if major_penalties is not UNSET:
            field_dict["majorPenalties"] = major_penalties
        if minor_penalties is not UNSET:
            field_dict["minorPenalties"] = minor_penalties
        if navigation_points is not UNSET:
            field_dict["navigationPoints"] = navigation_points
        if endgame_points is not UNSET:
            field_dict["endgamePoints"] = endgame_points
        if total_points is not UNSET:
            field_dict["totalPoints"] = total_points
        if alliance is not UNSET:
            field_dict["alliance"] = alliance
        if team is not UNSET:
            field_dict["team"] = team

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        adjust = d.pop("adjust", UNSET)

        dc_points = d.pop("dcPoints", UNSET)

        auto_points = d.pop("autoPoints", UNSET)

        dc_tower_low = d.pop("dcTowerLow", UNSET)

        dc_tower_mid = d.pop("dcTowerMid", UNSET)

        dc_tower_high = d.pop("dcTowerHigh", UNSET)

        navigated1 = d.pop("navigated1", UNSET)

        navigated2 = d.pop("navigated2", UNSET)

        wobble_delivered_1 = d.pop("wobbleDelivered1", UNSET)

        wobble_delivered_2 = d.pop("wobbleDelivered2", UNSET)

        auto_tower_low = d.pop("autoTowerLow", UNSET)

        auto_tower_mid = d.pop("autoTowerMid", UNSET)

        auto_tower_high = d.pop("autoTowerHigh", UNSET)

        auto_tower_points = d.pop("autoTowerPoints", UNSET)

        auto_power_shot_left = d.pop("autoPowerShotLeft", UNSET)

        auto_power_shot_center = d.pop("autoPowerShotCenter", UNSET)

        auto_power_shot_right = d.pop("autoPowerShotRight", UNSET)

        auto_power_shot_points = d.pop("autoPowerShotPoints", UNSET)

        wobble_rings_1 = d.pop("wobbleRings1", UNSET)

        wobble_rings_2 = d.pop("wobbleRings2", UNSET)

        wobble_end_1 = d.pop("wobbleEnd1", UNSET)

        wobble_end_2 = d.pop("wobbleEnd2", UNSET)

        wobble_end_points = d.pop("wobbleEndPoints", UNSET)

        wobble_ring_points = d.pop("wobbleRingPoints", UNSET)

        auto_wobble_points = d.pop("autoWobblePoints", UNSET)

        end_power_shot_left = d.pop("endPowerShotLeft", UNSET)

        end_power_shot_center = d.pop("endPowerShotCenter", UNSET)

        end_power_shot_right = d.pop("endPowerShotRight", UNSET)

        end_power_shot_points = d.pop("endPowerShotPoints", UNSET)

        penalty_points = d.pop("penaltyPoints", UNSET)

        major_penalties = d.pop("majorPenalties", UNSET)

        minor_penalties = d.pop("minorPenalties", UNSET)

        navigation_points = d.pop("navigationPoints", UNSET)

        endgame_points = d.pop("endgamePoints", UNSET)

        total_points = d.pop("totalPoints", UNSET)

        alliance = d.pop("alliance", UNSET)

        team = d.pop("team", UNSET)

        ultimate_goal_alliance_score_breakdown = cls(
            adjust=adjust,
            dc_points=dc_points,
            auto_points=auto_points,
            dc_tower_low=dc_tower_low,
            dc_tower_mid=dc_tower_mid,
            dc_tower_high=dc_tower_high,
            navigated1=navigated1,
            navigated2=navigated2,
            wobble_delivered_1=wobble_delivered_1,
            wobble_delivered_2=wobble_delivered_2,
            auto_tower_low=auto_tower_low,
            auto_tower_mid=auto_tower_mid,
            auto_tower_high=auto_tower_high,
            auto_tower_points=auto_tower_points,
            auto_power_shot_left=auto_power_shot_left,
            auto_power_shot_center=auto_power_shot_center,
            auto_power_shot_right=auto_power_shot_right,
            auto_power_shot_points=auto_power_shot_points,
            wobble_rings_1=wobble_rings_1,
            wobble_rings_2=wobble_rings_2,
            wobble_end_1=wobble_end_1,
            wobble_end_2=wobble_end_2,
            wobble_end_points=wobble_end_points,
            wobble_ring_points=wobble_ring_points,
            auto_wobble_points=auto_wobble_points,
            end_power_shot_left=end_power_shot_left,
            end_power_shot_center=end_power_shot_center,
            end_power_shot_right=end_power_shot_right,
            end_power_shot_points=end_power_shot_points,
            penalty_points=penalty_points,
            major_penalties=major_penalties,
            minor_penalties=minor_penalties,
            navigation_points=navigation_points,
            endgame_points=endgame_points,
            total_points=total_points,
            alliance=alliance,
            team=team,
        )

        return ultimate_goal_alliance_score_breakdown
