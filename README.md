# FTC api
A client library for accessing FTC Events API

## Usage
First, create a client:

```python
from ftc_api import Client

client = Client(token="Insert Token Here")
```

Now call your endpoint and use your models:

```python
from ftc_api.models import MyDataModel
from ftc_api.api.my_tag import get_my_data_model
from ftc_api.types import Response

my_data: MyDataModel = get_my_data_model.sync(client=client)
# or if you need more info (e.g. status_code)
response: Response[MyDataModel] = get_my_data_model.sync_detailed(client=client)
```

Or do the same thing with an async version:

```python
from ftc_api.models import MyDataModel
from ftc_api.api.my_tag import get_my_data_model
from ftc_api.types import Response

my_data: MyDataModel = await get_my_data_model.asyncio(client=client)
response: Response[MyDataModel] = await get_my_data_model.asyncio_detailed(client=client)
```

By default, when you're calling an HTTPS API it will attempt to verify that SSL is working correctly. Using certificate verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.

```python
client = Client(
    token="SuperSecretToken",
    verify_ssl="/path/to/certificate_bundle.pem",
)
```

You can also disable certificate validation altogether, but beware that **this is a security risk**.

```python
client = Client(
    token="Token", 
    verify_ssl=False
)
```

There are more settings on the generated `Client` class which let you control more runtime behavior, check out the docstring on that class for more info.

Things to know:
1. Every path/method combo becomes a Python module with four functions:
    1. `sync`: Blocking request that returns parsed data (if successful) or `None`
    2. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
    3. `asyncio`: Like `sync` but async instead of blocking
    4. `asyncio_detailed`: Like `sync_detailed` but async instead of blocking

2. All path/query params, and bodies become method arguments.
3. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)
4. Any endpoint which did not have a tag will be in `ftc_events_api_client.api.default`

