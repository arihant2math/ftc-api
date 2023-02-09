from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_ranking_list import EventRankingList
from ...types import Response


def _get_kwargs(
    season: int,
    region_code: Optional[str],
    league_code: Optional[str],
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/v2.0/{season}/leagues/rankings/{regionCode}/{leagueCode}".format(
        "https://ftc-api.firstinspires.org",
        season=season,
        regionCode=region_code,
        leagueCode=league_code,
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "http2": client.http2,
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
    region_code: Optional[str],
    league_code: Optional[str],
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, EventRankingList]]:
    """League Rankings

     The league rankings API returns team ranking detail from a particular league in a particular season.
    League rankings are only the cumulative rankings from League Meets - they do not include performance
    at the League Tournament. To get League Tournament Rankings, use the Event Rankings endpoint.

    Args:
        season (int):
        region_code (Optional[str]):
        league_code (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventRankingList]]
    """

    kwargs = _get_kwargs(
        season=season,
        region_code=region_code,
        league_code=league_code,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    season: int,
    region_code: Optional[str],
    league_code: Optional[str],
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, EventRankingList]]:
    """League Rankings

     The league rankings API returns team ranking detail from a particular league in a particular season.
    League rankings are only the cumulative rankings from League Meets - they do not include performance
    at the League Tournament. To get League Tournament Rankings, use the Event Rankings endpoint.

    Args:
        season (int):
        region_code (Optional[str]):
        league_code (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventRankingList]]
    """

    return sync_detailed(
        season=season,
        region_code=region_code,
        league_code=league_code,
        client=client,
    ).parsed


async def asyncio_detailed(
    season: int,
    region_code: Optional[str],
    league_code: Optional[str],
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, EventRankingList]]:
    """League Rankings

     The league rankings API returns team ranking detail from a particular league in a particular season.
    League rankings are only the cumulative rankings from League Meets - they do not include performance
    at the League Tournament. To get League Tournament Rankings, use the Event Rankings endpoint.

    Args:
        season (int):
        region_code (Optional[str]):
        league_code (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventRankingList]]
    """

    kwargs = _get_kwargs(
        season=season,
        region_code=region_code,
        league_code=league_code,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    season: int,
    region_code: Optional[str],
    league_code: Optional[str],
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, EventRankingList]]:
    """League Rankings

     The league rankings API returns team ranking detail from a particular league in a particular season.
    League rankings are only the cumulative rankings from League Meets - they do not include performance
    at the League Tournament. To get League Tournament Rankings, use the Event Rankings endpoint.

    Args:
        season (int):
        region_code (Optional[str]):
        league_code (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventRankingList]]
    """

    return (
        await asyncio_detailed(
            season=season,
            region_code=region_code,
            league_code=league_code,
            client=client,
        )
    ).parsed
