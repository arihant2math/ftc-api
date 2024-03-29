from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.award_assignment_list import AwardAssignmentList
from ...types import Response


def _get_kwargs(
    season: int,
    event_code: Optional[str] = "",
    team_number: int = 0,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/v2.0/{season}/awards/{eventCode}/{teamNumber}".format(
            season=season,
            eventCode=event_code,
            teamNumber=team_number,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, AwardAssignmentList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AwardAssignmentList.from_dict(response.json())

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
) -> Response[Union[Any, AwardAssignmentList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    season: int,
    event_code: Optional[str] = "",
    team_number: int = 0,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, AwardAssignmentList]]:
    """Event Awards

     The event awards API returns details about awards presented at a particular event in a particular
    season. Return values may contain either `teamNumber` or `person` values, and if the winner was a
    `person`, and that person is from a team, the `teamNumber` value *might* be set with their
    `teamNumber`. You must specify either an `eventCode` or a `teamNumber` or both. If you specify the
    `teamNumber` parameter, you will receive only awards where the team was listed as the winner,
    regardless of whether or not the `person` field is `null` or empty. If you specify only the
    `eventCode` field, you will receive all award listings for the requested event. If you specify both,
    you will receive all awards won by the `teamNumber` at the `eventCode`.

    Args:
        season (int):
        event_code (Optional[str]):  Default: ''.
        team_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AwardAssignmentList]]
    """

    kwargs = _get_kwargs(
        season=season,
        event_code=event_code,
        team_number=team_number,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    season: int,
    event_code: Optional[str] = "",
    team_number: int = 0,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, AwardAssignmentList]]:
    """Event Awards

     The event awards API returns details about awards presented at a particular event in a particular
    season. Return values may contain either `teamNumber` or `person` values, and if the winner was a
    `person`, and that person is from a team, the `teamNumber` value *might* be set with their
    `teamNumber`. You must specify either an `eventCode` or a `teamNumber` or both. If you specify the
    `teamNumber` parameter, you will receive only awards where the team was listed as the winner,
    regardless of whether or not the `person` field is `null` or empty. If you specify only the
    `eventCode` field, you will receive all award listings for the requested event. If you specify both,
    you will receive all awards won by the `teamNumber` at the `eventCode`.

    Args:
        season (int):
        event_code (Optional[str]):  Default: ''.
        team_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AwardAssignmentList]
    """

    return sync_detailed(
        season=season,
        event_code=event_code,
        team_number=team_number,
        client=client,
    ).parsed


async def asyncio_detailed(
    season: int,
    event_code: Optional[str] = "",
    team_number: int = 0,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, AwardAssignmentList]]:
    """Event Awards

     The event awards API returns details about awards presented at a particular event in a particular
    season. Return values may contain either `teamNumber` or `person` values, and if the winner was a
    `person`, and that person is from a team, the `teamNumber` value *might* be set with their
    `teamNumber`. You must specify either an `eventCode` or a `teamNumber` or both. If you specify the
    `teamNumber` parameter, you will receive only awards where the team was listed as the winner,
    regardless of whether or not the `person` field is `null` or empty. If you specify only the
    `eventCode` field, you will receive all award listings for the requested event. If you specify both,
    you will receive all awards won by the `teamNumber` at the `eventCode`.

    Args:
        season (int):
        event_code (Optional[str]):  Default: ''.
        team_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AwardAssignmentList]]
    """

    kwargs = _get_kwargs(
        season=season,
        event_code=event_code,
        team_number=team_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    season: int,
    event_code: Optional[str] = "",
    team_number: int = 0,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, AwardAssignmentList]]:
    """Event Awards

     The event awards API returns details about awards presented at a particular event in a particular
    season. Return values may contain either `teamNumber` or `person` values, and if the winner was a
    `person`, and that person is from a team, the `teamNumber` value *might* be set with their
    `teamNumber`. You must specify either an `eventCode` or a `teamNumber` or both. If you specify the
    `teamNumber` parameter, you will receive only awards where the team was listed as the winner,
    regardless of whether or not the `person` field is `null` or empty. If you specify only the
    `eventCode` field, you will receive all award listings for the requested event. If you specify both,
    you will receive all awards won by the `teamNumber` at the `eventCode`.

    Args:
        season (int):
        event_code (Optional[str]):  Default: ''.
        team_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AwardAssignmentList]
    """

    return (
        await asyncio_detailed(
            season=season,
            event_code=event_code,
            team_number=team_number,
            client=client,
        )
    ).parsed
