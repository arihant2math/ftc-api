from typing import Any, Dict, Type, TypeVar, Union

import attr

from .._types import UNSET, Unset

T = TypeVar("T", bound="Team")


@attr.s(auto_attribs=True)
class Team:
    """
    Attributes:
        team_number (Union[Unset, int]):
        name_full (Union[Unset, None, str]):
        name_short (Union[Unset, None, str]):
        school_name (Union[Unset, None, str]):
        city (Union[Unset, None, str]):
        state_prov (Union[Unset, None, str]):
        country (Union[Unset, None, str]):
        website (Union[Unset, None, str]):
        rookie_year (Union[Unset, None, int]):
        robot_name (Union[Unset, None, str]):
        district_code (Union[Unset, None, str]):
        home_cmp (Union[Unset, None, str]):
    """

    team_number: Union[Unset, int] = UNSET
    name_full: Union[Unset, None, str] = UNSET
    name_short: Union[Unset, None, str] = UNSET
    school_name: Union[Unset, None, str] = UNSET
    city: Union[Unset, None, str] = UNSET
    state_prov: Union[Unset, None, str] = UNSET
    country: Union[Unset, None, str] = UNSET
    website: Union[Unset, None, str] = UNSET
    rookie_year: Union[Unset, None, int] = UNSET
    robot_name: Union[Unset, None, str] = UNSET
    district_code: Union[Unset, None, str] = UNSET
    home_cmp: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        team_number = self.team_number
        name_full = self.name_full
        name_short = self.name_short
        school_name = self.school_name
        city = self.city
        state_prov = self.state_prov
        country = self.country
        website = self.website
        rookie_year = self.rookie_year
        robot_name = self.robot_name
        district_code = self.district_code
        home_cmp = self.home_cmp

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if team_number is not UNSET:
            field_dict["teamNumber"] = team_number
        if name_full is not UNSET:
            field_dict["nameFull"] = name_full
        if name_short is not UNSET:
            field_dict["nameShort"] = name_short
        if school_name is not UNSET:
            field_dict["schoolName"] = school_name
        if city is not UNSET:
            field_dict["city"] = city
        if state_prov is not UNSET:
            field_dict["stateProv"] = state_prov
        if country is not UNSET:
            field_dict["country"] = country
        if website is not UNSET:
            field_dict["website"] = website
        if rookie_year is not UNSET:
            field_dict["rookieYear"] = rookie_year
        if robot_name is not UNSET:
            field_dict["robotName"] = robot_name
        if district_code is not UNSET:
            field_dict["districtCode"] = district_code
        if home_cmp is not UNSET:
            field_dict["homeCMP"] = home_cmp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        team_number = d.pop("teamNumber", UNSET)

        name_full = d.pop("nameFull", UNSET)

        name_short = d.pop("nameShort", UNSET)

        school_name = d.pop("schoolName", UNSET)

        city = d.pop("city", UNSET)

        state_prov = d.pop("stateProv", UNSET)

        country = d.pop("country", UNSET)

        website = d.pop("website", UNSET)

        rookie_year = d.pop("rookieYear", UNSET)

        robot_name = d.pop("robotName", UNSET)

        district_code = d.pop("districtCode", UNSET)

        home_cmp = d.pop("homeCMP", UNSET)

        team = cls(
            team_number=team_number,
            name_full=name_full,
            name_short=name_short,
            school_name=school_name,
            city=city,
            state_prov=state_prov,
            country=country,
            website=website,
            rookie_year=rookie_year,
            robot_name=robot_name,
            district_code=district_code,
            home_cmp=home_cmp,
        )

        return team
