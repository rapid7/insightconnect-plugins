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


class AuthenticationError(Exception):
    pass


class AuthenticationRetryLimitError(Exception):
    pass


class ZoomAPI:
    def __init__(
        self,
        logger: Logger,
        account_id: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        oauth_retry_limit: Optional[int] = 5,
    ):
        self.api_url = "https://api.zoom.us/v2"
        self.oauth_url = "https://zoom.us/oauth/token"
        self.account_id = account_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.oauth_retry_limit = oauth_retry_limit
        self.logger = logger

        self.oauth_token: Optional[str] = None

    def authenticate(self):
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

    def get_user_activity_events_task(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        page_size: Optional[int] = None,
        next_page_token: Optional[str] = None,
    ) -> ([dict], Optional[str]):
        """
        Gets user activity events, paginated externally.
        Warning: Changing start date/end date/page size mid-pagination will result in the current next_page_token
        becoming invalidated!
        :param start_date: Optional, time to start from
        :param end_date: Optional, time to end at
        :param page_size: Optional, amount of pages to consume. Zoom API is capped at 300 results
        :param next_page_token: Optional, pagination token to use for retrieving next result set
        :return: Tuple containing list of results (as dictionaries), string containing next page token
        """
        activities_url = f"{self.api_url}/report/activities"

        events = []
        params = {
            "from": start_date,
            "to": end_date,
            "page_size": page_size,
            "next_page_token": next_page_token,
        }
        response = self._call_api("GET", activities_url, params=params)

        events = events + response.get("activity_logs", [])

        # Get next page token and normalize it to None
        new_next_page_token = response.get("next_page_token")
        if new_next_page_token is None or new_next_page_token == "":  # nosec
            new_next_page_token = None

        return events, new_next_page_token

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
            400: AuthenticationError,
            401: AuthenticationError,
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
        auth = BearerAuth(access_token=self.oauth_token)

        try:
            self.logger.info(f"Calling {method} {url}")
            response = requests.request(method, url, json=json_data, params=params, auth=auth)
            self.logger.info(f"Got response status code: {response.status_code}")

            if response.status_code in [400, 401, 404, 409, 429] or (200 <= response.status_code < 300):
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
                    retry_401_count=retry_401_count,
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

        # Success; no content
        if response.status_code == 204:
            return None

        if 200 <= response.status_code < 300:
            return response.json()

        if response.status_code == 400:
            raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response.json())
        if response.status_code == 404:
            if allow_404:
                return None
            raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.json())
        if response.status_code == 409:
            raise PluginException(
                cause="User already exists.", assistance="Please check your input and try again.", data=response.json()
            )
        if response.status_code == 429:
            raise self.get_exception_for_rate_limit(response=response)

        # 401 requires extra logic, so it is not included in the 4xx dict
        if response.status_code == 401:
            if retry_401_count == (self.oauth_retry_limit - 1):  # -1 to account for retries starting at 0
                raise AuthenticationRetryLimitError
            self.logger.info(f"Received HTTP {response.status_code}, re-authenticating to Zoom...")
            retry_401_count += 1
            self._refresh_oauth_token()
            return self._call_api(**original_call_args, retry_401_count=retry_401_count)

        # If we reach this point, all known/documented status codes have been exhausted, so the Zoom API has likely
        # changed and the plugin will require an update.
        raise PluginException(
            cause=f"Received an undocumented status code from the Zoom API ({response.status_code})",
            assistance="Please contact support for assistance.",
        )

    @staticmethod
    def get_exception_for_rate_limit(response: Response) -> PluginException:
        rate_limit_category = response.headers.get("x-ratelimit-category", "")
        rate_limit_limit = response.headers.get("x-ratelimit-limit")
        rate_limit_remaining = response.headers.get("x-ratelimit-remaining")
        rate_limit_retry_after = response.headers.get("Retry-After")

        if rate_limit_category == "Light":
            return PluginException(
                cause="Account is rate-limited by the maximum per-second limit for this API.",
                assistance="Try again later.",
            )

        if rate_limit_category == "Heavy":
            return PluginException(
                cause=f"Account is rate-limited by the maximum daily limit for this API "
                f"(limit: {rate_limit_limit} calls per day, {rate_limit_remaining} remaining.)",
                assistance=f"Try again after {rate_limit_retry_after}.",
            )

        return PluginException(cause="Account is rate-limited by an unknown quota.", assistance="Try again later.")
