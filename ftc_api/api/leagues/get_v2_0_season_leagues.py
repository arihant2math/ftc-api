from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.league_list import LeagueList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    season: int,
    *,
    client: AuthenticatedClient,
    region_code: Union[Unset, None, str] = UNSET,
    league_code: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v2.0/{season}/leagues".format("https://ftc-api.firstinspires.org", season=season)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["regionCode"] = region_code

    params["leagueCode"] = league_code

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, LeagueList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = LeagueList.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, LeagueList]]:
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
    region_code: Union[Unset, None, str] = UNSET,
    league_code: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, LeagueList]]:
    """League Listings

     The league listings API returns all FTC leagues in a particular season. You can specify a
    `regionCode` to filter to leagues within a particular region. To filter to a specific league, supply
    both a `regionCode` and a `leagueCode`. The returned objects have a `parentLeagueCode` field, which
    indicates the league is a child league if not null and provides the code of the parent league. The
    `regionCode` of the parent league will always match the child.

    Args:
        season (int):
        region_code (Union[Unset, None, str]):
        league_code (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LeagueList]]
    """

    kwargs = _get_kwargs(
        season=season,
        client=client,
        region_code=region_code,
        league_code=league_code,
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
    region_code: Union[Unset, None, str] = UNSET,
    league_code: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, LeagueList]]:
    """League Listings

     The league listings API returns all FTC leagues in a particular season. You can specify a
    `regionCode` to filter to leagues within a particular region. To filter to a specific league, supply
    both a `regionCode` and a `leagueCode`. The returned objects have a `parentLeagueCode` field, which
    indicates the league is a child league if not null and provides the code of the parent league. The
    `regionCode` of the parent league will always match the child.

    Args:
        season (int):
        region_code (Union[Unset, None, str]):
        league_code (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LeagueList]]
    """

    return sync_detailed(
        season=season,
        client=client,
        region_code=region_code,
        league_code=league_code,
    ).parsed


async def asyncio_detailed(
    season: int,
    *,
    client: AuthenticatedClient,
    region_code: Union[Unset, None, str] = UNSET,
    league_code: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, LeagueList]]:
    """League Listings

     The league listings API returns all FTC leagues in a particular season. You can specify a
    `regionCode` to filter to leagues within a particular region. To filter to a specific league, supply
    both a `regionCode` and a `leagueCode`. The returned objects have a `parentLeagueCode` field, which
    indicates the league is a child league if not null and provides the code of the parent league. The
    `regionCode` of the parent league will always match the child.

    Args:
        season (int):
        region_code (Union[Unset, None, str]):
        league_code (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LeagueList]]
    """

    kwargs = _get_kwargs(
        season=season,
        client=client,
        region_code=region_code,
        league_code=league_code,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    season: int,
    *,
    client: AuthenticatedClient,
    region_code: Union[Unset, None, str] = UNSET,
    league_code: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, LeagueList]]:
    """League Listings

     The league listings API returns all FTC leagues in a particular season. You can specify a
    `regionCode` to filter to leagues within a particular region. To filter to a specific league, supply
    both a `regionCode` and a `leagueCode`. The returned objects have a `parentLeagueCode` field, which
    indicates the league is a child league if not null and provides the code of the parent league. The
    `regionCode` of the parent league will always match the child.

    Args:
        season (int):
        region_code (Union[Unset, None, str]):
        league_code (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LeagueList]]
    """

    return (
        await asyncio_detailed(
            season=season,
            client=client,
            region_code=region_code,
            league_code=league_code,
        )
    ).parsed
