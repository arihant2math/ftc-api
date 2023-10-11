import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.point import Point


T = TypeVar("T", bound="Event")


@attr.s(auto_attribs=True)
class Event:
    """
    Attributes:
        event_id (Union[Unset, str]):
        code (Union[Unset, None, str]):
        division_code (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        remote (Union[Unset, bool]):
        hybrid (Union[Unset, bool]):
        field_count (Union[Unset, int]):
        published (Union[Unset, bool]):
        type (Union[Unset, None, str]):
        type_name (Union[Unset, None, str]):
        region_code (Union[Unset, None, str]):
        league_code (Union[Unset, None, str]):
        district_code (Union[Unset, None, str]):
        venue (Union[Unset, None, str]):
        address (Union[Unset, None, str]):
        city (Union[Unset, None, str]):
        stateprov (Union[Unset, None, str]):
        country (Union[Unset, None, str]):
        website (Union[Unset, None, str]):
        live_stream_url (Union[Unset, None, str]):
        coordinates (Union[Unset, Point]):
        webcasts (Union[Unset, None, List[str]]):
        timezone (Union[Unset, None, str]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
    """

    event_id: Union[Unset, str] = UNSET
    code: Union[Unset, None, str] = UNSET
    division_code: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    remote: Union[Unset, bool] = UNSET
    hybrid: Union[Unset, bool] = UNSET
    field_count: Union[Unset, int] = UNSET
    published: Union[Unset, bool] = UNSET
    type: Union[Unset, None, str] = UNSET
    type_name: Union[Unset, None, str] = UNSET
    region_code: Union[Unset, None, str] = UNSET
    league_code: Union[Unset, None, str] = UNSET
    district_code: Union[Unset, None, str] = UNSET
    venue: Union[Unset, None, str] = UNSET
    address: Union[Unset, None, str] = UNSET
    city: Union[Unset, None, str] = UNSET
    stateprov: Union[Unset, None, str] = UNSET
    country: Union[Unset, None, str] = UNSET
    website: Union[Unset, None, str] = UNSET
    live_stream_url: Union[Unset, None, str] = UNSET
    coordinates: Union[Unset, "Point"] = UNSET
    webcasts: Union[Unset, None, List[str]] = UNSET
    timezone: Union[Unset, None, str] = UNSET
    date_start: Union[Unset, datetime.datetime] = UNSET
    date_end: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        event_id = self.event_id
        code = self.code
        division_code = self.division_code
        name = self.name
        remote = self.remote
        hybrid = self.hybrid
        field_count = self.field_count
        published = self.published
        type = self.type
        type_name = self.type_name
        region_code = self.region_code
        league_code = self.league_code
        district_code = self.district_code
        venue = self.venue
        address = self.address
        city = self.city
        stateprov = self.stateprov
        country = self.country
        website = self.website
        live_stream_url = self.live_stream_url
        coordinates: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.coordinates, Unset):
            coordinates = self.coordinates.to_dict()

        webcasts: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.webcasts, Unset):
            if self.webcasts is None:
                webcasts = None
            else:
                webcasts = self.webcasts

        timezone = self.timezone
        date_start: Union[Unset, str] = UNSET
        if not isinstance(self.date_start, Unset):
            date_start = self.date_start.isoformat()

        date_end: Union[Unset, str] = UNSET
        if not isinstance(self.date_end, Unset):
            date_end = self.date_end.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if code is not UNSET:
            field_dict["code"] = code
        if division_code is not UNSET:
            field_dict["divisionCode"] = division_code
        if name is not UNSET:
            field_dict["name"] = name
        if remote is not UNSET:
            field_dict["remote"] = remote
        if hybrid is not UNSET:
            field_dict["hybrid"] = hybrid
        if field_count is not UNSET:
            field_dict["fieldCount"] = field_count
        if published is not UNSET:
            field_dict["published"] = published
        if type is not UNSET:
            field_dict["type"] = type
        if type_name is not UNSET:
            field_dict["typeName"] = type_name
        if region_code is not UNSET:
            field_dict["regionCode"] = region_code
        if league_code is not UNSET:
            field_dict["leagueCode"] = league_code
        if district_code is not UNSET:
            field_dict["districtCode"] = district_code
        if venue is not UNSET:
            field_dict["venue"] = venue
        if address is not UNSET:
            field_dict["address"] = address
        if city is not UNSET:
            field_dict["city"] = city
        if stateprov is not UNSET:
            field_dict["stateprov"] = stateprov
        if country is not UNSET:
            field_dict["country"] = country
        if website is not UNSET:
            field_dict["website"] = website
        if live_stream_url is not UNSET:
            field_dict["liveStreamUrl"] = live_stream_url
        if coordinates is not UNSET:
            field_dict["coordinates"] = coordinates
        if webcasts is not UNSET:
            field_dict["webcasts"] = webcasts
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if date_start is not UNSET:
            field_dict["dateStart"] = date_start
        if date_end is not UNSET:
            field_dict["dateEnd"] = date_end

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.point import Point

        d = src_dict.copy()
        event_id = d.pop("eventId", UNSET)

        code = d.pop("code", UNSET)

        division_code = d.pop("divisionCode", UNSET)

        name = d.pop("name", UNSET)

        remote = d.pop("remote", UNSET)

        hybrid = d.pop("hybrid", UNSET)

        field_count = d.pop("fieldCount", UNSET)

        published = d.pop("published", UNSET)

        type = d.pop("type", UNSET)

        type_name = d.pop("typeName", UNSET)

        region_code = d.pop("regionCode", UNSET)

        league_code = d.pop("leagueCode", UNSET)

        district_code = d.pop("districtCode", UNSET)

        venue = d.pop("venue", UNSET)

        address = d.pop("address", UNSET)

        city = d.pop("city", UNSET)

        stateprov = d.pop("stateprov", UNSET)

        country = d.pop("country", UNSET)

        website = d.pop("website", UNSET)

        live_stream_url = d.pop("liveStreamUrl", UNSET)

        _coordinates = d.pop("coordinates", UNSET)
        coordinates: Union[Unset, Point]
        if isinstance(_coordinates, Unset):
            coordinates = UNSET
        else:
            coordinates = Point.from_dict(_coordinates)

        webcasts = cast(List[str], d.pop("webcasts", UNSET))

        timezone = d.pop("timezone", UNSET)

        _date_start = d.pop("dateStart", UNSET)
        date_start: Union[Unset, datetime.datetime]
        if isinstance(_date_start, Unset):
            date_start = UNSET
        else:
            date_start = isoparse(_date_start)

        _date_end = d.pop("dateEnd", UNSET)
        date_end: Union[Unset, datetime.datetime]
        if isinstance(_date_end, Unset):
            date_end = UNSET
        else:
            date_end = isoparse(_date_end)

        event = cls(
            event_id=event_id,
            code=code,
            division_code=division_code,
            name=name,
            remote=remote,
            hybrid=hybrid,
            field_count=field_count,
            published=published,
            type=type,
            type_name=type_name,
            region_code=region_code,
            league_code=league_code,
            district_code=district_code,
            venue=venue,
            address=address,
            city=city,
            stateprov=stateprov,
            country=country,
            website=website,
            live_stream_url=live_stream_url,
            coordinates=coordinates,
            webcasts=webcasts,
            timezone=timezone,
            date_start=date_start,
            date_end=date_end,
        )

        return event
