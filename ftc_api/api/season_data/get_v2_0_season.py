from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.season_summary import SeasonSummary
from ...types import Response


def _get_kwargs(
    season: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/v2.0/{season}".format("https://ftc-api.firstinspires.org", season=season)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, SeasonSummary]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SeasonSummary.from_dict(response.json())

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
) -> Response[Union[Any, SeasonSummary]]:
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
) -> Response[Union[Any, SeasonSummary]]:
    """Season Summary

     The season summary API returns a high level glance of a particular FTC season.

    Args:
        season (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SeasonSummary]]
    """

    kwargs = _get_kwargs(
        season=season,
        client=client,
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
) -> Optional[Union[Any, SeasonSummary]]:
    """Season Summary

     The season summary API returns a high level glance of a particular FTC season.

    Args:
        season (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SeasonSummary]]
    """

    return sync_detailed(
        season=season,
        client=client,
    ).parsed


async def asyncio_detailed(
    season: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, SeasonSummary]]:
    """Season Summary

     The season summary API returns a high level glance of a particular FTC season.

    Args:
        season (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SeasonSummary]]
    """

    kwargs = _get_kwargs(
        season=season,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    season: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, SeasonSummary]]:
    """Season Summary

     The season summary API returns a high level glance of a particular FTC season.

    Args:
        season (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SeasonSummary]]
    """

    return (
        await asyncio_detailed(
            season=season,
            client=client,
        )
    ).parsed
