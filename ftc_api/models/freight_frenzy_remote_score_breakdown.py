from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.auto_navigated_status import AutoNavigatedStatus
from ..models.barcode_element import BarcodeElement
from ..models.endgame_parked_status import EndgameParkedStatus
from ftc_api.types import UNSET, Unset

T = TypeVar("T", bound="FreightFrenzyRemoteScoreBreakdown")


@attr.s(auto_attribs=True)
class FreightFrenzyRemoteScoreBreakdown:
    """
    Attributes:
        barcode_element (Union[Unset, BarcodeElement]):
        carousel (Union[Unset, bool]):
        auto_navigated (Union[Unset, AutoNavigatedStatus]):
        auto_bonus (Union[Unset, bool]):
        auto_storage_freight (Union[Unset, int]):
        auto_freight_1 (Union[Unset, int]):
        auto_freight_2 (Union[Unset, int]):
        auto_freight_3 (Union[Unset, int]):
        driver_controlled_storage_freight (Union[Unset, int]):
        driver_controlled_freight_1 (Union[Unset, int]):
        driver_controlled_freight_2 (Union[Unset, int]):
        driver_controlled_freight_3 (Union[Unset, int]):
        endgame_delivered (Union[Unset, int]):
        alliance_balanced (Union[Unset, bool]):
        endgame_parked (Union[Unset, EndgameParkedStatus]):
        capped (Union[Unset, int]):
        minor_penalties (Union[Unset, int]):
        major_penalties (Union[Unset, int]):
        carousel_points (Union[Unset, int]):
        auto_navigation_points (Union[Unset, int]):
        auto_freight_points (Union[Unset, int]):
        auto_bonus_points (Union[Unset, int]):
        driver_controlled_alliance_hub_points (Union[Unset, int]):
        driver_controlled_storage_points (Union[Unset, int]):
        endgame_delivery_points (Union[Unset, int]):
        alliance_balanced_points (Union[Unset, int]):
        endgame_parking_points (Union[Unset, int]):
        capping_points (Union[Unset, int]):
        auto_points (Union[Unset, int]):
        driver_controlled_points (Union[Unset, int]):
        endgame_points (Union[Unset, int]):
        penalty_points (Union[Unset, int]):
        total_points (Union[Unset, int]):
    """

    barcode_element: Union[Unset, BarcodeElement] = UNSET
    carousel: Union[Unset, bool] = UNSET
    auto_navigated: Union[Unset, AutoNavigatedStatus] = UNSET
    auto_bonus: Union[Unset, bool] = UNSET
    auto_storage_freight: Union[Unset, int] = UNSET
    auto_freight_1: Union[Unset, int] = UNSET
    auto_freight_2: Union[Unset, int] = UNSET
    auto_freight_3: Union[Unset, int] = UNSET
    driver_controlled_storage_freight: Union[Unset, int] = UNSET
    driver_controlled_freight_1: Union[Unset, int] = UNSET
    driver_controlled_freight_2: Union[Unset, int] = UNSET
    driver_controlled_freight_3: Union[Unset, int] = UNSET
    endgame_delivered: Union[Unset, int] = UNSET
    alliance_balanced: Union[Unset, bool] = UNSET
    endgame_parked: Union[Unset, EndgameParkedStatus] = UNSET
    capped: Union[Unset, int] = UNSET
    minor_penalties: Union[Unset, int] = UNSET
    major_penalties: Union[Unset, int] = UNSET
    carousel_points: Union[Unset, int] = UNSET
    auto_navigation_points: Union[Unset, int] = UNSET
    auto_freight_points: Union[Unset, int] = UNSET
    auto_bonus_points: Union[Unset, int] = UNSET
    driver_controlled_alliance_hub_points: Union[Unset, int] = UNSET
    driver_controlled_storage_points: Union[Unset, int] = UNSET
    endgame_delivery_points: Union[Unset, int] = UNSET
    alliance_balanced_points: Union[Unset, int] = UNSET
    endgame_parking_points: Union[Unset, int] = UNSET
    capping_points: Union[Unset, int] = UNSET
    auto_points: Union[Unset, int] = UNSET
    driver_controlled_points: Union[Unset, int] = UNSET
    endgame_points: Union[Unset, int] = UNSET
    penalty_points: Union[Unset, int] = UNSET
    total_points: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        barcode_element: Union[Unset, str] = UNSET
        if not isinstance(self.barcode_element, Unset):
            barcode_element = self.barcode_element.value

        carousel = self.carousel
        auto_navigated: Union[Unset, str] = UNSET
        if not isinstance(self.auto_navigated, Unset):
            auto_navigated = self.auto_navigated.value

        auto_bonus = self.auto_bonus
        auto_storage_freight = self.auto_storage_freight
        auto_freight_1 = self.auto_freight_1
        auto_freight_2 = self.auto_freight_2
        auto_freight_3 = self.auto_freight_3
        driver_controlled_storage_freight = self.driver_controlled_storage_freight
        driver_controlled_freight_1 = self.driver_controlled_freight_1
        driver_controlled_freight_2 = self.driver_controlled_freight_2
        driver_controlled_freight_3 = self.driver_controlled_freight_3
        endgame_delivered = self.endgame_delivered
        alliance_balanced = self.alliance_balanced
        endgame_parked: Union[Unset, str] = UNSET
        if not isinstance(self.endgame_parked, Unset):
            endgame_parked = self.endgame_parked.value

        capped = self.capped
        minor_penalties = self.minor_penalties
        major_penalties = self.major_penalties
        carousel_points = self.carousel_points
        auto_navigation_points = self.auto_navigation_points
        auto_freight_points = self.auto_freight_points
        auto_bonus_points = self.auto_bonus_points
        driver_controlled_alliance_hub_points = (
            self.driver_controlled_alliance_hub_points
        )
        driver_controlled_storage_points = self.driver_controlled_storage_points
        endgame_delivery_points = self.endgame_delivery_points
        alliance_balanced_points = self.alliance_balanced_points
        endgame_parking_points = self.endgame_parking_points
        capping_points = self.capping_points
        auto_points = self.auto_points
        driver_controlled_points = self.driver_controlled_points
        endgame_points = self.endgame_points
        penalty_points = self.penalty_points
        total_points = self.total_points

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if barcode_element is not UNSET:
            field_dict["barcodeElement"] = barcode_element
        if carousel is not UNSET:
            field_dict["carousel"] = carousel
        if auto_navigated is not UNSET:
            field_dict["autoNavigated"] = auto_navigated
        if auto_bonus is not UNSET:
            field_dict["autoBonus"] = auto_bonus
        if auto_storage_freight is not UNSET:
            field_dict["autoStorageFreight"] = auto_storage_freight
        if auto_freight_1 is not UNSET:
            field_dict["autoFreight1"] = auto_freight_1
        if auto_freight_2 is not UNSET:
            field_dict["autoFreight2"] = auto_freight_2
        if auto_freight_3 is not UNSET:
            field_dict["autoFreight3"] = auto_freight_3
        if driver_controlled_storage_freight is not UNSET:
            field_dict[
                "driverControlledStorageFreight"
            ] = driver_controlled_storage_freight
        if driver_controlled_freight_1 is not UNSET:
            field_dict["driverControlledFreight1"] = driver_controlled_freight_1
        if driver_controlled_freight_2 is not UNSET:
            field_dict["driverControlledFreight2"] = driver_controlled_freight_2
        if driver_controlled_freight_3 is not UNSET:
            field_dict["driverControlledFreight3"] = driver_controlled_freight_3
        if endgame_delivered is not UNSET:
            field_dict["endgameDelivered"] = endgame_delivered
        if alliance_balanced is not UNSET:
            field_dict["allianceBalanced"] = alliance_balanced
        if endgame_parked is not UNSET:
            field_dict["endgameParked"] = endgame_parked
        if capped is not UNSET:
            field_dict["capped"] = capped
        if minor_penalties is not UNSET:
            field_dict["minorPenalties"] = minor_penalties
        if major_penalties is not UNSET:
            field_dict["majorPenalties"] = major_penalties
        if carousel_points is not UNSET:
            field_dict["carouselPoints"] = carousel_points
        if auto_navigation_points is not UNSET:
            field_dict["autoNavigationPoints"] = auto_navigation_points
        if auto_freight_points is not UNSET:
            field_dict["autoFreightPoints"] = auto_freight_points
        if auto_bonus_points is not UNSET:
            field_dict["autoBonusPoints"] = auto_bonus_points
        if driver_controlled_alliance_hub_points is not UNSET:
            field_dict[
                "driverControlledAllianceHubPoints"
            ] = driver_controlled_alliance_hub_points
        if driver_controlled_storage_points is not UNSET:
            field_dict[
                "driverControlledStoragePoints"
            ] = driver_controlled_storage_points
        if endgame_delivery_points is not UNSET:
            field_dict["endgameDeliveryPoints"] = endgame_delivery_points
        if alliance_balanced_points is not UNSET:
            field_dict["allianceBalancedPoints"] = alliance_balanced_points
        if endgame_parking_points is not UNSET:
            field_dict["endgameParkingPoints"] = endgame_parking_points
        if capping_points is not UNSET:
            field_dict["cappingPoints"] = capping_points
        if auto_points is not UNSET:
            field_dict["autoPoints"] = auto_points
        if driver_controlled_points is not UNSET:
            field_dict["driverControlledPoints"] = driver_controlled_points
        if endgame_points is not UNSET:
            field_dict["endgamePoints"] = endgame_points
        if penalty_points is not UNSET:
            field_dict["penaltyPoints"] = penalty_points
        if total_points is not UNSET:
            field_dict["totalPoints"] = total_points

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _barcode_element = d.pop("barcodeElement", UNSET)
        barcode_element: Union[Unset, BarcodeElement]
        if isinstance(_barcode_element, Unset):
            barcode_element = UNSET
        else:
            barcode_element = BarcodeElement(_barcode_element)

        carousel = d.pop("carousel", UNSET)

        _auto_navigated = d.pop("autoNavigated", UNSET)
        auto_navigated: Union[Unset, AutoNavigatedStatus]
        if isinstance(_auto_navigated, Unset):
            auto_navigated = UNSET
        else:
            auto_navigated = AutoNavigatedStatus(_auto_navigated)

        auto_bonus = d.pop("autoBonus", UNSET)

        auto_storage_freight = d.pop("autoStorageFreight", UNSET)

        auto_freight_1 = d.pop("autoFreight1", UNSET)

        auto_freight_2 = d.pop("autoFreight2", UNSET)

        auto_freight_3 = d.pop("autoFreight3", UNSET)

        driver_controlled_storage_freight = d.pop(
            "driverControlledStorageFreight", UNSET
        )

        driver_controlled_freight_1 = d.pop("driverControlledFreight1", UNSET)

        driver_controlled_freight_2 = d.pop("driverControlledFreight2", UNSET)

        driver_controlled_freight_3 = d.pop("driverControlledFreight3", UNSET)

        endgame_delivered = d.pop("endgameDelivered", UNSET)

        alliance_balanced = d.pop("allianceBalanced", UNSET)

        _endgame_parked = d.pop("endgameParked", UNSET)
        endgame_parked: Union[Unset, EndgameParkedStatus]
        if isinstance(_endgame_parked, Unset):
            endgame_parked = UNSET
        else:
            endgame_parked = EndgameParkedStatus(_endgame_parked)

        capped = d.pop("capped", UNSET)

        minor_penalties = d.pop("minorPenalties", UNSET)

        major_penalties = d.pop("majorPenalties", UNSET)

        carousel_points = d.pop("carouselPoints", UNSET)

        auto_navigation_points = d.pop("autoNavigationPoints", UNSET)

        auto_freight_points = d.pop("autoFreightPoints", UNSET)

        auto_bonus_points = d.pop("autoBonusPoints", UNSET)

        driver_controlled_alliance_hub_points = d.pop(
            "driverControlledAllianceHubPoints", UNSET
        )

        driver_controlled_storage_points = d.pop("driverControlledStoragePoints", UNSET)

        endgame_delivery_points = d.pop("endgameDeliveryPoints", UNSET)

        alliance_balanced_points = d.pop("allianceBalancedPoints", UNSET)

        endgame_parking_points = d.pop("endgameParkingPoints", UNSET)

        capping_points = d.pop("cappingPoints", UNSET)

        auto_points = d.pop("autoPoints", UNSET)

        driver_controlled_points = d.pop("driverControlledPoints", UNSET)

        endgame_points = d.pop("endgamePoints", UNSET)

        penalty_points = d.pop("penaltyPoints", UNSET)

        total_points = d.pop("totalPoints", UNSET)

        freight_frenzy_remote_score_breakdown = cls(
            barcode_element=barcode_element,
            carousel=carousel,
            auto_navigated=auto_navigated,
            auto_bonus=auto_bonus,
            auto_storage_freight=auto_storage_freight,
            auto_freight_1=auto_freight_1,
            auto_freight_2=auto_freight_2,
            auto_freight_3=auto_freight_3,
            driver_controlled_storage_freight=driver_controlled_storage_freight,
            driver_controlled_freight_1=driver_controlled_freight_1,
            driver_controlled_freight_2=driver_controlled_freight_2,
            driver_controlled_freight_3=driver_controlled_freight_3,
            endgame_delivered=endgame_delivered,
            alliance_balanced=alliance_balanced,
            endgame_parked=endgame_parked,
            capped=capped,
            minor_penalties=minor_penalties,
            major_penalties=major_penalties,
            carousel_points=carousel_points,
            auto_navigation_points=auto_navigation_points,
            auto_freight_points=auto_freight_points,
            auto_bonus_points=auto_bonus_points,
            driver_controlled_alliance_hub_points=driver_controlled_alliance_hub_points,
            driver_controlled_storage_points=driver_controlled_storage_points,
            endgame_delivery_points=endgame_delivery_points,
            alliance_balanced_points=alliance_balanced_points,
            endgame_parking_points=endgame_parking_points,
            capping_points=capping_points,
            auto_points=auto_points,
            driver_controlled_points=driver_controlled_points,
            endgame_points=endgame_points,
            penalty_points=penalty_points,
            total_points=total_points,
        )

        return freight_frenzy_remote_score_breakdown
