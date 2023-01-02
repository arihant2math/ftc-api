from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.stone import Stone
from .._types import UNSET, Unset

T = TypeVar("T", bound="SkyStoneAllianceScoreDetails")


@attr.s(auto_attribs=True)
class SkyStoneAllianceScoreDetails:
    """
    Attributes:
        alliance (Union[Unset, None, str]):
        robot_1_navigated (Union[Unset, bool]):
        robot_1_parked (Union[Unset, bool]):
        robot_1_capstone_level (Union[Unset, int]):
        robot_2_navigated (Union[Unset, bool]):
        robot_2_parked (Union[Unset, bool]):
        robot_2_capstone_level (Union[Unset, int]):
        auto_stones (Union[Unset, None, List[Stone]]):
        auto_delivered (Union[Unset, int]):
        auto_returned (Union[Unset, int]):
        first_returned_is_skystone (Union[Unset, bool]):
        auto_placed (Union[Unset, int]):
        foundation_repositioned (Union[Unset, bool]):
        foundation_moved (Union[Unset, bool]):
        driver_controlled_delivered (Union[Unset, int]):
        driver_controlled_returned (Union[Unset, int]):
        driver_controlled_placed (Union[Unset, int]):
        tallest_skyscraper (Union[Unset, int]):
        auto_delivery_points (Union[Unset, int]):
        auto_placed_points (Union[Unset, int]):
        autonomous_points (Union[Unset, int]):
        repositioned_points (Union[Unset, int]):
        navigation_points (Union[Unset, int]):
        driver_controlled_delivery_points (Union[Unset, int]):
        driver_controlled_placed_points (Union[Unset, int]):
        skyscraper_bonus_points (Union[Unset, int]):
        capstone_points (Union[Unset, int]):
        driver_controlled_points (Union[Unset, int]):
        parking_points (Union[Unset, int]):
        end_game_points (Union[Unset, int]):
        minor_penalties (Union[Unset, int]):
        major_penalties (Union[Unset, int]):
        penalty_points (Union[Unset, int]):
        total_points (Union[Unset, int]):
    """

    alliance: Union[Unset, None, str] = UNSET
    robot_1_navigated: Union[Unset, bool] = UNSET
    robot_1_parked: Union[Unset, bool] = UNSET
    robot_1_capstone_level: Union[Unset, int] = UNSET
    robot_2_navigated: Union[Unset, bool] = UNSET
    robot_2_parked: Union[Unset, bool] = UNSET
    robot_2_capstone_level: Union[Unset, int] = UNSET
    auto_stones: Union[Unset, None, List[Stone]] = UNSET
    auto_delivered: Union[Unset, int] = UNSET
    auto_returned: Union[Unset, int] = UNSET
    first_returned_is_skystone: Union[Unset, bool] = UNSET
    auto_placed: Union[Unset, int] = UNSET
    foundation_repositioned: Union[Unset, bool] = UNSET
    foundation_moved: Union[Unset, bool] = UNSET
    driver_controlled_delivered: Union[Unset, int] = UNSET
    driver_controlled_returned: Union[Unset, int] = UNSET
    driver_controlled_placed: Union[Unset, int] = UNSET
    tallest_skyscraper: Union[Unset, int] = UNSET
    auto_delivery_points: Union[Unset, int] = UNSET
    auto_placed_points: Union[Unset, int] = UNSET
    autonomous_points: Union[Unset, int] = UNSET
    repositioned_points: Union[Unset, int] = UNSET
    navigation_points: Union[Unset, int] = UNSET
    driver_controlled_delivery_points: Union[Unset, int] = UNSET
    driver_controlled_placed_points: Union[Unset, int] = UNSET
    skyscraper_bonus_points: Union[Unset, int] = UNSET
    capstone_points: Union[Unset, int] = UNSET
    driver_controlled_points: Union[Unset, int] = UNSET
    parking_points: Union[Unset, int] = UNSET
    end_game_points: Union[Unset, int] = UNSET
    minor_penalties: Union[Unset, int] = UNSET
    major_penalties: Union[Unset, int] = UNSET
    penalty_points: Union[Unset, int] = UNSET
    total_points: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        alliance = self.alliance
        robot_1_navigated = self.robot_1_navigated
        robot_1_parked = self.robot_1_parked
        robot_1_capstone_level = self.robot_1_capstone_level
        robot_2_navigated = self.robot_2_navigated
        robot_2_parked = self.robot_2_parked
        robot_2_capstone_level = self.robot_2_capstone_level
        auto_stones: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.auto_stones, Unset):
            if self.auto_stones is None:
                auto_stones = None
            else:
                auto_stones = []
                for auto_stones_item_data in self.auto_stones:
                    auto_stones_item = auto_stones_item_data.value

                    auto_stones.append(auto_stones_item)

        auto_delivered = self.auto_delivered
        auto_returned = self.auto_returned
        first_returned_is_skystone = self.first_returned_is_skystone
        auto_placed = self.auto_placed
        foundation_repositioned = self.foundation_repositioned
        foundation_moved = self.foundation_moved
        driver_controlled_delivered = self.driver_controlled_delivered
        driver_controlled_returned = self.driver_controlled_returned
        driver_controlled_placed = self.driver_controlled_placed
        tallest_skyscraper = self.tallest_skyscraper
        auto_delivery_points = self.auto_delivery_points
        auto_placed_points = self.auto_placed_points
        autonomous_points = self.autonomous_points
        repositioned_points = self.repositioned_points
        navigation_points = self.navigation_points
        driver_controlled_delivery_points = self.driver_controlled_delivery_points
        driver_controlled_placed_points = self.driver_controlled_placed_points
        skyscraper_bonus_points = self.skyscraper_bonus_points
        capstone_points = self.capstone_points
        driver_controlled_points = self.driver_controlled_points
        parking_points = self.parking_points
        end_game_points = self.end_game_points
        minor_penalties = self.minor_penalties
        major_penalties = self.major_penalties
        penalty_points = self.penalty_points
        total_points = self.total_points

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if alliance is not UNSET:
            field_dict["alliance"] = alliance
        if robot_1_navigated is not UNSET:
            field_dict["robot1Navigated"] = robot_1_navigated
        if robot_1_parked is not UNSET:
            field_dict["robot1Parked"] = robot_1_parked
        if robot_1_capstone_level is not UNSET:
            field_dict["robot1CapstoneLevel"] = robot_1_capstone_level
        if robot_2_navigated is not UNSET:
            field_dict["robot2Navigated"] = robot_2_navigated
        if robot_2_parked is not UNSET:
            field_dict["robot2Parked"] = robot_2_parked
        if robot_2_capstone_level is not UNSET:
            field_dict["robot2CapstoneLevel"] = robot_2_capstone_level
        if auto_stones is not UNSET:
            field_dict["autoStones"] = auto_stones
        if auto_delivered is not UNSET:
            field_dict["autoDelivered"] = auto_delivered
        if auto_returned is not UNSET:
            field_dict["autoReturned"] = auto_returned
        if first_returned_is_skystone is not UNSET:
            field_dict["firstReturnedIsSkystone"] = first_returned_is_skystone
        if auto_placed is not UNSET:
            field_dict["autoPlaced"] = auto_placed
        if foundation_repositioned is not UNSET:
            field_dict["foundationRepositioned"] = foundation_repositioned
        if foundation_moved is not UNSET:
            field_dict["foundationMoved"] = foundation_moved
        if driver_controlled_delivered is not UNSET:
            field_dict["driverControlledDelivered"] = driver_controlled_delivered
        if driver_controlled_returned is not UNSET:
            field_dict["driverControlledReturned"] = driver_controlled_returned
        if driver_controlled_placed is not UNSET:
            field_dict["driverControlledPlaced"] = driver_controlled_placed
        if tallest_skyscraper is not UNSET:
            field_dict["tallestSkyscraper"] = tallest_skyscraper
        if auto_delivery_points is not UNSET:
            field_dict["autoDeliveryPoints"] = auto_delivery_points
        if auto_placed_points is not UNSET:
            field_dict["autoPlacedPoints"] = auto_placed_points
        if autonomous_points is not UNSET:
            field_dict["autonomousPoints"] = autonomous_points
        if repositioned_points is not UNSET:
            field_dict["repositionedPoints"] = repositioned_points
        if navigation_points is not UNSET:
            field_dict["navigationPoints"] = navigation_points
        if driver_controlled_delivery_points is not UNSET:
            field_dict["driverControlledDeliveryPoints"] = driver_controlled_delivery_points
        if driver_controlled_placed_points is not UNSET:
            field_dict["driverControlledPlacedPoints"] = driver_controlled_placed_points
        if skyscraper_bonus_points is not UNSET:
            field_dict["skyscraperBonusPoints"] = skyscraper_bonus_points
        if capstone_points is not UNSET:
            field_dict["capstonePoints"] = capstone_points
        if driver_controlled_points is not UNSET:
            field_dict["driverControlledPoints"] = driver_controlled_points
        if parking_points is not UNSET:
            field_dict["parkingPoints"] = parking_points
        if end_game_points is not UNSET:
            field_dict["endGamePoints"] = end_game_points
        if minor_penalties is not UNSET:
            field_dict["minorPenalties"] = minor_penalties
        if major_penalties is not UNSET:
            field_dict["majorPenalties"] = major_penalties
        if penalty_points is not UNSET:
            field_dict["penaltyPoints"] = penalty_points
        if total_points is not UNSET:
            field_dict["totalPoints"] = total_points

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        alliance = d.pop("alliance", UNSET)

        robot_1_navigated = d.pop("robot1Navigated", UNSET)

        robot_1_parked = d.pop("robot1Parked", UNSET)

        robot_1_capstone_level = d.pop("robot1CapstoneLevel", UNSET)

        robot_2_navigated = d.pop("robot2Navigated", UNSET)

        robot_2_parked = d.pop("robot2Parked", UNSET)

        robot_2_capstone_level = d.pop("robot2CapstoneLevel", UNSET)

        auto_stones = []
        _auto_stones = d.pop("autoStones", UNSET)
        for auto_stones_item_data in _auto_stones or []:
            auto_stones_item = Stone(auto_stones_item_data)

            auto_stones.append(auto_stones_item)

        auto_delivered = d.pop("autoDelivered", UNSET)

        auto_returned = d.pop("autoReturned", UNSET)

        first_returned_is_skystone = d.pop("firstReturnedIsSkystone", UNSET)

        auto_placed = d.pop("autoPlaced", UNSET)

        foundation_repositioned = d.pop("foundationRepositioned", UNSET)

        foundation_moved = d.pop("foundationMoved", UNSET)

        driver_controlled_delivered = d.pop("driverControlledDelivered", UNSET)

        driver_controlled_returned = d.pop("driverControlledReturned", UNSET)

        driver_controlled_placed = d.pop("driverControlledPlaced", UNSET)

        tallest_skyscraper = d.pop("tallestSkyscraper", UNSET)

        auto_delivery_points = d.pop("autoDeliveryPoints", UNSET)

        auto_placed_points = d.pop("autoPlacedPoints", UNSET)

        autonomous_points = d.pop("autonomousPoints", UNSET)

        repositioned_points = d.pop("repositionedPoints", UNSET)

        navigation_points = d.pop("navigationPoints", UNSET)

        driver_controlled_delivery_points = d.pop("driverControlledDeliveryPoints", UNSET)

        driver_controlled_placed_points = d.pop("driverControlledPlacedPoints", UNSET)

        skyscraper_bonus_points = d.pop("skyscraperBonusPoints", UNSET)

        capstone_points = d.pop("capstonePoints", UNSET)

        driver_controlled_points = d.pop("driverControlledPoints", UNSET)

        parking_points = d.pop("parkingPoints", UNSET)

        end_game_points = d.pop("endGamePoints", UNSET)

        minor_penalties = d.pop("minorPenalties", UNSET)

        major_penalties = d.pop("majorPenalties", UNSET)

        penalty_points = d.pop("penaltyPoints", UNSET)

        total_points = d.pop("totalPoints", UNSET)

        sky_stone_alliance_score_details = cls(
            alliance=alliance,
            robot_1_navigated=robot_1_navigated,
            robot_1_parked=robot_1_parked,
            robot_1_capstone_level=robot_1_capstone_level,
            robot_2_navigated=robot_2_navigated,
            robot_2_parked=robot_2_parked,
            robot_2_capstone_level=robot_2_capstone_level,
            auto_stones=auto_stones,
            auto_delivered=auto_delivered,
            auto_returned=auto_returned,
            first_returned_is_skystone=first_returned_is_skystone,
            auto_placed=auto_placed,
            foundation_repositioned=foundation_repositioned,
            foundation_moved=foundation_moved,
            driver_controlled_delivered=driver_controlled_delivered,
            driver_controlled_returned=driver_controlled_returned,
            driver_controlled_placed=driver_controlled_placed,
            tallest_skyscraper=tallest_skyscraper,
            auto_delivery_points=auto_delivery_points,
            auto_placed_points=auto_placed_points,
            autonomous_points=autonomous_points,
            repositioned_points=repositioned_points,
            navigation_points=navigation_points,
            driver_controlled_delivery_points=driver_controlled_delivery_points,
            driver_controlled_placed_points=driver_controlled_placed_points,
            skyscraper_bonus_points=skyscraper_bonus_points,
            capstone_points=capstone_points,
            driver_controlled_points=driver_controlled_points,
            parking_points=parking_points,
            end_game_points=end_game_points,
            minor_penalties=minor_penalties,
            major_penalties=major_penalties,
            penalty_points=penalty_points,
            total_points=total_points,
        )

        return sky_stone_alliance_score_details
