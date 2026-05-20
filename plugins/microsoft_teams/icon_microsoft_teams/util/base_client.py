import time
from typing import Union

import requests
from logging import Logger
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_microsoft_teams.util.constants import TIMEOUT, HTTP_ERROR_MAP

DEFAULT_TOKEN_LIFETIME = 3500


class BaseClient:
    """
    Base API client providing shared authentication and request functionality.

    Subclasses (GraphApiClient, BotService) inherit common patterns:
    - OAuth2 client_credentials token acquisition and refresh
    - Centralized HTTP request handling with timeout/connection error handling
    - HTTP status code to PluginException mapping
    - Automatic token refresh on expiry
    """

    def __init__(  # pylint: disable=too-many-arguments,too-many-positional-arguments
        self,
        app_id: str,
        app_secret: str,
        tenant_id: str,
        auth_url: str,
        scope: str,
        logger: Logger,
    ):
        """
        Initialize the base client.

        :param app_id: Azure App Registration client ID
        :param app_secret: Azure App Registration client secret
        :param tenant_id: Azure AD tenant ID
        :param auth_url: Base auth URL (e.g., https://login.microsoftonline.com)
        :param scope: OAuth2 scope for token request
        :param logger: Logger instance
        """
        self._app_id = app_id
        self._app_secret = app_secret
        self._tenant_id = tenant_id
        self._auth_url = auth_url
        self._scope = scope
        self._logger = logger
        self._token = None
        self._token_acquired_at = 0
        self._token_lifetime = DEFAULT_TOKEN_LIFETIME

    def _authenticate(self):
        """Acquire an OAuth2 access token using client_credentials flow."""
        token_url = f"{self._auth_url}/{self._tenant_id}/oauth2/v2.0/token"

        body = {
            "grant_type": "client_credentials",
            "client_id": self._app_id,
            "client_secret": self._app_secret,
            "scope": self._scope,
        }

        self._logger.info(f"Authenticating via: {token_url}")

        try:
            response = requests.post(token_url, data=body, timeout=TIMEOUT)

            if response.status_code != 200:
                raise PluginException(
                    cause="Authentication failed",
                    assistance="Please verify your Application ID, Directory ID, and Application Secret are correct. "
                    "Ensure the app registration has the required permissions with admin consent granted.",
                    data=response.text,
                )

            result_json = response.json()
            self._token = result_json.get("access_token")

            # Use expires_in from token response if available, with a 60-second buffer
            expires_in = result_json.get("expires_in")
            if expires_in:
                self._token_lifetime = int(expires_in) - 60
            else:
                self._token_lifetime = DEFAULT_TOKEN_LIFETIME

        except PluginException:
            raise
        except requests.exceptions.Timeout as error:
            raise PluginException(
                cause="Authentication request timed out",
                assistance="Please verify network connectivity and try again.",
                data=str(error),
            ) from error
        except requests.exceptions.ConnectionError as error:
            raise PluginException(
                cause="Unable to connect to authentication endpoint",
                assistance=f"Could not connect to {token_url}. Please verify network connectivity.",
                data=str(error),
            ) from error
        except (ValueError, KeyError) as error:
            raise PluginException(
                cause="Failed to parse authentication response",
                assistance="Unexpected response from the token endpoint.",
                data=str(error),
            ) from error

        self._token_acquired_at = time.time()
        self._logger.info(f"Authentication successful, token: ******************{self._token[-5:]}")

    def _get_token(self, force_refresh: bool = False) -> str:
        """Get a valid access token, refreshing if expired."""
        elapsed = time.time() - self._token_acquired_at
        if not self._token or elapsed > self._token_lifetime or force_refresh:
            self._authenticate()
        return self._token

    def authenticate(self):
        """Public method to trigger authentication. Used by connection test."""
        self._authenticate()

    def get_auth_headers(self, force_refresh: bool = False) -> dict:
        """Public method to get authorization headers."""
        return self._get_auth_headers(force_refresh)

    def _get_auth_headers(self, force_refresh: bool = False) -> dict:
        """Get authorization headers with a valid bearer token."""
        token = self._get_token(force_refresh)
        return {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    def _call_api(self, method: str, url: str, **kwargs) -> requests.Response:
        """
        Make an HTTP request with timeout and connection error handling.

        :param method: HTTP method
        :param url: Full URL to call
        :param kwargs: Additional arguments passed to requests
        :return: Response object
        """
        try:
            return requests.request(method=method, url=url, timeout=TIMEOUT, **kwargs)
        except requests.exceptions.Timeout as error:
            raise PluginException(
                cause="Request timed out",
                assistance=f"The request to {url} timed out after {TIMEOUT} seconds. "
                "Please verify network connectivity and try again.",
                data=str(error),
            ) from error
        except requests.exceptions.ConnectionError as error:
            raise PluginException(
                cause="Unable to connect",
                assistance=f"Could not connect to {url}. "
                "Please verify network connectivity and that the endpoint is correct.",
                data=str(error),
            ) from error

    def _handle_json_response(self, response: requests.Response) -> Union[dict, list, None]:
        """Parse a JSON response, raising PluginException on error status codes."""
        if response.status_code == 204:
            return None

        if response.status_code >= 400:
            self._raise_for_status(response)

        if not response.content:
            return None

        try:
            return response.json()
        except ValueError as error:
            raise PluginException(
                cause="Non-JSON response received",
                assistance="The server returned a response that could not be parsed as JSON.",
                data=response.text[:500],
            ) from error

    def _raise_for_status(self, response: requests.Response):
        """Map HTTP error codes to PluginExceptions using the shared error map."""
        status_code = response.status_code
        error_info = HTTP_ERROR_MAP.get(status_code)

        if error_info:
            raise PluginException(
                cause=error_info["cause"],
                assistance=error_info["assistance"],
                data=response.text[:1000],
            )

        raise PluginException(
            cause=f"Unexpected HTTP error: {status_code}",
            assistance="An unexpected error occurred. Please contact support if this persists.",
            data=response.text[:1000],
        )
