from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event import Event


T = TypeVar("T", bound="EventList")


@attr.s(auto_attribs=True)
class EventList:
    """
    Attributes:
        events (Union[Unset, None, List['Event']]):
        event_count (Union[Unset, int]):
    """

    events: Union[Unset, None, List["Event"]] = UNSET
    event_count: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        events: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            if self.events is None:
                events = None
            else:
                events = []
                for events_item_data in self.events:
                    events_item = events_item_data.to_dict()

                    events.append(events_item)

        event_count = self.event_count

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if events is not UNSET:
            field_dict["events"] = events
        if event_count is not UNSET:
            field_dict["eventCount"] = event_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event import Event

        d = src_dict.copy()
        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = Event.from_dict(events_item_data)

            events.append(events_item)

        event_count = d.pop("eventCount", UNSET)

        event_list = cls(
            events=events,
            event_count=event_count,
        )

        return event_list
