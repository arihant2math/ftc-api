import base64
import ssl
import warnings
from typing import Dict, Union


class Client:
    """A class for keeping track of data related to the API

    Attributes:
        cookies: A dictionary of cookies to be sent with every request
        headers: A dictionary of headers to be sent with every request
        timeout: The maximum amount of a time in seconds a request can take. API functions will raise
            httpx.TimeoutException if this is exceeded.
        verify_ssl: Whether or not to verify the SSL certificate of the API server. This should be True in production,
            but can be set to False for testing purposes.
        raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns a
            status code that was not documented in the source OpenAPI document.
    """

    cookies = {}
    headers: Dict[str, str] = {}
    timeout: float = 5.0
    verify_ssl: Union[str, bool, ssl.SSLContext] = True
    raise_on_unexpected_status: bool = False
    prefix: str = "Basic"
    auth_header_name: str = "Authorization"

    def __init__(self, token=None, username="", authorization_key=""):
        if token is not None:
            self.token = token
        else:
            token = username + ":" + authorization_key
            token_bytes = token.encode("ascii")
            base64_bytes = base64.b64encode(token_bytes)
            self.token = base64_bytes.decode("ascii")

    def get_headers(self) -> Dict[str, str]:
        auth_header_value = f"{self.prefix} {self.token}" if self.prefix else self.token
        """Get headers to be used in authenticated endpoints"""
        return {self.auth_header_name: auth_header_value, **self.headers}

    def get_cookies(self) -> Dict[str, str]:
        return {**self.cookies}

    def get_timeout(self) -> float:
        return self.timeout


class AuthenticatedClient(Client):
    """Deprecated, use Client instead, as it has equivalent functionality, will be removed v1.0.0"""
    warnings.warn("Will be removed v1.0.0 switch to Client because the functionality has been merged.",
                  DeprecationWarning)
