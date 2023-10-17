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
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/v2.0/{season}/alliances/{eventCode}".format(
            season=season,
            eventCode=event_code,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AllianceSelection, Any]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AllianceSelection.from_dict(response.json())

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
    client: Union[AuthenticatedClient, Client],
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
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    season: int,
    event_code: Optional[str],
    *,
    client: Union[AuthenticatedClient, Client],
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
        Union[AllianceSelection, Any]
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
    client: Union[AuthenticatedClient, Client],
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
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    season: int,
    event_code: Optional[str],
    *,
    client: Union[AuthenticatedClient, Client],
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
        Union[AllianceSelection, Any]
    """

    return (
        await asyncio_detailed(
            season=season,
            event_code=event_code,
            client=client,
        )
    ).parsed
