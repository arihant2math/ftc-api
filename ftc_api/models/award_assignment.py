from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AwardAssignment")


@_attrs_define
class AwardAssignment:
    """
    Attributes:
        award_id (Union[Unset, int]):
        team_id (Union[Unset, None, int]):
        event_id (Union[Unset, None, int]):
        event_division_id (Union[Unset, None, int]):
        event_code (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        series (Union[Unset, int]):
        team_number (Union[Unset, None, int]):
        school_name (Union[Unset, None, str]):
        full_team_name (Union[Unset, None, str]):
        person (Union[Unset, None, str]):
    """

    award_id: Union[Unset, int] = UNSET
    team_id: Union[Unset, None, int] = UNSET
    event_id: Union[Unset, None, int] = UNSET
    event_division_id: Union[Unset, None, int] = UNSET
    event_code: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    series: Union[Unset, int] = UNSET
    team_number: Union[Unset, None, int] = UNSET
    school_name: Union[Unset, None, str] = UNSET
    full_team_name: Union[Unset, None, str] = UNSET
    person: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        award_id = self.award_id
        team_id = self.team_id
        event_id = self.event_id
        event_division_id = self.event_division_id
        event_code = self.event_code
        name = self.name
        series = self.series
        team_number = self.team_number
        school_name = self.school_name
        full_team_name = self.full_team_name
        person = self.person

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if award_id is not UNSET:
            field_dict["awardId"] = award_id
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if event_division_id is not UNSET:
            field_dict["eventDivisionId"] = event_division_id
        if event_code is not UNSET:
            field_dict["eventCode"] = event_code
        if name is not UNSET:
            field_dict["name"] = name
        if series is not UNSET:
            field_dict["series"] = series
        if team_number is not UNSET:
            field_dict["teamNumber"] = team_number
        if school_name is not UNSET:
            field_dict["schoolName"] = school_name
        if full_team_name is not UNSET:
            field_dict["fullTeamName"] = full_team_name
        if person is not UNSET:
            field_dict["person"] = person

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        award_id = d.pop("awardId", UNSET)

        team_id = d.pop("teamId", UNSET)

        event_id = d.pop("eventId", UNSET)

        event_division_id = d.pop("eventDivisionId", UNSET)

        event_code = d.pop("eventCode", UNSET)

        name = d.pop("name", UNSET)

        series = d.pop("series", UNSET)

        team_number = d.pop("teamNumber", UNSET)

        school_name = d.pop("schoolName", UNSET)

        full_team_name = d.pop("fullTeamName", UNSET)

        person = d.pop("person", UNSET)

        award_assignment = cls(
            award_id=award_id,
            team_id=team_id,
            event_id=event_id,
            event_division_id=event_division_id,
            event_code=event_code,
            name=name,
            series=series,
            team_number=team_number,
            school_name=school_name,
            full_team_name=full_team_name,
            person=person,
        )

        return award_assignment
