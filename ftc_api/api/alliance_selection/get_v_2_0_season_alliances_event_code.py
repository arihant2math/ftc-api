from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alliance_selection import AllianceSelection
from ...types import Response


def _get_kwargs(
    season: int,
    event_code: Optional[str],
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/v2.0/{season}/alliances/{eventCode}".format(
        "https://ftc-api.firstinspires.org", season=season, eventCode=event_code
    )

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
) -> Optional[Union[AllianceSelection, Any]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AllianceSelection.from_dict(response.json())

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
) -> Response[Union[AllianceSelection, Any]]:
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
) -> Response[Union[AllianceSelection, Any]]:
    """Event Alliances

     The alliances API returns details about alliance selection at a particular event in a particular
    season.

    Args:
        season (int):
        event_code (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AllianceSelection, Any]]
    """

    kwargs = _get_kwargs(
        season=season,
        event_code=event_code,
        client=client,
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
) -> Optional[Union[AllianceSelection, Any]]:
    """Event Alliances

     The alliances API returns details about alliance selection at a particular event in a particular
    season.

    Args:
        season (int):
        event_code (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AllianceSelection, Any]]
    """

    return sync_detailed(
        season=season,
        event_code=event_code,
        client=client,
    ).parsed


async def asyncio_detailed(
    season: int,
    event_code: Optional[str],
    *,
    client: AuthenticatedClient,
) -> Response[Union[AllianceSelection, Any]]:
    """Event Alliances

     The alliances API returns details about alliance selection at a particular event in a particular
    season.

    Args:
        season (int):
        event_code (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AllianceSelection, Any]]
    """

    kwargs = _get_kwargs(
        season=season,
        event_code=event_code,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    season: int,
    event_code: Optional[str],
    *,
    client: AuthenticatedClient,
) -> Optional[Union[AllianceSelection, Any]]:
    """Event Alliances

     The alliances API returns details about alliance selection at a particular event in a particular
    season.

    Args:
        season (int):
        event_code (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AllianceSelection, Any]]
    """

    return (
        await asyncio_detailed(
            season=season,
            event_code=event_code,
            client=client,
        )
    ).parsed
