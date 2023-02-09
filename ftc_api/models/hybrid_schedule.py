from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ftc_api.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hybrid_schedule_match import HybridScheduleMatch


T = TypeVar("T", bound="HybridSchedule")


@attr.s(auto_attribs=True)
class HybridSchedule:
    """
    Attributes:
        schedule (Union[Unset, None, List['HybridScheduleMatch']]):
    """

    schedule: Union[Unset, None, List["HybridScheduleMatch"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        schedule: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.schedule, Unset):
            if self.schedule is None:
                schedule = None
            else:
                schedule = []
                for schedule_item_data in self.schedule:
                    schedule_item = schedule_item_data.to_dict()

                    schedule.append(schedule_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if schedule is not UNSET:
            field_dict["schedule"] = schedule

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.hybrid_schedule_match import HybridScheduleMatch

        d = src_dict.copy()
        schedule = []
        _schedule = d.pop("schedule", UNSET)
        for schedule_item_data in _schedule or []:
            schedule_item = HybridScheduleMatch.from_dict(schedule_item_data)

            schedule.append(schedule_item)

        hybrid_schedule = cls(
            schedule=schedule,
        )

        return hybrid_schedule
