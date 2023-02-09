from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.team_list import TeamList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    season: int,
    *,
    client: AuthenticatedClient,
    team_number: Union[Unset, None, int] = 0,
    event_code: Union[Unset, None, str] = "0",
    state: Union[Unset, None, str] = "",
    page: Union[Unset, None, int] = 1,
) -> Dict[str, Any]:
    url = "{}/v2.0/{season}/teams".format(
        "https://ftc-api.firstinspires.org", season=season
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["teamNumber"] = team_number

    params["eventCode"] = event_code

    params["state"] = state

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, TeamList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TeamList.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, TeamList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    season: int,
    *,
    client: AuthenticatedClient,
    team_number: Union[Unset, None, int] = 0,
    event_code: Union[Unset, None, str] = "0",
    state: Union[Unset, None, str] = "",
    page: Union[Unset, None, int] = 1,
) -> Response[Union[Any, TeamList]]:
    """Team Listings

     The team listings API returns all FTC official teams in a particular season. If specified, the
    `teamNumber` parameter will return only one result with the details of the requested `teamNumber`.
    Alternately, the `eventCode` parameter allows sorting of the team list to only those teams attending
    a particular event in the particular season. If you specify a teamNumber parameter, you cannot
    additionally specify an `eventCode` and/or `state` in the same request, or you will receive an HTTP
    501. If you specify the `state` parameter, it should be the full legal name of the US state or
    international state/prov, such as New Hampshire or Ontario. Values on this endpoint are \"pass
    through\" values from the TIMS registration system. As such, if the team does not specify a value
    for a field, it may be presented in the API as null.

    Args:
        season (int):
        team_number (Union[Unset, None, int]):
        event_code (Union[Unset, None, str]):  Default: '0'.
        state (Union[Unset, None, str]):  Default: ''.
        page (Union[Unset, None, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TeamList]]
    """

    kwargs = _get_kwargs(
        season=season,
        client=client,
        team_number=team_number,
        event_code=event_code,
        state=state,
        page=page,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    season: int,
    *,
    client: AuthenticatedClient,
    team_number: Union[Unset, None, int] = 0,
    event_code: Union[Unset, None, str] = "0",
    state: Union[Unset, None, str] = "",
    page: Union[Unset, None, int] = 1,
) -> Optional[Union[Any, TeamList]]:
    """Team Listings

     The team listings API returns all FTC official teams in a particular season. If specified, the
    `teamNumber` parameter will return only one result with the details of the requested `teamNumber`.
    Alternately, the `eventCode` parameter allows sorting of the team list to only those teams attending
    a particular event in the particular season. If you specify a teamNumber parameter, you cannot
    additionally specify an `eventCode` and/or `state` in the same request, or you will receive an HTTP
    501. If you specify the `state` parameter, it should be the full legal name of the US state or
    international state/prov, such as New Hampshire or Ontario. Values on this endpoint are \"pass
    through\" values from the TIMS registration system. As such, if the team does not specify a value
    for a field, it may be presented in the API as null.

    Args:
        season (int):
        team_number (Union[Unset, None, int]):
        event_code (Union[Unset, None, str]):  Default: '0'.
        state (Union[Unset, None, str]):  Default: ''.
        page (Union[Unset, None, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TeamList]]
    """

    return sync_detailed(
        season=season,
        client=client,
        team_number=team_number,
        event_code=event_code,
        state=state,
        page=page,
    ).parsed


async def asyncio_detailed(
    season: int,
    *,
    client: AuthenticatedClient,
    team_number: Union[Unset, None, int] = 0,
    event_code: Union[Unset, None, str] = "0",
    state: Union[Unset, None, str] = "",
    page: Union[Unset, None, int] = 1,
) -> Response[Union[Any, TeamList]]:
    """Team Listings

     The team listings API returns all FTC official teams in a particular season. If specified, the
    `teamNumber` parameter will return only one result with the details of the requested `teamNumber`.
    Alternately, the `eventCode` parameter allows sorting of the team list to only those teams attending
    a particular event in the particular season. If you specify a teamNumber parameter, you cannot
    additionally specify an `eventCode` and/or `state` in the same request, or you will receive an HTTP
    501. If you specify the `state` parameter, it should be the full legal name of the US state or
    international state/prov, such as New Hampshire or Ontario. Values on this endpoint are \"pass
    through\" values from the TIMS registration system. As such, if the team does not specify a value
    for a field, it may be presented in the API as null.

    Args:
        season (int):
        team_number (Union[Unset, None, int]):
        event_code (Union[Unset, None, str]):  Default: '0'.
        state (Union[Unset, None, str]):  Default: ''.
        page (Union[Unset, None, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TeamList]]
    """

    kwargs = _get_kwargs(
        season=season,
        client=client,
        team_number=team_number,
        event_code=event_code,
        state=state,
        page=page,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    season: int,
    *,
    client: AuthenticatedClient,
    team_number: Union[Unset, None, int] = 0,
    event_code: Union[Unset, None, str] = "0",
    state: Union[Unset, None, str] = "",
    page: Union[Unset, None, int] = 1,
) -> Optional[Union[Any, TeamList]]:
    """Team Listings

     The team listings API returns all FTC official teams in a particular season. If specified, the
    `teamNumber` parameter will return only one result with the details of the requested `teamNumber`.
    Alternately, the `eventCode` parameter allows sorting of the team list to only those teams attending
    a particular event in the particular season. If you specify a teamNumber parameter, you cannot
    additionally specify an `eventCode` and/or `state` in the same request, or you will receive an HTTP
    501. If you specify the `state` parameter, it should be the full legal name of the US state or
    international state/prov, such as New Hampshire or Ontario. Values on this endpoint are \"pass
    through\" values from the TIMS registration system. As such, if the team does not specify a value
    for a field, it may be presented in the API as null.

    Args:
        season (int):
        team_number (Union[Unset, None, int]):
        event_code (Union[Unset, None, str]):  Default: '0'.
        state (Union[Unset, None, str]):  Default: ''.
        page (Union[Unset, None, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TeamList]]
    """

    return (
        await asyncio_detailed(
            season=season,
            client=client,
            team_number=team_number,
            event_code=event_code,
            state=state,
            page=page,
        )
    ).parsed
