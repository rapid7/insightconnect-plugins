import base64
from logging import Logger

import requests

from icon_jira_service_management.util.constants import REQUESTS_TIMEOUT
from icon_jira_service_management.util.retry import rate_limiting
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import make_request

MAX_REQUEST_TRIES = 10


class JiraServiceManagementApi:

    def __init__(self, api_token: str, cloud_id: str, email: str, logger: Logger) -> None:
        self.api_token = api_token
        self.cloud_id = cloud_id
        self.email = email
        self.logger = logger

    def encode_basic_auth(self):
        credentials = f"{self.email}:{self.api_token}"
        return base64.b64encode(credentials.encode()).decode()

    def get_headers(self):
        return {
            "Accept": "application/json",
            "Authorization": f"Basic {self.encode_basic_auth()}",
        }

    def create_alert(self, data: dict) -> dict:
        url = f"https://api.atlassian.com/jsm/ops/api/{self.cloud_id}/v1/alerts"

        try:
            self.logger.info("Creating alert in Jira Service Management Ops API.")

            create_alert_response = self._call_api(
                method="POST",
                url=url,
                json_data=data,
            )

            request_id = create_alert_response.get("requestId")
            self.logger.info(f"Alert creation request sent. Request ID: {request_id}")

            alert_id = self._get_request_status(identifier=create_alert_response.get("requestId")).get("alertId")
            self.logger.info(f"Alert created successfully. Alert ID: {alert_id}")

            return {**create_alert_response, "alertId": alert_id}
        except PluginException as error:
            self.logger.error(f"Failed to create alert: {error}")
            raise

    def close_alert(self, identifier: str) -> dict:
        url = f"https://api.atlassian.com/jsm/ops/api/{self.cloud_id}/v1/alerts/{identifier}/close"

        try:
            self.logger.info(f"Closing alert with identifier: {identifier}")

            close_alert_response = self._call_api(
                method="POST",
                url=url,
            )
            self.logger.info(f"Alert close request sent. Request ID: {close_alert_response.get('requestId')}")

            return close_alert_response
        except PluginException as error:
            self.logger.error(f"Failed to close alert: {error}")
            raise

    def get_alert(self, identifier: str) -> dict:
        url = f"https://api.atlassian.com/jsm/ops/api/{self.cloud_id}/v1/alerts/{identifier}"

        try:
            self.logger.info(f"Retrieving alert with identifier: {identifier}")

            get_alert_response = self._call_api(
                method="GET",
                url=url,
            )

            return get_alert_response
        except PluginException as error:
            self.logger.error(f"Failed to retrieve alert: {error}")
            raise

    def get_on_calls(self, schedule_id: str, flat: bool = False, date: str = None) -> dict:
        url = f"https://api.atlassian.com/jsm/ops/api/{self.cloud_id}/v1/schedules/{schedule_id}/on-calls"
        params = {}
        try:
            self.logger.info(f"Retrieving on-calls for schedule with ID: {schedule_id}")
            if flat:
                params["flat"] = flat
            if date:
                params["date"] = date

            get_on_calls_response = self._call_api(
                method="GET",
                url=url,
                params=params,
            )

            return get_on_calls_response
        except PluginException as error:
            self.logger.error(f"Failed to retrieve on-calls: {error}")
            raise

    @rate_limiting(max_tries=MAX_REQUEST_TRIES)
    def _call_api(self, method: str, url: str, json_data: dict = None, params: dict = None) -> dict:
        return make_request(
            _request=requests.Request(
                method=method,
                url=url,
                json=json_data,
                headers=self.get_headers(),
                params=params,
            ),
            timeout=REQUESTS_TIMEOUT,
        ).json()

    def _get_request_status(self, identifier: str) -> dict:
        url = f"https://api.atlassian.com/jsm/ops/api/{self.cloud_id}/v1/alerts/requests/{identifier}"

        return make_request(
            _request=requests.Request(
                method="GET",
                url=url,
                headers=self.get_headers(),
            ),
            timeout=REQUESTS_TIMEOUT,
        ).json()

    def test_api(self) -> dict:
        return make_request(
            _request=requests.Request(
                method="GET",
                url=f"https://api.atlassian.com/jsm/ops/api/{self.cloud_id}/v1/alerts",
                headers=self.get_headers(),
            ),
            timeout=REQUESTS_TIMEOUT,
        )
