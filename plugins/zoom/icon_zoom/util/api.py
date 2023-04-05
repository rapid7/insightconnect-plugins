import json
from logging import Logger
from typing import Optional

import requests
from requests.auth import HTTPBasicAuth
from requests.auth import AuthBase
from requests import Response

from insightconnect_plugin_runtime.exceptions import PluginException


class BearerAuth(AuthBase):
    """
    Authentication class for Bearer auth
    """

    def __init__(self, access_token: str):
        self.access_token = access_token

    def __call__(self, request: requests.Request):
        request.headers["Authorization"] = f"Bearer {self.access_token}"
        return request


class ZoomAPI:
    def __init__(
        self,
        logger: Logger,
        account_id: Optional[str] = None,  # For OAuth only
        client_id: Optional[str] = None,  # For OAuth only
        client_secret: Optional[str] = None,  # For OAuth only
        jwt_token: Optional[str] = None,
    ):  # For JWT auth only
        self.api_url = "https://api.zoom.us/v2"
        self.oauth_url = "https://zoom.us/oauth/token"
        self.account_id = account_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.jwt_token = jwt_token
        self.logger = logger

        self.oauth_token: Optional[str] = None

        # JWT is -not- being used, so get an OAuth token
        if not jwt_token:
            self._refresh_oauth_token()

    def get_user(self, user_id: str) -> Optional[dict]:
        return self._call_api("GET", f"{self.api_url}/users/{user_id}")

    def create_user(self, payload: dict) -> Optional[dict]:
        return self._call_api("POST", f"{self.api_url}/users", json_data=payload)

    def delete_user(self, user_id: str, params: dict) -> Optional[dict]:
        return self._call_api("DELETE", f"{self.api_url}/users/{user_id}", params=params)

    def get_user_activity_events(
        self, start_date: str = None, end_date: str = None, page_size: int = None, next_page_token: str = None
    ) -> [dict]:
        activities_url = f"{self.api_url}/report/activities"

        events = []
        params = {
            "from": start_date,
            "to": end_date,
            "page_size": page_size,
            "next_page_token": next_page_token,
        }

        while True:
            response = self._call_api("GET", activities_url, params=params)

            events = events + response.get("activity_logs", [])

            if "next_page_token" in response and response.get("next_page_token") != "":
                params["next_page_token"] = response.get("next_page_token")
            else:
                return events

    def _refresh_oauth_token(self):
        """
        Retrieves a new server-to-server OAuth token from Zoom
        :return: None
        """
        params = {"grant_type": "account_credentials", "account_id": self.account_id}
        auth = HTTPBasicAuth(self.client_id, self.client_secret)

        try:
            self.logger.info("Calling Zoom API to refresh OAuth token...")
            # Attempt to refresh OAuth token with 2-minute timeout
            response = requests.post("https://zoom.us/oauth/token", params=params, auth=auth, timeout=120)

            # Handle known status codes
            codes = {
                400: PluginException(preset=PluginException.Preset.BAD_REQUEST),
                401: PluginException(preset=PluginException.Preset.UNAUTHORIZED),
                403: PluginException(
                    cause="Configured credentials do not have permission for this API endpoint.",
                    assistance="Please ensure credentials have required permissions.",
                ),
                429: self._handle_rate_limit_error(response),
                4700: PluginException(
                    cause="Configured credentials do not have permission for this API endpoint.",
                    assistance="Please ensure credentials have required permissions.",
                ),
            }

            self.logger.info(f"Got status code {response.status_code} from OAuth token refresh")
            for key, value in codes:
                if response.status_code == key:
                    raise value

            # Handle unknown status codes
            if response.status_code in range(0, 199) or response.status_code >= 300:
                raise PluginException(preset=PluginException.Preset.UNKNOWN)

        except requests.exceptions.HTTPError as error:
            self.logger.info(f"Request to get OAuth token failed: {error}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN)

        except requests.exceptions.Timeout as error:
            self.logger.info(f"Request to get OAuth token timed out: {error}")
            raise PluginException(preset=PluginException.Preset.TIMEOUT)

        try:
            response_data = response.json()
        except json.decoder.JSONDecodeError as error:
            self.logger.info(f"Invalid JSON response was received while refreshing OAuth token: {error}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)

        try:
            access_token = response_data["access_token"]
        except KeyError:
            raise PluginException(
                cause=f"Unable to get access token: {response_data.get('reason', '')}.",
                assistance="Ensure your connection configuration is using correct credentials.",
            )

        self.logger.info("Request for new OAuth token was successful!")
        self.oauth_token = access_token

    def _call_api(
        self,
        method: str,
        url: str,
        params: dict = None,
        json_data: dict = None,
        allow_404: bool = False,
    ) -> Optional[dict]:  # noqa: MC0001
        # Determine which type of authentication mechanism to use
        if self.oauth_token:
            auth = BearerAuth(access_token=self.oauth_token)
        else:
            auth = BearerAuth(access_token=self.jwt_token)

        try:
            self.logger.info(f"Calling {method} {url}")
            response = requests.request(method, url, json=json_data, params=params, auth=auth)
            self.logger.info(f"Got response status code: {response.status_code}")

            if response.status_code in [400, 401, 404, 409, 429, 204] or (200 <= response.status_code < 300):
                return self._handle_response(
                    response=response,
                    allow_404=allow_404,
                    original_call_args={
                        "method": method,
                        "url": url,
                        "params": params,
                        "json_data": json_data,
                        "allow_404": allow_404,
                    },
                )

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as error:
            self.logger.info(f"Invalid JSON: {error}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)
        except requests.exceptions.HTTPError as error:
            self.logger.info(f"Request to {url} failed: {error}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN)

    def _handle_response(self, response: Response, allow_404: bool, original_call_args: dict):
        """
        Helper function to process the response based on the status code returned.
        :param response: Response object
        :param allow_404: Boolean value to indicate whether to allow 404 status code to be ignored
        """

        if response.status_code == 400:
            raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response.json())

        if response.status_code == 401:
            if self.oauth_token:
                self.logger.info(f"Received HTTP {response.status_code}, re-authenticating to Zoom...")
                self._refresh_oauth_token()
                return self._call_api(**original_call_args)
            else:
                raise PluginException(
                    cause="The JWT token provided in the plugin connection configuration is either "
                    "invalid or expired.",
                    assistance="Please update the plugin connection configuration with a valid or "
                    "updated JWT token.",
                )

        if response.status_code == 404:
            if allow_404:
                return None
            else:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.json())

        if response.status_code == 409:
            raise PluginException(
                cause="User already exists.", assistance="Please check your input and try again.", data=response.json()
            )

        if response.status_code == 429:
            exception = self._handle_rate_limit_error(response=response)
            raise exception

        # Success; no content
        if response.status_code == 204:
            return None

        if 200 <= response.status_code < 300:
            return response.json()

    @staticmethod
    def _handle_rate_limit_error(response: Response) -> PluginException:
        rate_limit_type = response.headers.get("X-RateLimit-Type", "")
        rate_limit_limit = response.headers.get("X-RateLimit-Limit")
        rate_limit_remaining = response.headers.get("X-RateLimit-Remaining")
        rate_limit_retry_after = response.headers.get("Retry-After")

        if rate_limit_type == "Light":
            return PluginException(
                cause="Account is rate-limited by the maximum per-second limit for this API.",
                assistance="Try again later.",
            )
        elif rate_limit_type == "Heavy":
            return PluginException(
                cause=f"Account is rate-limited by the maximum daily limit for this API "
                f"(limit: {rate_limit_limit} calls per day, {rate_limit_remaining} remaining.)",
                assistance=f"Try again after {rate_limit_retry_after}.",
            )
        else:
            return PluginException(cause="Account is rate-limited by an unknown quota.", assistance="Try again later.")
