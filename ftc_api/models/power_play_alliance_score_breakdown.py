from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.auto_navigation import AutoNavigation
from ..models.field_side import FieldSide
from ..models.junction_element import JunctionElement
from ftc_api.types import UNSET, Unset

T = TypeVar("T", bound="PowerPlayAllianceScoreBreakdown")


@attr.s(auto_attribs=True)
class PowerPlayAllianceScoreBreakdown:
    """
    Attributes:
        side_of_field (Union[Unset, FieldSide]):
        init_signal_sleeve_1 (Union[Unset, bool]):
        init_signal_sleeve_2 (Union[Unset, bool]):
        robot_1_auto (Union[Unset, AutoNavigation]):
        robot_2_auto (Union[Unset, AutoNavigation]):
        auto_terminal (Union[Unset, int]):
        auto_junctions (Union[Unset, None, List[List[List[JunctionElement]]]]): Two dimensional array of lists of items
            scored on junctions in autonomous. [0,0] is the upper-left corner of the field as viewed from the audience side
            of the field (V5). The array is indexed by row, then column. (e.g [0,4] is in the upper right corner of the
            field (Z5).) Each junction is stored bottom up (index 0 is the bottom-most element on the field). MY_* elements
            belong to the alliance whose score object the element appears in, OTHER_* elements belong to the opposing
            alliance. (e.g in a set of scores for the red alliance, MY_CONE is a red cone and OTHER_CONE is a blue cone.)
            For a complete example, if red.autoJunctions[4][0][1] is OTHER_CONE, there is a blue cone in the bottom left
            cornerof the field (V1) on top of one other cone.
        dc_junctions (Union[Unset, None, List[List[List[JunctionElement]]]]): Two dimensional array of lists of items
            scored on junctions in driver-controlled. [0,0] is the upper-left corner of the field as viewed from the
            audience side of the field (V5). The array is indexed by crow, then column. (e.g [0,4] is in the upper right
            corner of the field (Z5).) Each junction is stored bottom up (index 0 is the bottom-most element on the field).
            MY_* elements belong to the alliance whose score object the element appears in, OTHER_* elements belong to the
            opposing alliance. (e.g in a set of scores for the red alliance, MY_CONE is a red cone and OTHER_CONE is a blue
            cone.) *_R1_BEACON means the beacon scored by robot 1 on the corresponding alliance. For a complete example, if
            red.dcJunctions[4][0][1] is OTHER_CONE, there is a blue cone in the bottom left cornerof the field (V1) on top
            of one other cone.
        dc_terminal_near (Union[Unset, int]): Number of Scored cones in the alliance-colored terminal on the side of the
            field closest to the alliance station.
        dc_terminal_far (Union[Unset, int]): Number of Scored cones in the alliance-colored terminal on the side of the
            field opposite the alliance station.
        eg_navigated_1 (Union[Unset, bool]):
        eg_navigated_2 (Union[Unset, bool]):
        minor_penalties (Union[Unset, int]):
        major_penalties (Union[Unset, int]):
        auto_navigation_points (Union[Unset, int]):
        signal_bonus_points (Union[Unset, int]):
        auto_junction_cone_points (Union[Unset, int]):
        auto_terminal_cone_points (Union[Unset, int]):
        dc_junction_cone_points (Union[Unset, int]):
        dc_terminal_cone_points (Union[Unset, int]):
        ownership_points (Union[Unset, int]):
        circuit_points (Union[Unset, int]):
        eg_navigation_points (Union[Unset, int]):
        auto_points (Union[Unset, int]):
        dc_points (Union[Unset, int]):
        endgame_points (Union[Unset, int]):
        penalty_points_committed (Union[Unset, int]):
        pre_penalty_total (Union[Unset, int]):
        auto_junction_cones (Union[Unset, None, List[int]]): Array of 4 cone counts scored by this alliance on ground,
            low, medium, and high junctions respectively, scored in autonomous. E.g. red.autoJunctionCones[2] is the total
            number of cones scored by red on medium-height junctions.
        dc_junction_cones (Union[Unset, None, List[int]]): Array of 4 cone counts scored by this alliance on ground,
            low, medium, and high junctions respectively, scored in driver-controlled. E.g. red.dcJunctionCones[2] is the
            total number of cones scored by red on medium-height junctions.
        beacons (Union[Unset, int]):
        owned_junctions (Union[Unset, int]):
        circuit (Union[Unset, bool]):
        total_points (Union[Unset, int]):
        alliance (Union[Unset, None, str]):
        team (Union[Unset, int]):
    """

    side_of_field: Union[Unset, FieldSide] = UNSET
    init_signal_sleeve_1: Union[Unset, bool] = UNSET
    init_signal_sleeve_2: Union[Unset, bool] = UNSET
    robot_1_auto: Union[Unset, AutoNavigation] = UNSET
    robot_2_auto: Union[Unset, AutoNavigation] = UNSET
    auto_terminal: Union[Unset, int] = UNSET
    auto_junctions: Union[Unset, None, List[List[List[JunctionElement]]]] = UNSET
    dc_junctions: Union[Unset, None, List[List[List[JunctionElement]]]] = UNSET
    dc_terminal_near: Union[Unset, int] = UNSET
    dc_terminal_far: Union[Unset, int] = UNSET
    eg_navigated_1: Union[Unset, bool] = UNSET
    eg_navigated_2: Union[Unset, bool] = UNSET
    minor_penalties: Union[Unset, int] = UNSET
    major_penalties: Union[Unset, int] = UNSET
    auto_navigation_points: Union[Unset, int] = UNSET
    signal_bonus_points: Union[Unset, int] = UNSET
    auto_junction_cone_points: Union[Unset, int] = UNSET
    auto_terminal_cone_points: Union[Unset, int] = UNSET
    dc_junction_cone_points: Union[Unset, int] = UNSET
    dc_terminal_cone_points: Union[Unset, int] = UNSET
    ownership_points: Union[Unset, int] = UNSET
    circuit_points: Union[Unset, int] = UNSET
    eg_navigation_points: Union[Unset, int] = UNSET
    auto_points: Union[Unset, int] = UNSET
    dc_points: Union[Unset, int] = UNSET
    endgame_points: Union[Unset, int] = UNSET
    penalty_points_committed: Union[Unset, int] = UNSET
    pre_penalty_total: Union[Unset, int] = UNSET
    auto_junction_cones: Union[Unset, None, List[int]] = UNSET
    dc_junction_cones: Union[Unset, None, List[int]] = UNSET
    beacons: Union[Unset, int] = UNSET
    owned_junctions: Union[Unset, int] = UNSET
    circuit: Union[Unset, bool] = UNSET
    total_points: Union[Unset, int] = UNSET
    alliance: Union[Unset, None, str] = UNSET
    team: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        side_of_field: Union[Unset, str] = UNSET
        if not isinstance(self.side_of_field, Unset):
            side_of_field = self.side_of_field.value

        init_signal_sleeve_1 = self.init_signal_sleeve_1
        init_signal_sleeve_2 = self.init_signal_sleeve_2
        robot_1_auto: Union[Unset, str] = UNSET
        if not isinstance(self.robot_1_auto, Unset):
            robot_1_auto = self.robot_1_auto.value

        robot_2_auto: Union[Unset, str] = UNSET
        if not isinstance(self.robot_2_auto, Unset):
            robot_2_auto = self.robot_2_auto.value

        auto_terminal = self.auto_terminal
        auto_junctions: Union[Unset, None, List[List[List[str]]]] = UNSET
        if not isinstance(self.auto_junctions, Unset):
            if self.auto_junctions is None:
                auto_junctions = None
            else:
                auto_junctions = []
                for auto_junctions_item_data in self.auto_junctions:
                    auto_junctions_item = []
                    for auto_junctions_item_item_data in auto_junctions_item_data:
                        auto_junctions_item_item = []
                        for (
                            auto_junctions_item_item_item_data
                        ) in auto_junctions_item_item_data:
                            auto_junctions_item_item_item = (
                                auto_junctions_item_item_item_data.value
                            )

                            auto_junctions_item_item.append(
                                auto_junctions_item_item_item
                            )

                        auto_junctions_item.append(auto_junctions_item_item)

                    auto_junctions.append(auto_junctions_item)

        dc_junctions: Union[Unset, None, List[List[List[str]]]] = UNSET
        if not isinstance(self.dc_junctions, Unset):
            if self.dc_junctions is None:
                dc_junctions = None
            else:
                dc_junctions = []
                for dc_junctions_item_data in self.dc_junctions:
                    dc_junctions_item = []
                    for dc_junctions_item_item_data in dc_junctions_item_data:
                        dc_junctions_item_item = []
                        for (
                            dc_junctions_item_item_item_data
                        ) in dc_junctions_item_item_data:
                            dc_junctions_item_item_item = (
                                dc_junctions_item_item_item_data.value
                            )

                            dc_junctions_item_item.append(dc_junctions_item_item_item)

                        dc_junctions_item.append(dc_junctions_item_item)

                    dc_junctions.append(dc_junctions_item)

        dc_terminal_near = self.dc_terminal_near
        dc_terminal_far = self.dc_terminal_far
        eg_navigated_1 = self.eg_navigated_1
        eg_navigated_2 = self.eg_navigated_2
        minor_penalties = self.minor_penalties
        major_penalties = self.major_penalties
        auto_navigation_points = self.auto_navigation_points
        signal_bonus_points = self.signal_bonus_points
        auto_junction_cone_points = self.auto_junction_cone_points
        auto_terminal_cone_points = self.auto_terminal_cone_points
        dc_junction_cone_points = self.dc_junction_cone_points
        dc_terminal_cone_points = self.dc_terminal_cone_points
        ownership_points = self.ownership_points
        circuit_points = self.circuit_points
        eg_navigation_points = self.eg_navigation_points
        auto_points = self.auto_points
        dc_points = self.dc_points
        endgame_points = self.endgame_points
        penalty_points_committed = self.penalty_points_committed
        pre_penalty_total = self.pre_penalty_total
        auto_junction_cones: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.auto_junction_cones, Unset):
            if self.auto_junction_cones is None:
                auto_junction_cones = None
            else:
                auto_junction_cones = self.auto_junction_cones

        dc_junction_cones: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.dc_junction_cones, Unset):
            if self.dc_junction_cones is None:
                dc_junction_cones = None
            else:
                dc_junction_cones = self.dc_junction_cones

        beacons = self.beacons
        owned_junctions = self.owned_junctions
        circuit = self.circuit
        total_points = self.total_points
        alliance = self.alliance
        team = self.team

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if side_of_field is not UNSET:
            field_dict["sideOfField"] = side_of_field
        if init_signal_sleeve_1 is not UNSET:
            field_dict["initSignalSleeve1"] = init_signal_sleeve_1
        if init_signal_sleeve_2 is not UNSET:
            field_dict["initSignalSleeve2"] = init_signal_sleeve_2
        if robot_1_auto is not UNSET:
            field_dict["robot1Auto"] = robot_1_auto
        if robot_2_auto is not UNSET:
            field_dict["robot2Auto"] = robot_2_auto
        if auto_terminal is not UNSET:
            field_dict["autoTerminal"] = auto_terminal
        if auto_junctions is not UNSET:
            field_dict["autoJunctions"] = auto_junctions
        if dc_junctions is not UNSET:
            field_dict["dcJunctions"] = dc_junctions
        if dc_terminal_near is not UNSET:
            field_dict["dcTerminalNear"] = dc_terminal_near
        if dc_terminal_far is not UNSET:
            field_dict["dcTerminalFar"] = dc_terminal_far
        if eg_navigated_1 is not UNSET:
            field_dict["egNavigated1"] = eg_navigated_1
        if eg_navigated_2 is not UNSET:
            field_dict["egNavigated2"] = eg_navigated_2
        if minor_penalties is not UNSET:
            field_dict["minorPenalties"] = minor_penalties
        if major_penalties is not UNSET:
            field_dict["majorPenalties"] = major_penalties
        if auto_navigation_points is not UNSET:
            field_dict["autoNavigationPoints"] = auto_navigation_points
        if signal_bonus_points is not UNSET:
            field_dict["signalBonusPoints"] = signal_bonus_points
        if auto_junction_cone_points is not UNSET:
            field_dict["autoJunctionConePoints"] = auto_junction_cone_points
        if auto_terminal_cone_points is not UNSET:
            field_dict["autoTerminalConePoints"] = auto_terminal_cone_points
        if dc_junction_cone_points is not UNSET:
            field_dict["dcJunctionConePoints"] = dc_junction_cone_points
        if dc_terminal_cone_points is not UNSET:
            field_dict["dcTerminalConePoints"] = dc_terminal_cone_points
        if ownership_points is not UNSET:
            field_dict["ownershipPoints"] = ownership_points
        if circuit_points is not UNSET:
            field_dict["circuitPoints"] = circuit_points
        if eg_navigation_points is not UNSET:
            field_dict["egNavigationPoints"] = eg_navigation_points
        if auto_points is not UNSET:
            field_dict["autoPoints"] = auto_points
        if dc_points is not UNSET:
            field_dict["dcPoints"] = dc_points
        if endgame_points is not UNSET:
            field_dict["endgamePoints"] = endgame_points
        if penalty_points_committed is not UNSET:
            field_dict["penaltyPointsCommitted"] = penalty_points_committed
        if pre_penalty_total is not UNSET:
            field_dict["prePenaltyTotal"] = pre_penalty_total
        if auto_junction_cones is not UNSET:
            field_dict["autoJunctionCones"] = auto_junction_cones
        if dc_junction_cones is not UNSET:
            field_dict["dcJunctionCones"] = dc_junction_cones
        if beacons is not UNSET:
            field_dict["beacons"] = beacons
        if owned_junctions is not UNSET:
            field_dict["ownedJunctions"] = owned_junctions
        if circuit is not UNSET:
            field_dict["circuit"] = circuit
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
        _side_of_field = d.pop("sideOfField", UNSET)
        side_of_field: Union[Unset, FieldSide]
        if isinstance(_side_of_field, Unset):
            side_of_field = UNSET
        else:
            side_of_field = FieldSide(_side_of_field)

        init_signal_sleeve_1 = d.pop("initSignalSleeve1", UNSET)

        init_signal_sleeve_2 = d.pop("initSignalSleeve2", UNSET)

        _robot_1_auto = d.pop("robot1Auto", UNSET)
        robot_1_auto: Union[Unset, AutoNavigation]
        if isinstance(_robot_1_auto, Unset):
            robot_1_auto = UNSET
        else:
            robot_1_auto = AutoNavigation(_robot_1_auto)

        _robot_2_auto = d.pop("robot2Auto", UNSET)
        robot_2_auto: Union[Unset, AutoNavigation]
        if isinstance(_robot_2_auto, Unset):
            robot_2_auto = UNSET
        else:
            robot_2_auto = AutoNavigation(_robot_2_auto)

        auto_terminal = d.pop("autoTerminal", UNSET)

        auto_junctions = []
        _auto_junctions = d.pop("autoJunctions", UNSET)
        for auto_junctions_item_data in _auto_junctions or []:
            auto_junctions_item = []
            _auto_junctions_item = auto_junctions_item_data
            for auto_junctions_item_item_data in _auto_junctions_item:
                auto_junctions_item_item = []
                _auto_junctions_item_item = auto_junctions_item_item_data
                for auto_junctions_item_item_item_data in _auto_junctions_item_item:
                    auto_junctions_item_item_item = JunctionElement(
                        auto_junctions_item_item_item_data
                    )

                    auto_junctions_item_item.append(auto_junctions_item_item_item)

                auto_junctions_item.append(auto_junctions_item_item)

            auto_junctions.append(auto_junctions_item)

        dc_junctions = []
        _dc_junctions = d.pop("dcJunctions", UNSET)
        for dc_junctions_item_data in _dc_junctions or []:
            dc_junctions_item = []
            _dc_junctions_item = dc_junctions_item_data
            for dc_junctions_item_item_data in _dc_junctions_item:
                dc_junctions_item_item = []
                _dc_junctions_item_item = dc_junctions_item_item_data
                for dc_junctions_item_item_item_data in _dc_junctions_item_item:
                    dc_junctions_item_item_item = JunctionElement(
                        dc_junctions_item_item_item_data
                    )

                    dc_junctions_item_item.append(dc_junctions_item_item_item)

                dc_junctions_item.append(dc_junctions_item_item)

            dc_junctions.append(dc_junctions_item)

        dc_terminal_near = d.pop("dcTerminalNear", UNSET)

        dc_terminal_far = d.pop("dcTerminalFar", UNSET)

        eg_navigated_1 = d.pop("egNavigated1", UNSET)

        eg_navigated_2 = d.pop("egNavigated2", UNSET)

        minor_penalties = d.pop("minorPenalties", UNSET)

        major_penalties = d.pop("majorPenalties", UNSET)

        auto_navigation_points = d.pop("autoNavigationPoints", UNSET)

        signal_bonus_points = d.pop("signalBonusPoints", UNSET)

        auto_junction_cone_points = d.pop("autoJunctionConePoints", UNSET)

        auto_terminal_cone_points = d.pop("autoTerminalConePoints", UNSET)

        dc_junction_cone_points = d.pop("dcJunctionConePoints", UNSET)

        dc_terminal_cone_points = d.pop("dcTerminalConePoints", UNSET)

        ownership_points = d.pop("ownershipPoints", UNSET)

        circuit_points = d.pop("circuitPoints", UNSET)

        eg_navigation_points = d.pop("egNavigationPoints", UNSET)

        auto_points = d.pop("autoPoints", UNSET)

        dc_points = d.pop("dcPoints", UNSET)

        endgame_points = d.pop("endgamePoints", UNSET)

        penalty_points_committed = d.pop("penaltyPointsCommitted", UNSET)

        pre_penalty_total = d.pop("prePenaltyTotal", UNSET)

        auto_junction_cones = cast(List[int], d.pop("autoJunctionCones", UNSET))

        dc_junction_cones = cast(List[int], d.pop("dcJunctionCones", UNSET))

        beacons = d.pop("beacons", UNSET)

        owned_junctions = d.pop("ownedJunctions", UNSET)

        circuit = d.pop("circuit", UNSET)

        total_points = d.pop("totalPoints", UNSET)

        alliance = d.pop("alliance", UNSET)

        team = d.pop("team", UNSET)

        power_play_alliance_score_breakdown = cls(
            side_of_field=side_of_field,
            init_signal_sleeve_1=init_signal_sleeve_1,
            init_signal_sleeve_2=init_signal_sleeve_2,
            robot_1_auto=robot_1_auto,
            robot_2_auto=robot_2_auto,
            auto_terminal=auto_terminal,
            auto_junctions=auto_junctions,
            dc_junctions=dc_junctions,
            dc_terminal_near=dc_terminal_near,
            dc_terminal_far=dc_terminal_far,
            eg_navigated_1=eg_navigated_1,
            eg_navigated_2=eg_navigated_2,
            minor_penalties=minor_penalties,
            major_penalties=major_penalties,
            auto_navigation_points=auto_navigation_points,
            signal_bonus_points=signal_bonus_points,
            auto_junction_cone_points=auto_junction_cone_points,
            auto_terminal_cone_points=auto_terminal_cone_points,
            dc_junction_cone_points=dc_junction_cone_points,
            dc_terminal_cone_points=dc_terminal_cone_points,
            ownership_points=ownership_points,
            circuit_points=circuit_points,
            eg_navigation_points=eg_navigation_points,
            auto_points=auto_points,
            dc_points=dc_points,
            endgame_points=endgame_points,
            penalty_points_committed=penalty_points_committed,
            pre_penalty_total=pre_penalty_total,
            auto_junction_cones=auto_junction_cones,
            dc_junction_cones=dc_junction_cones,
            beacons=beacons,
            owned_junctions=owned_junctions,
            circuit=circuit,
            total_points=total_points,
            alliance=alliance,
            team=team,
        )

        return power_play_alliance_score_breakdown
