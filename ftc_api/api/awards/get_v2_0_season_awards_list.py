from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.award_list import AwardList
from ...types import Response


def _get_kwargs(
    season: int,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/v2.0/{season}/awards/list".format(
            season=season,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, AwardList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AwardList.from_dict(response.json())

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
) -> Response[Union[Any, AwardList]]:
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
) -> Response[Union[Any, AwardList]]:
    """Award Listings

     The award listings API returns a listing of the various awards that can be distributed in the
    requested season. This is especially useful in order to avoid having to use the name field of the
    event awards API to know which award was won. Instead the awardId field can be matched between the
    two APIs.

    Args:
        season (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AwardList]]
    """

    kwargs = _get_kwargs(
        season=season,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    season: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, AwardList]]:
    """Award Listings

     The award listings API returns a listing of the various awards that can be distributed in the
    requested season. This is especially useful in order to avoid having to use the name field of the
    event awards API to know which award was won. Instead the awardId field can be matched between the
    two APIs.

    Args:
        season (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AwardList]
    """

    return sync_detailed(
        season=season,
        client=client,
    ).parsed


async def asyncio_detailed(
    season: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, AwardList]]:
    """Award Listings

     The award listings API returns a listing of the various awards that can be distributed in the
    requested season. This is especially useful in order to avoid having to use the name field of the
    event awards API to know which award was won. Instead the awardId field can be matched between the
    two APIs.

    Args:
        season (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AwardList]]
    """

    kwargs = _get_kwargs(
        season=season,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    season: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, AwardList]]:
    """Award Listings

     The award listings API returns a listing of the various awards that can be distributed in the
    requested season. This is especially useful in order to avoid having to use the name field of the
    event awards API to know which award was won. Instead the awardId field can be matched between the
    two APIs.

    Args:
        season (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AwardList]
    """

    return (
        await asyncio_detailed(
            season=season,
            client=client,
        )
    ).parsed
