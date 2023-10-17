from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scheduled_match import ScheduledMatch


T = TypeVar("T", bound="ScheduledMatchList")


@_attrs_define
class ScheduledMatchList:
    """
    Attributes:
        schedule (Union[Unset, None, List['ScheduledMatch']]):
    """

    schedule: Union[Unset, None, List["ScheduledMatch"]] = UNSET

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
        from ..models.scheduled_match import ScheduledMatch

        d = src_dict.copy()
        schedule = []
        _schedule = d.pop("schedule", UNSET)
        for schedule_item_data in _schedule or []:
            schedule_item = ScheduledMatch.from_dict(schedule_item_data)

            schedule.append(schedule_item)

        scheduled_match_list = cls(
            schedule=schedule,
        )

        return scheduled_match_list
