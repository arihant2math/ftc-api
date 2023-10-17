from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.league_members import LeagueMembers
from ...types import Response


def _get_kwargs(
    season: int,
    region_code: Optional[str],
    league_code: Optional[str],
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/v2.0/{season}/leagues/members/{regionCode}/{leagueCode}".format(
            season=season,
            regionCode=region_code,
            leagueCode=league_code,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, LeagueMembers]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = LeagueMembers.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, LeagueMembers]]:
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
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, LeagueMembers]]:
    """League Membership

     The league membership API returns the list of team numbers for the teams that are members of a
    particular league. Leagues are specified by a `regionCode` in combination with a `leagueCode`.

    Args:
        season (int):
        region_code (Optional[str]):
        league_code (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LeagueMembers]]
    """

    kwargs = _get_kwargs(
        season=season,
        region_code=region_code,
        league_code=league_code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    season: int,
    region_code: Optional[str],
    league_code: Optional[str],
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, LeagueMembers]]:
    """League Membership

     The league membership API returns the list of team numbers for the teams that are members of a
    particular league. Leagues are specified by a `regionCode` in combination with a `leagueCode`.

    Args:
        season (int):
        region_code (Optional[str]):
        league_code (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, LeagueMembers]
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
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, LeagueMembers]]:
    """League Membership

     The league membership API returns the list of team numbers for the teams that are members of a
    particular league. Leagues are specified by a `regionCode` in combination with a `leagueCode`.

    Args:
        season (int):
        region_code (Optional[str]):
        league_code (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LeagueMembers]]
    """

    kwargs = _get_kwargs(
        season=season,
        region_code=region_code,
        league_code=league_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    season: int,
    region_code: Optional[str],
    league_code: Optional[str],
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, LeagueMembers]]:
    """League Membership

     The league membership API returns the list of team numbers for the teams that are members of a
    particular league. Leagues are specified by a `regionCode` in combination with a `leagueCode`.

    Args:
        season (int):
        region_code (Optional[str]):
        league_code (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, LeagueMembers]
    """

    return (
        await asyncio_detailed(
            season=season,
            region_code=region_code,
            league_code=league_code,
            client=client,
        )
    ).parsed
