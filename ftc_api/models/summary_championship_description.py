import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SummaryChampionshipDescription")


@attr.s(auto_attribs=True)
class SummaryChampionshipDescription:
    """
    Attributes:
        name (Union[Unset, None, str]):
        start_date (Union[Unset, None, datetime.datetime]):
        location (Union[Unset, None, str]):
    """

    name: Union[Unset, None, str] = UNSET
    start_date: Union[Unset, None, datetime.datetime] = UNSET
    location: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        start_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat() if self.start_date else None

        location = self.location

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, None, datetime.datetime]
        if _start_date is None:
            start_date = None
        elif isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        location = d.pop("location", UNSET)

        summary_championship_description = cls(
            name=name,
            start_date=start_date,
            location=location,
        )

        return summary_championship_description
