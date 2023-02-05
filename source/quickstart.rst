Quickstart
===========
First, create a client:

.. code:: python

    from ftc_api import Client

    client = Client(token="Insert Token Here")


Alternatively, use your username and access key, and the token will be automatically generated:

.. code:: python

    from ftc_api import Client

    client = Client(username="test", authorization_key="****-****-****-****")

Now call your endpoint and use your models:

.. code:: python

    from ftc_api.api.season_data import get_v2_0_season
    import ftc_api

    client = ftc_api.Client(username="test", authorization_key="****-****-****-****")
    my_data = get_v2_0_season.sync(client=client, season=2022)
    print(my_data.game_name) # POWERPLAY
    # or if you need more info (e.g. status_code)
    response = get_v2_0_season.sync_detailed(client=client, season=2022)
    print(response.headers) # server headers
    print(response.content) # raw json

Or do the same thing with an async version:

.. code:: python

    from ftc_api.api.season_data import get_v2_0_season
    import ftc_api

    client = ftc_api.Client(username="test", authorization_key="****-****-****-****")
    my_data = await get_v2_0_season.asyncio(client=client, season=2022)
    print(my_data.game_name) # POWERPLAY
    # or if you need more info (e.g. status_code)
    response = await get_v2_0_season.asyncio(client=client, season=2022)
    print(response.headers) # server headers
    print(response.content) # raw json



Things to know
_____________________

1. Every path/method combo becomes a Python module with four functions:
2. ``sync``: Blocking request that returns parsed data (if successful) or ``None``
3. ``sync_detailed``: Blocking request that always returns a httpx ``Request``, optionally with ``parsed`` set if the request was successful.
4. ``asyncio``: Like ``sync`` but async instead of blocking
5. ``asyncio_detailed``: Like ``sync_detailed`` but async instead of blocking
6. All path/query params, and bodies become method arguments
7. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)
8. Any endpoint which did not have a tag will be in ``ftc_events_api_client.api.default``
