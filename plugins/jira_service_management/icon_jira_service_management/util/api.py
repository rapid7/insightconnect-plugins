import base64
import time
from logging import Logger

import requests

from icon_jira_service_management.util.constants import REQUESTS_TIMEOUT
from icon_jira_service_management.util.retry import rate_limiting
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import make_request, clean

MAX_REQUEST_TRIES = 10
MAX_STATUS_TRIES = 8


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

            alert_id = self._get_alert_id(request_id)
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
        try:
            self.logger.info(f"Retrieving on-calls for schedule with ID: {schedule_id}")
            params = clean({"flat": flat if flat else None, "date": date})

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

    def _get_alert_id(self, request_id: str) -> str:
        # JSM processes alert requests asynchronously and answers 404 until it is done.
        # Timeouts, rate limiting, server errors and network errors are retried too. 4xx codes the SDK labels
        # with a status code (400, 401, 403, ...) fail at once; unlabelled ones (e.g. 422) are retried.
        last_error = None
        for delay in range(MAX_STATUS_TRIES):
            time.sleep(delay)
            try:
                request_status = self._get_request_status(identifier=request_id)
            except PluginException as error:
                last_error = error
                status_code = getattr(error, "status_code", None)
                if status_code and status_code < 500 and status_code not in (404, 408, 429):
                    raise
                self.logger.info(
                    f"Alert request not available yet, status code {status_code} ({delay + 1}/{MAX_STATUS_TRIES})"
                )
                continue

            if request_status.get("isSuccess") is False:
                raise PluginException(
                    cause="Jira Service Management failed to process the alert request.",
                    assistance=f"Request ID: {request_id}.",
                    data=request_status.get("status"),
                )
            return request_status.get("alertId")

        raise PluginException(
            cause=f"Jira Service Management accepted alert request {request_id} but has not processed it yet.",
            assistance="Check the alerts list in Jira Service Management before running the step again.",
            data=f"Last error: {last_error}",
        )

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
