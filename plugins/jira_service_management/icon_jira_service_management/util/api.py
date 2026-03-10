import base64
import time
from functools import wraps
from logging import Logger
from typing import Callable

import requests

from icon_jira_service_management.util.constants import REQUESTS_TIMEOUT
from icon_jira_service_management.util.validators import InputDataValidator
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import make_request


RETRY_MESSAGE = "Rate limiting error occurred. Retrying in {delay:.1f} seconds ({attempts_counter}/{max_tries})"
GET_REQUEST_ID_RETRY_MESSAGE = (
    "Request is still being processed. Retrying in {delay:.1f} seconds ({attempts_counter}/{max_tries})"
)
MAX_REQUEST_TRIES = 10


class JiraServiceManagementApi:

    def __init__(self, api_token: str, cloud_id: str, email: str, logger: Logger) -> None:
        self.api_token = api_token
        self.cloud_id = cloud_id
        self.email = email
        self.logger = logger
        self.validator = InputDataValidator()

    def encode_basic_auth(self):
        credentials = f"{self.email}:{self.api_token}"
        return base64.b64encode(credentials.encode()).decode()

    @staticmethod
    def _rate_limiting(max_tries: int = 5):
        def decorator(func: Callable):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                attempts, delay = 0, 0
                while attempts < max_tries:
                    if attempts > 0:
                        time.sleep(delay)
                    try:
                        return func(self, *args, **kwargs)
                    except PluginException as e:
                        attempts += 1
                        delay = 2 ** (attempts * 0.6)
                        if e.cause == PluginException.causes[PluginException.Preset.RATE_LIMIT]:
                            self.logger.info(
                                RETRY_MESSAGE.format(delay=delay, attempts_counter=attempts, max_tries=max_tries)
                            )
                            continue
                        raise
                return func(self, *args, **kwargs)

            return wrapper

        return decorator

    def create_alert(self, data: dict) -> dict:
        url = f"https://api.atlassian.com/jsm/ops/api/{self.cloud_id}/v1/alerts"
        self.validator.validate(data)
        token = self.encode_basic_auth()

        create_alert_response = self._call_api(
            method="POST",
            url=url,
            token=token,
            json_data=data,
        )
        request_alert_id = self._retry_request(
            token=token,
            request_id=create_alert_response.get("requestId"),
            max_tries=MAX_REQUEST_TRIES,
        )

        return {**create_alert_response, "alertId": request_alert_id}

    @_rate_limiting(max_tries=MAX_REQUEST_TRIES)
    def _call_api(self, method: str, url: str, token: str, json_data: dict = None, params: dict = None) -> dict:
        return make_request(
            _request=requests.Request(
                method=method,
                url=url,
                json=json_data,
                headers={
                    "Accept": "application/json",
                    "Authorization": f"Basic {token}",
                },
                params=params,
            ),
            timeout=REQUESTS_TIMEOUT,
        ).json()

    def _retry_request(self, token: str, request_id: str, max_tries: int) -> str:
        request_response = {}
        attempts_counter, delay = -1, 0
        while not request_response.get("alertId", "") and attempts_counter < max_tries:
            time.sleep(delay)
            try:
                request_response = self._get_request_status(
                    token=token,
                    identifier=request_id,
                )
            except PluginException:
                attempts_counter += 1
                delay = 2 ** (attempts_counter * 0.6)
                self.logger.info(
                    GET_REQUEST_ID_RETRY_MESSAGE.format(
                        delay=delay, attempts_counter=attempts_counter, max_tries=max_tries
                    )
                )
        alert_id = request_response.get("alertId")
        if alert_id:
            return alert_id
        raise PluginException(preset=PluginException.Preset.NOT_FOUND)

    def _get_request_status(self, token: str, identifier: str) -> dict:
        url = f"https://api.atlassian.com/jsm/ops/api/{self.cloud_id}/v1/alerts/requests/{identifier}"

        return make_request(
            _request=requests.Request(
                method="GET",
                url=url,
                headers={
                    "Accept": "application/json",
                    "Authorization": f"Basic {token}",
                },
            ),
            timeout=REQUESTS_TIMEOUT,
        ).json()

    def test_api(self) -> dict:
        return make_request(
            _request=requests.Request(
                method="GET",
                url=f"https://api.atlassian.com/jsm/ops/api/{self.cloud_id}/v1/alerts",
                headers={
                    "Accept": "application/json",
                    "Authorization": f"Basic {self.encode_basic_auth()}",
                },
            ),
            timeout=REQUESTS_TIMEOUT,
        ).status_code
