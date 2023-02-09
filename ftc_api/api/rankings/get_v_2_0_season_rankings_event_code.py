from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ftc_api import errors
from ftc_api.client import AuthenticatedClient, Client
from ftc_api.models.event_ranking_list import EventRankingList
from ftc_api.types import UNSET, Response, Unset


def _get_kwargs(
    season: int,
    event_code: Optional[str],
    *,
    client: AuthenticatedClient,
    team_number: Union[Unset, None, int] = 0,
    top: Union[Unset, None, int] = 0,
) -> Dict[str, Any]:
    url = "{}/v2.0/{season}/rankings/{eventCode}".format(
        "https://ftc-api.firstinspires.org", season=season, eventCode=event_code
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["teamNumber"] = team_number

    params["top"] = top

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
) -> Optional[Union[Any, EventRankingList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = EventRankingList.from_dict(response.json())

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
) -> Response[Union[Any, EventRankingList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    season: int,
    event_code: Optional[str],
    *,
    client: AuthenticatedClient,
    team_number: Union[Unset, None, int] = 0,
    top: Union[Unset, None, int] = 0,
) -> Response[Union[Any, EventRankingList]]:
    """Event Rankings

     The rankings API returns team ranking detail from a particular event in a particular season.
    Optionally, the `top` parameter can be added to the query string to request a subset of the rankings
    based on the highest ranked teams at the time of the request. Alternately, you can specify the
    `teamNumber` parameter to retrieve the ranking on one specific team. You cannot specify both a `top`
    and `teamNumber` in the same call.

    Args:
        season (int):
        event_code (Optional[str]):
        team_number (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventRankingList]]
    """

    kwargs = _get_kwargs(
        season=season,
        event_code=event_code,
        client=client,
        team_number=team_number,
        top=top,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    season: int,
    event_code: Optional[str],
    *,
    client: AuthenticatedClient,
    team_number: Union[Unset, None, int] = 0,
    top: Union[Unset, None, int] = 0,
) -> Optional[Union[Any, EventRankingList]]:
    """Event Rankings

     The rankings API returns team ranking detail from a particular event in a particular season.
    Optionally, the `top` parameter can be added to the query string to request a subset of the rankings
    based on the highest ranked teams at the time of the request. Alternately, you can specify the
    `teamNumber` parameter to retrieve the ranking on one specific team. You cannot specify both a `top`
    and `teamNumber` in the same call.

    Args:
        season (int):
        event_code (Optional[str]):
        team_number (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventRankingList]]
    """

    return sync_detailed(
        season=season,
        event_code=event_code,
        client=client,
        team_number=team_number,
        top=top,
    ).parsed


async def asyncio_detailed(
    season: int,
    event_code: Optional[str],
    *,
    client: AuthenticatedClient,
    team_number: Union[Unset, None, int] = 0,
    top: Union[Unset, None, int] = 0,
) -> Response[Union[Any, EventRankingList]]:
    """Event Rankings

     The rankings API returns team ranking detail from a particular event in a particular season.
    Optionally, the `top` parameter can be added to the query string to request a subset of the rankings
    based on the highest ranked teams at the time of the request. Alternately, you can specify the
    `teamNumber` parameter to retrieve the ranking on one specific team. You cannot specify both a `top`
    and `teamNumber` in the same call.

    Args:
        season (int):
        event_code (Optional[str]):
        team_number (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventRankingList]]
    """

    kwargs = _get_kwargs(
        season=season,
        event_code=event_code,
        client=client,
        team_number=team_number,
        top=top,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    season: int,
    event_code: Optional[str],
    *,
    client: AuthenticatedClient,
    team_number: Union[Unset, None, int] = 0,
    top: Union[Unset, None, int] = 0,
) -> Optional[Union[Any, EventRankingList]]:
    """Event Rankings

     The rankings API returns team ranking detail from a particular event in a particular season.
    Optionally, the `top` parameter can be added to the query string to request a subset of the rankings
    based on the highest ranked teams at the time of the request. Alternately, you can specify the
    `teamNumber` parameter to retrieve the ranking on one specific team. You cannot specify both a `top`
    and `teamNumber` in the same call.

    Args:
        season (int):
        event_code (Optional[str]):
        team_number (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventRankingList]]
    """

    return (
        await asyncio_detailed(
            season=season,
            event_code=event_code,
            client=client,
            team_number=team_number,
            top=top,
        )
    ).parsed
