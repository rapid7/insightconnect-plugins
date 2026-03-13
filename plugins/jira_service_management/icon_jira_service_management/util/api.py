import base64

import requests

from icon_jira_service_management.util.constants import REQUESTS_TIMEOUT
from icon_jira_service_management.util.retry import rate_limiting
from insightconnect_plugin_runtime.helper import make_request

MAX_REQUEST_TRIES = 10


class JiraServiceManagementApi:

    def __init__(self, api_token: str, cloud_id: str, email: str) -> None:
        self.api_token = api_token
        self.cloud_id = cloud_id
        self.email = email

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

        create_alert_response = self._call_api(
            method="POST",
            url=url,
            json_data=data,
        )
        alert_id = self._get_request_status(identifier=create_alert_response.get("requestId")).get("alertId")

        return {**create_alert_response, "alertId": alert_id}

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
