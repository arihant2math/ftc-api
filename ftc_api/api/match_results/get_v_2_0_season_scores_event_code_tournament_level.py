from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v20_season_scores_event_code_tournament_level_tournament_level import (
    GetV20SeasonScoresEventCodeTournamentLevelTournamentLevel,
)
from ...models.match_score_list import MatchScoreList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    season: int,
    event_code: Optional[str],
    tournament_level: Optional[
        GetV20SeasonScoresEventCodeTournamentLevelTournamentLevel
    ],
    *,
    client: AuthenticatedClient,
    team_number: Union[Unset, None, int] = UNSET,
    match_number: Union[Unset, None, int] = UNSET,
    start: Union[Unset, None, int] = 0,
    end: Union[Unset, None, int] = 999,
) -> Dict[str, Any]:
    url = "{}/v2.0/{season}/scores/{eventCode}/{tournamentLevel}".format(
        "https://ftc-api.firstinspires.org",
        season=season,
        eventCode=event_code,
        tournamentLevel=tournament_level,
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["teamNumber"] = team_number

    params["matchNumber"] = match_number

    params["start"] = start

    params["end"] = end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "http2": client.http2,
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, MatchScoreList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = MatchScoreList.from_dict(response.json())

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
) -> Response[Union[Any, MatchScoreList]]:
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
        GetV20SeasonScoresEventCodeTournamentLevelTournamentLevel
    ],
    *,
    client: AuthenticatedClient,
    team_number: Union[Unset, None, int] = UNSET,
    match_number: Union[Unset, None, int] = UNSET,
    start: Union[Unset, None, int] = 0,
    end: Union[Unset, None, int] = 999,
) -> Response[Union[Any, MatchScoreList]]:
    """Score Details

     The score details API returns the score detail for all matches of a particular event in a particular
    season and a particular tournament level. Score details are only available once a match has been
    played, retrieving info about future matches requires the event schedule API. You cannot receive
    data about a match that is in progress.

    Args:
        season (int):
        event_code (Optional[str]):
        tournament_level (Optional[GetV20SeasonScoresEventCodeTournamentLevelTournamentLevel]):
        team_number (Union[Unset, None, int]):
        match_number (Union[Unset, None, int]):
        start (Union[Unset, None, int]):
        end (Union[Unset, None, int]):  Default: 999.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MatchScoreList]]
    """

    kwargs = _get_kwargs(
        season=season,
        event_code=event_code,
        tournament_level=tournament_level,
        client=client,
        team_number=team_number,
        match_number=match_number,
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
        GetV20SeasonScoresEventCodeTournamentLevelTournamentLevel
    ],
    *,
    client: AuthenticatedClient,
    team_number: Union[Unset, None, int] = UNSET,
    match_number: Union[Unset, None, int] = UNSET,
    start: Union[Unset, None, int] = 0,
    end: Union[Unset, None, int] = 999,
) -> Optional[Union[Any, MatchScoreList]]:
    """Score Details

     The score details API returns the score detail for all matches of a particular event in a particular
    season and a particular tournament level. Score details are only available once a match has been
    played, retrieving info about future matches requires the event schedule API. You cannot receive
    data about a match that is in progress.

    Args:
        season (int):
        event_code (Optional[str]):
        tournament_level (Optional[GetV20SeasonScoresEventCodeTournamentLevelTournamentLevel]):
        team_number (Union[Unset, None, int]):
        match_number (Union[Unset, None, int]):
        start (Union[Unset, None, int]):
        end (Union[Unset, None, int]):  Default: 999.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MatchScoreList]]
    """

    return sync_detailed(
        season=season,
        event_code=event_code,
        tournament_level=tournament_level,
        client=client,
        team_number=team_number,
        match_number=match_number,
        start=start,
        end=end,
    ).parsed


async def asyncio_detailed(
    season: int,
    event_code: Optional[str],
    tournament_level: Optional[
        GetV20SeasonScoresEventCodeTournamentLevelTournamentLevel
    ],
    *,
    client: AuthenticatedClient,
    team_number: Union[Unset, None, int] = UNSET,
    match_number: Union[Unset, None, int] = UNSET,
    start: Union[Unset, None, int] = 0,
    end: Union[Unset, None, int] = 999,
) -> Response[Union[Any, MatchScoreList]]:
    """Score Details

     The score details API returns the score detail for all matches of a particular event in a particular
    season and a particular tournament level. Score details are only available once a match has been
    played, retrieving info about future matches requires the event schedule API. You cannot receive
    data about a match that is in progress.

    Args:
        season (int):
        event_code (Optional[str]):
        tournament_level (Optional[GetV20SeasonScoresEventCodeTournamentLevelTournamentLevel]):
        team_number (Union[Unset, None, int]):
        match_number (Union[Unset, None, int]):
        start (Union[Unset, None, int]):
        end (Union[Unset, None, int]):  Default: 999.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MatchScoreList]]
    """

    kwargs = _get_kwargs(
        season=season,
        event_code=event_code,
        tournament_level=tournament_level,
        client=client,
        team_number=team_number,
        match_number=match_number,
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
        GetV20SeasonScoresEventCodeTournamentLevelTournamentLevel
    ],
    *,
    client: AuthenticatedClient,
    team_number: Union[Unset, None, int] = UNSET,
    match_number: Union[Unset, None, int] = UNSET,
    start: Union[Unset, None, int] = 0,
    end: Union[Unset, None, int] = 999,
) -> Optional[Union[Any, MatchScoreList]]:
    """Score Details

     The score details API returns the score detail for all matches of a particular event in a particular
    season and a particular tournament level. Score details are only available once a match has been
    played, retrieving info about future matches requires the event schedule API. You cannot receive
    data about a match that is in progress.

    Args:
        season (int):
        event_code (Optional[str]):
        tournament_level (Optional[GetV20SeasonScoresEventCodeTournamentLevelTournamentLevel]):
        team_number (Union[Unset, None, int]):
        match_number (Union[Unset, None, int]):
        start (Union[Unset, None, int]):
        end (Union[Unset, None, int]):  Default: 999.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MatchScoreList]]
    """

    return (
        await asyncio_detailed(
            season=season,
            event_code=event_code,
            tournament_level=tournament_level,
            client=client,
            team_number=team_number,
            match_number=match_number,
            start=start,
            end=end,
        )
    ).parsed
