from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.auto_navigated_status import AutoNavigatedStatus
from ..models.barcode_element import BarcodeElement
from ..models.endgame_parked_status import EndgameParkedStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="FreightFrenzyAllianceScoreBreakdown")


@attr.s(auto_attribs=True)
class FreightFrenzyAllianceScoreBreakdown:
    """
    Attributes:
        alliance (Union[Unset, None, str]):
        barcode_element_1 (Union[Unset, BarcodeElement]):
        barcode_element_2 (Union[Unset, BarcodeElement]):
        carousel (Union[Unset, bool]):
        auto_navigated_1 (Union[Unset, AutoNavigatedStatus]):
        auto_navigated_2 (Union[Unset, AutoNavigatedStatus]):
        auto_bonus_1 (Union[Unset, bool]):
        auto_bonus_2 (Union[Unset, bool]):
        auto_storage_freight (Union[Unset, int]):
        auto_freight_1 (Union[Unset, int]):
        auto_freight_2 (Union[Unset, int]):
        auto_freight_3 (Union[Unset, int]):
        driver_controlled_storage_freight (Union[Unset, int]):
        driver_controlled_freight_1 (Union[Unset, int]):
        driver_controlled_freight_2 (Union[Unset, int]):
        driver_controlled_freight_3 (Union[Unset, int]):
        shared_freight (Union[Unset, int]):
        endgame_delivered (Union[Unset, int]):
        alliance_balanced (Union[Unset, bool]):
        shared_unbalanced (Union[Unset, bool]):
        endgame_parked_1 (Union[Unset, EndgameParkedStatus]):
        endgame_parked_2 (Union[Unset, EndgameParkedStatus]):
        capped (Union[Unset, int]):
        minor_penalties (Union[Unset, int]):
        major_penalties (Union[Unset, int]):
        carousel_points (Union[Unset, int]):
        auto_navigation_points (Union[Unset, int]):
        auto_freight_points (Union[Unset, int]):
        auto_bonus_points (Union[Unset, int]):
        driver_controlled_alliance_hub_points (Union[Unset, int]):
        driver_controlled_shared_hub_points (Union[Unset, int]):
        driver_controlled_storage_points (Union[Unset, int]):
        endgame_delivery_points (Union[Unset, int]):
        alliance_balanced_points (Union[Unset, int]):
        shared_unbalanced_points (Union[Unset, int]):
        endgame_parking_points (Union[Unset, int]):
        capping_points (Union[Unset, int]):
        auto_points (Union[Unset, int]):
        driver_controlled_points (Union[Unset, int]):
        endgame_points (Union[Unset, int]):
        penalty_points (Union[Unset, int]):
        total_points (Union[Unset, int]):
    """

    alliance: Union[Unset, None, str] = UNSET
    barcode_element_1: Union[Unset, BarcodeElement] = UNSET
    barcode_element_2: Union[Unset, BarcodeElement] = UNSET
    carousel: Union[Unset, bool] = UNSET
    auto_navigated_1: Union[Unset, AutoNavigatedStatus] = UNSET
    auto_navigated_2: Union[Unset, AutoNavigatedStatus] = UNSET
    auto_bonus_1: Union[Unset, bool] = UNSET
    auto_bonus_2: Union[Unset, bool] = UNSET
    auto_storage_freight: Union[Unset, int] = UNSET
    auto_freight_1: Union[Unset, int] = UNSET
    auto_freight_2: Union[Unset, int] = UNSET
    auto_freight_3: Union[Unset, int] = UNSET
    driver_controlled_storage_freight: Union[Unset, int] = UNSET
    driver_controlled_freight_1: Union[Unset, int] = UNSET
    driver_controlled_freight_2: Union[Unset, int] = UNSET
    driver_controlled_freight_3: Union[Unset, int] = UNSET
    shared_freight: Union[Unset, int] = UNSET
    endgame_delivered: Union[Unset, int] = UNSET
    alliance_balanced: Union[Unset, bool] = UNSET
    shared_unbalanced: Union[Unset, bool] = UNSET
    endgame_parked_1: Union[Unset, EndgameParkedStatus] = UNSET
    endgame_parked_2: Union[Unset, EndgameParkedStatus] = UNSET
    capped: Union[Unset, int] = UNSET
    minor_penalties: Union[Unset, int] = UNSET
    major_penalties: Union[Unset, int] = UNSET
    carousel_points: Union[Unset, int] = UNSET
    auto_navigation_points: Union[Unset, int] = UNSET
    auto_freight_points: Union[Unset, int] = UNSET
    auto_bonus_points: Union[Unset, int] = UNSET
    driver_controlled_alliance_hub_points: Union[Unset, int] = UNSET
    driver_controlled_shared_hub_points: Union[Unset, int] = UNSET
    driver_controlled_storage_points: Union[Unset, int] = UNSET
    endgame_delivery_points: Union[Unset, int] = UNSET
    alliance_balanced_points: Union[Unset, int] = UNSET
    shared_unbalanced_points: Union[Unset, int] = UNSET
    endgame_parking_points: Union[Unset, int] = UNSET
    capping_points: Union[Unset, int] = UNSET
    auto_points: Union[Unset, int] = UNSET
    driver_controlled_points: Union[Unset, int] = UNSET
    endgame_points: Union[Unset, int] = UNSET
    penalty_points: Union[Unset, int] = UNSET
    total_points: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        alliance = self.alliance
        barcode_element_1: Union[Unset, str] = UNSET
        if not isinstance(self.barcode_element_1, Unset):
            barcode_element_1 = self.barcode_element_1.value

        barcode_element_2: Union[Unset, str] = UNSET
        if not isinstance(self.barcode_element_2, Unset):
            barcode_element_2 = self.barcode_element_2.value

        carousel = self.carousel
        auto_navigated_1: Union[Unset, str] = UNSET
        if not isinstance(self.auto_navigated_1, Unset):
            auto_navigated_1 = self.auto_navigated_1.value

        auto_navigated_2: Union[Unset, str] = UNSET
        if not isinstance(self.auto_navigated_2, Unset):
            auto_navigated_2 = self.auto_navigated_2.value

        auto_bonus_1 = self.auto_bonus_1
        auto_bonus_2 = self.auto_bonus_2
        auto_storage_freight = self.auto_storage_freight
        auto_freight_1 = self.auto_freight_1
        auto_freight_2 = self.auto_freight_2
        auto_freight_3 = self.auto_freight_3
        driver_controlled_storage_freight = self.driver_controlled_storage_freight
        driver_controlled_freight_1 = self.driver_controlled_freight_1
        driver_controlled_freight_2 = self.driver_controlled_freight_2
        driver_controlled_freight_3 = self.driver_controlled_freight_3
        shared_freight = self.shared_freight
        endgame_delivered = self.endgame_delivered
        alliance_balanced = self.alliance_balanced
        shared_unbalanced = self.shared_unbalanced
        endgame_parked_1: Union[Unset, str] = UNSET
        if not isinstance(self.endgame_parked_1, Unset):
            endgame_parked_1 = self.endgame_parked_1.value

        endgame_parked_2: Union[Unset, str] = UNSET
        if not isinstance(self.endgame_parked_2, Unset):
            endgame_parked_2 = self.endgame_parked_2.value

        capped = self.capped
        minor_penalties = self.minor_penalties
        major_penalties = self.major_penalties
        carousel_points = self.carousel_points
        auto_navigation_points = self.auto_navigation_points
        auto_freight_points = self.auto_freight_points
        auto_bonus_points = self.auto_bonus_points
        driver_controlled_alliance_hub_points = self.driver_controlled_alliance_hub_points
        driver_controlled_shared_hub_points = self.driver_controlled_shared_hub_points
        driver_controlled_storage_points = self.driver_controlled_storage_points
        endgame_delivery_points = self.endgame_delivery_points
        alliance_balanced_points = self.alliance_balanced_points
        shared_unbalanced_points = self.shared_unbalanced_points
        endgame_parking_points = self.endgame_parking_points
        capping_points = self.capping_points
        auto_points = self.auto_points
        driver_controlled_points = self.driver_controlled_points
        endgame_points = self.endgame_points
        penalty_points = self.penalty_points
        total_points = self.total_points

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if alliance is not UNSET:
            field_dict["alliance"] = alliance
        if barcode_element_1 is not UNSET:
            field_dict["barcodeElement1"] = barcode_element_1
        if barcode_element_2 is not UNSET:
            field_dict["barcodeElement2"] = barcode_element_2
        if carousel is not UNSET:
            field_dict["carousel"] = carousel
        if auto_navigated_1 is not UNSET:
            field_dict["autoNavigated1"] = auto_navigated_1
        if auto_navigated_2 is not UNSET:
            field_dict["autoNavigated2"] = auto_navigated_2
        if auto_bonus_1 is not UNSET:
            field_dict["autoBonus1"] = auto_bonus_1
        if auto_bonus_2 is not UNSET:
            field_dict["autoBonus2"] = auto_bonus_2
        if auto_storage_freight is not UNSET:
            field_dict["autoStorageFreight"] = auto_storage_freight
        if auto_freight_1 is not UNSET:
            field_dict["autoFreight1"] = auto_freight_1
        if auto_freight_2 is not UNSET:
            field_dict["autoFreight2"] = auto_freight_2
        if auto_freight_3 is not UNSET:
            field_dict["autoFreight3"] = auto_freight_3
        if driver_controlled_storage_freight is not UNSET:
            field_dict["driverControlledStorageFreight"] = driver_controlled_storage_freight
        if driver_controlled_freight_1 is not UNSET:
            field_dict["driverControlledFreight1"] = driver_controlled_freight_1
        if driver_controlled_freight_2 is not UNSET:
            field_dict["driverControlledFreight2"] = driver_controlled_freight_2
        if driver_controlled_freight_3 is not UNSET:
            field_dict["driverControlledFreight3"] = driver_controlled_freight_3
        if shared_freight is not UNSET:
            field_dict["sharedFreight"] = shared_freight
        if endgame_delivered is not UNSET:
            field_dict["endgameDelivered"] = endgame_delivered
        if alliance_balanced is not UNSET:
            field_dict["allianceBalanced"] = alliance_balanced
        if shared_unbalanced is not UNSET:
            field_dict["sharedUnbalanced"] = shared_unbalanced
        if endgame_parked_1 is not UNSET:
            field_dict["endgameParked1"] = endgame_parked_1
        if endgame_parked_2 is not UNSET:
            field_dict["endgameParked2"] = endgame_parked_2
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
            field_dict["driverControlledAllianceHubPoints"] = driver_controlled_alliance_hub_points
        if driver_controlled_shared_hub_points is not UNSET:
            field_dict["driverControlledSharedHubPoints"] = driver_controlled_shared_hub_points
        if driver_controlled_storage_points is not UNSET:
            field_dict["driverControlledStoragePoints"] = driver_controlled_storage_points
        if endgame_delivery_points is not UNSET:
            field_dict["endgameDeliveryPoints"] = endgame_delivery_points
        if alliance_balanced_points is not UNSET:
            field_dict["allianceBalancedPoints"] = alliance_balanced_points
        if shared_unbalanced_points is not UNSET:
            field_dict["sharedUnbalancedPoints"] = shared_unbalanced_points
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
        alliance = d.pop("alliance", UNSET)

        _barcode_element_1 = d.pop("barcodeElement1", UNSET)
        barcode_element_1: Union[Unset, BarcodeElement]
        if isinstance(_barcode_element_1, Unset):
            barcode_element_1 = UNSET
        else:
            barcode_element_1 = BarcodeElement(_barcode_element_1)

        _barcode_element_2 = d.pop("barcodeElement2", UNSET)
        barcode_element_2: Union[Unset, BarcodeElement]
        if isinstance(_barcode_element_2, Unset):
            barcode_element_2 = UNSET
        else:
            barcode_element_2 = BarcodeElement(_barcode_element_2)

        carousel = d.pop("carousel", UNSET)

        _auto_navigated_1 = d.pop("autoNavigated1", UNSET)
        auto_navigated_1: Union[Unset, AutoNavigatedStatus]
        if isinstance(_auto_navigated_1, Unset):
            auto_navigated_1 = UNSET
        else:
            auto_navigated_1 = AutoNavigatedStatus(_auto_navigated_1)

        _auto_navigated_2 = d.pop("autoNavigated2", UNSET)
        auto_navigated_2: Union[Unset, AutoNavigatedStatus]
        if isinstance(_auto_navigated_2, Unset):
            auto_navigated_2 = UNSET
        else:
            auto_navigated_2 = AutoNavigatedStatus(_auto_navigated_2)

        auto_bonus_1 = d.pop("autoBonus1", UNSET)

        auto_bonus_2 = d.pop("autoBonus2", UNSET)

        auto_storage_freight = d.pop("autoStorageFreight", UNSET)

        auto_freight_1 = d.pop("autoFreight1", UNSET)

        auto_freight_2 = d.pop("autoFreight2", UNSET)

        auto_freight_3 = d.pop("autoFreight3", UNSET)

        driver_controlled_storage_freight = d.pop("driverControlledStorageFreight", UNSET)

        driver_controlled_freight_1 = d.pop("driverControlledFreight1", UNSET)

        driver_controlled_freight_2 = d.pop("driverControlledFreight2", UNSET)

        driver_controlled_freight_3 = d.pop("driverControlledFreight3", UNSET)

        shared_freight = d.pop("sharedFreight", UNSET)

        endgame_delivered = d.pop("endgameDelivered", UNSET)

        alliance_balanced = d.pop("allianceBalanced", UNSET)

        shared_unbalanced = d.pop("sharedUnbalanced", UNSET)

        _endgame_parked_1 = d.pop("endgameParked1", UNSET)
        endgame_parked_1: Union[Unset, EndgameParkedStatus]
        if isinstance(_endgame_parked_1, Unset):
            endgame_parked_1 = UNSET
        else:
            endgame_parked_1 = EndgameParkedStatus(_endgame_parked_1)

        _endgame_parked_2 = d.pop("endgameParked2", UNSET)
        endgame_parked_2: Union[Unset, EndgameParkedStatus]
        if isinstance(_endgame_parked_2, Unset):
            endgame_parked_2 = UNSET
        else:
            endgame_parked_2 = EndgameParkedStatus(_endgame_parked_2)

        capped = d.pop("capped", UNSET)

        minor_penalties = d.pop("minorPenalties", UNSET)

        major_penalties = d.pop("majorPenalties", UNSET)

        carousel_points = d.pop("carouselPoints", UNSET)

        auto_navigation_points = d.pop("autoNavigationPoints", UNSET)

        auto_freight_points = d.pop("autoFreightPoints", UNSET)

        auto_bonus_points = d.pop("autoBonusPoints", UNSET)

        driver_controlled_alliance_hub_points = d.pop("driverControlledAllianceHubPoints", UNSET)

        driver_controlled_shared_hub_points = d.pop("driverControlledSharedHubPoints", UNSET)

        driver_controlled_storage_points = d.pop("driverControlledStoragePoints", UNSET)

        endgame_delivery_points = d.pop("endgameDeliveryPoints", UNSET)

        alliance_balanced_points = d.pop("allianceBalancedPoints", UNSET)

        shared_unbalanced_points = d.pop("sharedUnbalancedPoints", UNSET)

        endgame_parking_points = d.pop("endgameParkingPoints", UNSET)

        capping_points = d.pop("cappingPoints", UNSET)

        auto_points = d.pop("autoPoints", UNSET)

        driver_controlled_points = d.pop("driverControlledPoints", UNSET)

        endgame_points = d.pop("endgamePoints", UNSET)

        penalty_points = d.pop("penaltyPoints", UNSET)

        total_points = d.pop("totalPoints", UNSET)

        freight_frenzy_alliance_score_breakdown = cls(
            alliance=alliance,
            barcode_element_1=barcode_element_1,
            barcode_element_2=barcode_element_2,
            carousel=carousel,
            auto_navigated_1=auto_navigated_1,
            auto_navigated_2=auto_navigated_2,
            auto_bonus_1=auto_bonus_1,
            auto_bonus_2=auto_bonus_2,
            auto_storage_freight=auto_storage_freight,
            auto_freight_1=auto_freight_1,
            auto_freight_2=auto_freight_2,
            auto_freight_3=auto_freight_3,
            driver_controlled_storage_freight=driver_controlled_storage_freight,
            driver_controlled_freight_1=driver_controlled_freight_1,
            driver_controlled_freight_2=driver_controlled_freight_2,
            driver_controlled_freight_3=driver_controlled_freight_3,
            shared_freight=shared_freight,
            endgame_delivered=endgame_delivered,
            alliance_balanced=alliance_balanced,
            shared_unbalanced=shared_unbalanced,
            endgame_parked_1=endgame_parked_1,
            endgame_parked_2=endgame_parked_2,
            capped=capped,
            minor_penalties=minor_penalties,
            major_penalties=major_penalties,
            carousel_points=carousel_points,
            auto_navigation_points=auto_navigation_points,
            auto_freight_points=auto_freight_points,
            auto_bonus_points=auto_bonus_points,
            driver_controlled_alliance_hub_points=driver_controlled_alliance_hub_points,
            driver_controlled_shared_hub_points=driver_controlled_shared_hub_points,
            driver_controlled_storage_points=driver_controlled_storage_points,
            endgame_delivery_points=endgame_delivery_points,
            alliance_balanced_points=alliance_balanced_points,
            shared_unbalanced_points=shared_unbalanced_points,
            endgame_parking_points=endgame_parking_points,
            capping_points=capping_points,
            auto_points=auto_points,
            driver_controlled_points=driver_controlled_points,
            endgame_points=endgame_points,
            penalty_points=penalty_points,
            total_points=total_points,
        )

        return freight_frenzy_alliance_score_breakdown
