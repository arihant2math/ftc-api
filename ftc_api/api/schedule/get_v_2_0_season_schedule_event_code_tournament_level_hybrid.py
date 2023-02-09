from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ftc_api import errors
from ftc_api.client import AuthenticatedClient, Client
from ftc_api.models.get_v20_season_schedule_event_code_tournament_level_hybrid_tournament_level import (
    GetV20SeasonScheduleEventCodeTournamentLevelHybridTournamentLevel,
)
from ftc_api.models.hybrid_schedule import HybridSchedule
from ftc_api.types import UNSET, Response, Unset


def _get_kwargs(
    season: int,
    event_code: Optional[str],
    tournament_level: Optional[
        GetV20SeasonScheduleEventCodeTournamentLevelHybridTournamentLevel
    ],
    *,
    client: AuthenticatedClient,
    start: Union[Unset, None, int] = 0,
    end: Union[Unset, None, int] = 999,
) -> Dict[str, Any]:
    url = "{}/v2.0/{season}/schedule/{eventCode}/{tournamentLevel}/hybrid".format(
        "https://ftc-api.firstinspires.org",
        season=season,
        eventCode=event_code,
        tournamentLevel=tournament_level,
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["start"] = start

    params["end"] = end

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
) -> Optional[Union[Any, HybridSchedule]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = HybridSchedule.from_dict(response.json())

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
) -> Response[Union[Any, HybridSchedule]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    season: int,
    event_code: Optional[str],
    tournament_level: Optional[
        GetV20SeasonScheduleEventCodeTournamentLevelHybridTournamentLevel
    ],
    *,
    client: AuthenticatedClient,
    start: Union[Unset, None, int] = 0,
    end: Union[Unset, None, int] = 999,
) -> Response[Union[Any, HybridSchedule]]:
    """Hybrid Schedule

     The schedule API returns the match schedule for the desired tournament level of a particular event
    in a particular season in the hybrid format. When a match has been played, the match result related
    details will be filled. When a match has not yet happened, match result related fields will be null.
    All parameters, except start and end, are required for the hybrid schedule.

    Args:
        season (int):
        event_code (Optional[str]):
        tournament_level
            (Optional[GetV20SeasonScheduleEventCodeTournamentLevelHybridTournamentLevel]):
        start (Union[Unset, None, int]):
        end (Union[Unset, None, int]):  Default: 999.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HybridSchedule]]
    """

    kwargs = _get_kwargs(
        season=season,
        event_code=event_code,
        tournament_level=tournament_level,
        client=client,
        start=start,
        end=end,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    season: int,
    event_code: Optional[str],
    tournament_level: Optional[
        GetV20SeasonScheduleEventCodeTournamentLevelHybridTournamentLevel
    ],
    *,
    client: AuthenticatedClient,
    start: Union[Unset, None, int] = 0,
    end: Union[Unset, None, int] = 999,
) -> Optional[Union[Any, HybridSchedule]]:
    """Hybrid Schedule

     The schedule API returns the match schedule for the desired tournament level of a particular event
    in a particular season in the hybrid format. When a match has been played, the match result related
    details will be filled. When a match has not yet happened, match result related fields will be null.
    All parameters, except start and end, are required for the hybrid schedule.

    Args:
        season (int):
        event_code (Optional[str]):
        tournament_level
            (Optional[GetV20SeasonScheduleEventCodeTournamentLevelHybridTournamentLevel]):
        start (Union[Unset, None, int]):
        end (Union[Unset, None, int]):  Default: 999.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HybridSchedule]]
    """

    return sync_detailed(
        season=season,
        event_code=event_code,
        tournament_level=tournament_level,
        client=client,
        start=start,
        end=end,
    ).parsed


async def asyncio_detailed(
    season: int,
    event_code: Optional[str],
    tournament_level: Optional[
        GetV20SeasonScheduleEventCodeTournamentLevelHybridTournamentLevel
    ],
    *,
    client: AuthenticatedClient,
    start: Union[Unset, None, int] = 0,
    end: Union[Unset, None, int] = 999,
) -> Response[Union[Any, HybridSchedule]]:
    """Hybrid Schedule

     The schedule API returns the match schedule for the desired tournament level of a particular event
    in a particular season in the hybrid format. When a match has been played, the match result related
    details will be filled. When a match has not yet happened, match result related fields will be null.
    All parameters, except start and end, are required for the hybrid schedule.

    Args:
        season (int):
        event_code (Optional[str]):
        tournament_level
            (Optional[GetV20SeasonScheduleEventCodeTournamentLevelHybridTournamentLevel]):
        start (Union[Unset, None, int]):
        end (Union[Unset, None, int]):  Default: 999.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HybridSchedule]]
    """

    kwargs = _get_kwargs(
        season=season,
        event_code=event_code,
        tournament_level=tournament_level,
        client=client,
        start=start,
        end=end,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    season: int,
    event_code: Optional[str],
    tournament_level: Optional[
        GetV20SeasonScheduleEventCodeTournamentLevelHybridTournamentLevel
    ],
    *,
    client: AuthenticatedClient,
    start: Union[Unset, None, int] = 0,
    end: Union[Unset, None, int] = 999,
) -> Optional[Union[Any, HybridSchedule]]:
    """Hybrid Schedule

     The schedule API returns the match schedule for the desired tournament level of a particular event
    in a particular season in the hybrid format. When a match has been played, the match result related
    details will be filled. When a match has not yet happened, match result related fields will be null.
    All parameters, except start and end, are required for the hybrid schedule.

    Args:
        season (int):
        event_code (Optional[str]):
        tournament_level
            (Optional[GetV20SeasonScheduleEventCodeTournamentLevelHybridTournamentLevel]):
        start (Union[Unset, None, int]):
        end (Union[Unset, None, int]):  Default: 999.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HybridSchedule]]
    """

    return (
        await asyncio_detailed(
            season=season,
            event_code=event_code,
            tournament_level=tournament_level,
            client=client,
            start=start,
            end=end,
        )
    ).parsed
