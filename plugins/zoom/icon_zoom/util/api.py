import json
import datetime
import time
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

    def __call__(self, r):
        r.headers["Authorization"] = f"Bearer {self.access_token}"
        return r


class ZoomAPI:
    def __init__(self, account_id: str, client_id: str, client_secret: str, logger: Logger):
        self.api_url = "https://api.zoom.us/v2"
        self.oauth_url = "https://zoom.us/oauth/token"
        self.account_id = account_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.logger = logger

        self.oauth_token: Optional[str] = None
        self.oauth_last_refresh_timestamp: Optional[float] = None

    def refresh_oauth_token_if_needed(self) -> None:
        """
        Refreshes OAuth token if needed.
        :return: None
        """
        if self.oauth_last_refresh_timestamp and not self._should_refresh_oauth_token(
            last_refresh_timestamp=self.oauth_last_refresh_timestamp
        ):
            return

        # Refresh should happen, so do the refresh.
        try:
            self.logger.info("Making call to get new OAuth token")
            oauth_token = self.get_oauth_token()
            now_timestamp = self._get_current_time_epoch()
        except Exception as error:
            raise PluginException(
                cause=f"Unable to refresh OAuth token: {error}.",
                assistance="Ensure connection credentials are correct.",
                data=error,
            )

        self.oauth_token = oauth_token
        self.oauth_last_refresh_timestamp = now_timestamp

    def get_oauth_token(self) -> str:
        """
        Retrieves a server-to-server OAuth token from Zoom
        :return: OAuth token
        """

        params = {"grant_type": "account_credentials", "account_id": self.account_id}

        auth = HTTPBasicAuth(self.client_id, self.client_secret)

        self.logger.info("Requesting new OAuth token from Zoom...")
        response = self._call_api(method="POST", url=self.oauth_url, params=params, auth=auth)
        try:
            access_token = response["access_token"]
        except KeyError:
            raise PluginException(
                cause=f"Unable to get access token: {response.get('reason', '')}.",
                assistance="Ensure your connection configuration is using correct credentials.",
            )

        self.logger.info("Request for new OAuth token was successful!")
        return access_token

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

    def _call_api(
        self,
        method: str,
        url: str,
        params: dict = None,
        json_data: dict = None,
        allow_404: bool = False,
        auth: AuthBase = None,
    ) -> Optional[dict]:  # noqa: MC0001

        if not isinstance(auth, HTTPBasicAuth):
            self.refresh_oauth_token_if_needed()

        # If HTTPBasicAuth isn't provided (for calls to get OAuth token), then
        # use BearerAuth since we have a token already
        if not auth:
            auth = BearerAuth(access_token=self.oauth_token)

        try:
            self.logger.info(f"Calling {method} {url}")
            response = requests.request(method, url, json=json_data, params=params, auth=auth)
            self.logger.info(f"Got response status code: {response.status_code}")

            if response.status_code in [401, 404, 204] or (200 <= response.status_code < 300):
                return self._handle_response(response=response, allow_404=allow_404)

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            self.logger.info(f"Invalid json: {e}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)
        except requests.exceptions.HTTPError as e:
            self.logger.info(f"Request to f{url} failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN)

    def _handle_response(self, response: Response, allow_404: bool):
        if response.status_code == 401:
            resp = json.loads(response.text)
            raise PluginException(
                cause=resp.get("message"),
                assistance="Verify that the credentials configured within the Zoom plugin connection are correct.",
            )
        if response.status_code == 404:
            resp = json.loads(response.text)
            if allow_404:
                return None
            else:
                raise PluginException(
                    cause=resp.get("message"),
                    assistance=f"The object at {response.url} does not exist. Verify the ID and fields " f"used are valid.",
                )
        # Success; no content
        if response.status_code == 204:
            return None
        if 200 <= response.status_code < 300:
            return response.json()

    @staticmethod
    def _get_current_time_epoch() -> float:
        """
        Gets the current epoch time
        :return: Current time in unix epoch
        """
        now = datetime.datetime.now()
        now_millis = time.mktime(now.timetuple())

        return now_millis

    def _should_refresh_oauth_token(self, last_refresh_timestamp: float) -> bool:
        """
        Determines whether or not the OAuth token should be refreshed.
        Calculated differences >=55 minutes will return True.
        :param last_refresh_timestamp: Unix epoch timestamp representing last time the OAuth token was refreshed
        :return: Boolean, True if a token refresh should happen, False otherwise
        """
        # 55 minutes in seconds. Zoom API refresh is 60 minutes, but we'll use 55 minutes for headroom.
        fifty_five_minutes = 3300

        now = ZoomAPI._get_current_time_epoch()
        previous_time = last_refresh_timestamp
        self.logger.info(f"Calculating OAuth token refresh, last refreshed at {previous_time}, current time {now}")

        time_difference = now - previous_time
        should_refresh = time_difference >= fifty_five_minutes

        return should_refresh
