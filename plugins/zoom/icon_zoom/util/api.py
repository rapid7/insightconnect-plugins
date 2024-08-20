from logging import Logger
from typing import Optional

import requests
from requests.auth import HTTPBasicAuth
from requests.auth import AuthBase
from requests import Response

from insightconnect_plugin_runtime.exceptions import PluginException, HTTPStatusCodes, ResponseExceptionData
from insightconnect_plugin_runtime.helper import make_request, extract_json


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
        Info: This endpoint accepts to and from params that don't consider hours, minutes, and seconds
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
            request = requests.Request(
                method="POST",
                url="https://zoom.us/oauth/token",
                params=params,
                auth=auth,
            )
            custom_config = {
                HTTPStatusCodes.BAD_REQUEST: AuthenticationError(),
                HTTPStatusCodes.UNAUTHORIZED: AuthenticationError(),
                HTTPStatusCodes.FORBIDDEN: PluginException(
                    cause="Configured credentials do not have permission for this API endpoint.",
                    assistance="Please ensure credentials have required permissions.",
                ),
                4700: PluginException(
                    cause="Configured credentials do not have permission for this API endpoint.",
                    assistance="Please ensure credentials have required permissions.",
                ),
            }
            response = make_request(
                _request=request,
                exception_custom_configs=custom_config,
                timeout=120,
                allowed_status_codes=[HTTPStatusCodes.TOO_MANY_REQUESTS],
            )

            self.logger.info(f"Got status code {response.status_code} from OAuth token refresh")
            if response.status_code == HTTPStatusCodes.TOO_MANY_REQUESTS:
                raise self.get_exception_for_rate_limit(response)
            response_data = extract_json(response)

        except PluginException as error:
            self.logger.info(f"Request to get OAuth token failed {error}")
            raise error

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
        retry_401_count: int = 0,
    ) -> Optional[dict]:  # noqa: MC0001
        auth = BearerAuth(access_token=self.oauth_token)
        request = requests.Request(method=method, url=url, json=json_data, params=params, auth=auth)
        allowed_codes = [HTTPStatusCodes.UNAUTHORIZED, HTTPStatusCodes.TOO_MANY_REQUESTS]
        if allow_404:
            allowed_codes.append(HTTPStatusCodes.NOT_FOUND)
        custom_config = {
            HTTPStatusCodes.CONFLICT: PluginException(
                cause="User already exists.", assistance="Please check your input and try again."
            )
        }
        # try:
        self.logger.info(f"Calling {method} {url}")
        response = make_request(
            _request=request,
            exception_custom_configs=custom_config,
            exception_data_location=ResponseExceptionData.RESPONSE_TEXT,
            allowed_status_codes=allowed_codes,
        )
        self.logger.info(f"Got response status code: {response.status_code}")

        return self._handle_response(
            response=response,
            original_call_args={
                "method": method,
                "url": url,
                "params": params,
                "json_data": json_data,
                "allow_404": allow_404,
            },
            retry_401_count=retry_401_count,
        )

    def _handle_response(self, response: Response, original_call_args: dict, retry_401_count: int):
        """
        Helper function to process the response based on the status code returned.
        :param response: Response object
        """

        if response.status_code == 401:
            if retry_401_count == (self.oauth_retry_limit - 1):  # -1 to account for retries starting at 0
                raise AuthenticationRetryLimitError
            self.logger.info(f"Received HTTP {response.status_code}, re-authenticating to Zoom...")
            retry_401_count += 1
            self._refresh_oauth_token()
            return self._call_api(**original_call_args, retry_401_count=retry_401_count)

        if response.status_code == 429:
            raise self.get_exception_for_rate_limit(response=response)

        # Success or allow 404; no content
        if response.status_code in [204, 404]:
            return None

        return extract_json(response)

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
