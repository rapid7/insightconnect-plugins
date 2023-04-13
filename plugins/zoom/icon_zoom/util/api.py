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
        oauth_retry_limit: Optional[int] = 5,  # For OAuth only
        jwt_token: Optional[str] = None  # For JWT auth only
    ):
        self.api_url = "https://api.zoom.us/v2"
        self.oauth_url = "https://zoom.us/oauth/token"
        self.account_id = account_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.oauth_retry_limit = oauth_retry_limit
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

    def _refresh_oauth_token(self) -> None:
        """
        Retrieves a new server-to-server OAuth token from Zoom
        :return: None
        """
        params = {"grant_type": "account_credentials", "account_id": self.account_id}
        auth = HTTPBasicAuth(self.client_id, self.client_secret)

        try:
            self.logger.info("Calling Zoom API to refresh OAuth token...")
            response = requests.post("https://zoom.us/oauth/token", params=params, auth=auth, timeout=120)

            self.logger.info(f"Got status code {response.status_code} from OAuth token refresh")
            self._handle_oauth_status_codes(response=response)
            response_data = response.json()

        except requests.exceptions.HTTPError as error:
            self.logger.info(f"Request to get OAuth token failed: {error}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN)

        except requests.exceptions.Timeout as error:
            self.logger.info(f"Request to get OAuth token timed out: {error}")
            raise PluginException(preset=PluginException.Preset.TIMEOUT)

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

    def _handle_oauth_status_codes(self, response: Response) -> None:
        # Handle known status codes
        codes = {
            400: PluginException(preset=PluginException.Preset.BAD_REQUEST),
            401: PluginException(preset=PluginException.Preset.UNAUTHORIZED),
            403: PluginException(
                cause="Configured credentials do not have permission for this API endpoint.",
                assistance="Please ensure credentials have required permissions.",
            ),
            429: self.get_exception_for_rate_limit(response),
            4700: PluginException(
                cause="Configured credentials do not have permission for this API endpoint.",
                assistance="Please ensure credentials have required permissions.",
            ),
        }

        for key, value in codes.items():
            if response.status_code == key:
                raise value

        # Handle unknown status codes
        if response.status_code in range(0, 199) or response.status_code >= 300:
            raise PluginException(preset=PluginException.Preset.UNKNOWN)

    def _call_api(
        self,
        method: str,
        url: str,
        params: dict = None,
        json_data: dict = None,
        allow_404: bool = False,
        retry_401_count: int = 0,
    ) -> Optional[dict]:  # noqa: MC0001
        # Determine which type of authentication mechanism to use
        if self.oauth_token or self._is_using_oauth():
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
                    retry_401_count=retry_401_count
                )

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as error:
            self.logger.info(f"Invalid JSON: {error}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)
        except requests.exceptions.HTTPError as error:
            self.logger.info(f"Request to {url} failed: {error}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN)

    def _handle_response(self, response: Response, allow_404: bool, original_call_args: dict, retry_401_count: int):
        """
        Helper function to process the response based on the status code returned.
        :param response: Response object
        :param allow_404: Boolean value to indicate whether to allow 404 status code to be ignored
        """

        exceptions_4xx = {
            400: PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response.json()),
            404: PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.json()),
            409: PluginException(cause="User already exists.", assistance="Please check your input and try again.", data=response.json()),
            429: self.get_exception_for_rate_limit(response=response)
        }

        # Success; no content
        if response.status_code == 204:
            return None

        if 200 <= response.status_code < 300:
            return response.json()

        for status_code, exception in exceptions_4xx.items():
            if response.status_code == status_code:
                if status_code == 404 and allow_404:
                    return None
                raise exception

        # 401 requires extra logic, so it is not included in the 4xx dict
        if response.status_code == 401:
            if self.oauth_token or self._is_using_oauth():
                if retry_401_count == (self.oauth_retry_limit - 1):  # -1 to account for retries starting at 0
                    raise PluginException(cause="OAuth authentication retry limit was met.",
                                          assistance="Ensure your OAuth connection credentials are valid. "
                                                     "If running a large number of integrations with Zoom, consider "
                                                     "increasing the OAuth authentication retry limit to accommodate.")
                self.logger.info(f"Received HTTP {response.status_code}, re-authenticating to Zoom...")
                retry_401_count += 1
                self._refresh_oauth_token()
                return self._call_api(**original_call_args, retry_401_count=retry_401_count)

            raise PluginException(
                cause="The JWT token provided in the plugin connection configuration is either " "invalid or expired.",
                assistance="Please update the plugin connection configuration with a valid or " "updated JWT token.",
            )

    @staticmethod
    def get_exception_for_rate_limit(response: Response) -> PluginException:
        rate_limit_type = response.headers.get("X-RateLimit-Type", "")
        rate_limit_limit = response.headers.get("X-RateLimit-Limit")
        rate_limit_remaining = response.headers.get("X-RateLimit-Remaining")
        rate_limit_retry_after = response.headers.get("Retry-After")

        if rate_limit_type == "Light":
            return PluginException(
                cause="Account is rate-limited by the maximum per-second limit for this API.",
                assistance="Try again later.",
            )

        if rate_limit_type == "Heavy":
            return PluginException(
                cause=f"Account is rate-limited by the maximum daily limit for this API "
                f"(limit: {rate_limit_limit} calls per day, {rate_limit_remaining} remaining.)",
                assistance=f"Try again after {rate_limit_retry_after}.",
            )

        return PluginException(cause="Account is rate-limited by an unknown quota.", assistance="Try again later.")

    def _is_using_oauth(self) -> bool:
        if (self.account_id and self.client_id and self.client_secret) or self.oauth_token:
            return True
        else:
            return False
