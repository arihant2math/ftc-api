from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.event_list import EventList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    season: int,
    *,
    client: Client,
    event_code: Union[Unset, None, str] = "0",
    team_number: Union[Unset, None, int] = 0,
) -> Dict[str, Any]:
    url = "{}/v2.0/{season}/events".format("https://ftc-api.firstinspires.org", season=season)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["eventCode"] = event_code

    params["teamNumber"] = team_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, EventList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = EventList.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, EventList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    season: int,
    *,
    client: Client,
    event_code: Union[Unset, None, str] = "0",
    team_number: Union[Unset, None, int] = 0,
) -> Response[Union[Any, EventList]]:
    """Event Listings

     The event listings API returns all FTC official regional events in a particular season. You can
    specify an `eventCode` if you would only like data about one specific event. If you specify an
    `eventCode` you cannot specify any other optional parameters. Alternately, you can specify a
    `teamNumber` to retrieve only the listings of events being attended by the particular team. If you
    specify a `teamNumber` you cannot specify an `eventCode`.

    The response for event listings contains a special field called divisionCode. For example, the FIRST
    Championship contains two Divisions. As an example of a response, the event listings for a Division
    will have a divisionCode that matches the FIRST Championship event code (as they are divisions of
    that event). This allows you to see the full structure of events, and how they relate to each other.

    Args:
        season (int):
        event_code (Union[Unset, None, str]):  Default: '0'.
        team_number (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventList]]
    """

    kwargs = _get_kwargs(
        season=season,
        client=client,
        event_code=event_code,
        team_number=team_number,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    season: int,
    *,
    client: Client,
    event_code: Union[Unset, None, str] = "0",
    team_number: Union[Unset, None, int] = 0,
) -> Optional[Union[Any, EventList]]:
    """Event Listings

     The event listings API returns all FTC official regional events in a particular season. You can
    specify an `eventCode` if you would only like data about one specific event. If you specify an
    `eventCode` you cannot specify any other optional parameters. Alternately, you can specify a
    `teamNumber` to retrieve only the listings of events being attended by the particular team. If you
    specify a `teamNumber` you cannot specify an `eventCode`.

    The response for event listings contains a special field called divisionCode. For example, the FIRST
    Championship contains two Divisions. As an example of a response, the event listings for a Division
    will have a divisionCode that matches the FIRST Championship event code (as they are divisions of
    that event). This allows you to see the full structure of events, and how they relate to each other.

    Args:
        season (int):
        event_code (Union[Unset, None, str]):  Default: '0'.
        team_number (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventList]]
    """

    return sync_detailed(
        season=season,
        client=client,
        event_code=event_code,
        team_number=team_number,
    ).parsed


async def asyncio_detailed(
    season: int,
    *,
    client: Client,
    event_code: Union[Unset, None, str] = "0",
    team_number: Union[Unset, None, int] = 0,
) -> Response[Union[Any, EventList]]:
    """Event Listings

     The event listings API returns all FTC official regional events in a particular season. You can
    specify an `eventCode` if you would only like data about one specific event. If you specify an
    `eventCode` you cannot specify any other optional parameters. Alternately, you can specify a
    `teamNumber` to retrieve only the listings of events being attended by the particular team. If you
    specify a `teamNumber` you cannot specify an `eventCode`.

    The response for event listings contains a special field called divisionCode. For example, the FIRST
    Championship contains two Divisions. As an example of a response, the event listings for a Division
    will have a divisionCode that matches the FIRST Championship event code (as they are divisions of
    that event). This allows you to see the full structure of events, and how they relate to each other.

    Args:
        season (int):
        event_code (Union[Unset, None, str]):  Default: '0'.
        team_number (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventList]]
    """

    kwargs = _get_kwargs(
        season=season,
        client=client,
        event_code=event_code,
        team_number=team_number,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    season: int,
    *,
    client: Client,
    event_code: Union[Unset, None, str] = "0",
    team_number: Union[Unset, None, int] = 0,
) -> Optional[Union[Any, EventList]]:
    """Event Listings

     The event listings API returns all FTC official regional events in a particular season. You can
    specify an `eventCode` if you would only like data about one specific event. If you specify an
    `eventCode` you cannot specify any other optional parameters. Alternately, you can specify a
    `teamNumber` to retrieve only the listings of events being attended by the particular team. If you
    specify a `teamNumber` you cannot specify an `eventCode`.

    The response for event listings contains a special field called divisionCode. For example, the FIRST
    Championship contains two Divisions. As an example of a response, the event listings for a Division
    will have a divisionCode that matches the FIRST Championship event code (as they are divisions of
    that event). This allows you to see the full structure of events, and how they relate to each other.

    Args:
        season (int):
        event_code (Union[Unset, None, str]):  Default: '0'.
        team_number (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventList]]
    """

    return (
        await asyncio_detailed(
            season=season,
            client=client,
            event_code=event_code,
            team_number=team_number,
        )
    ).parsed
