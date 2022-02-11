from logging import Logger
import time
from typing import Callable, Type
import requests

from insightconnect_plugin_runtime.exceptions import PluginException

from .validators import InputDataValidator

RETRY_MESSAGE = "Rate limiting error occurred. Retrying in {delay} seconds ({attemps_counter}/{max_tries})"
GET_REQUEST_ID_RETRY_MESSAGE = (
    "Request is still being processed. Retrying in {delay} seconds ({attemps_counter}/{max_tries})"
)


class ApiClient:
    def __init__(self, api_key: str, logger: Type[Logger] = None) -> None:
        self.api_url = "https://api.opsgenie.com/v2/"
        self.api_key = api_key
        self.logger = logger
        self.validator = InputDataValidator()

    def create_alert(self, data: dict) -> dict:
        CREATE_ALERT_URL = f"{self.api_url}alerts/"
        self.validator.validate(data)
        create_alert_reponse = self._call_api("POST", CREATE_ALERT_URL, json_data=data)
        request_alert_id = self._retry_request(create_alert_reponse.get("requestId"), 10)
        return {**create_alert_reponse, "alertId": request_alert_id}

    def get_alert(self, identifier: str, id_type: str = "ID") -> dict:
        GET_ALERT_URL = f"{self.api_url}alerts/{identifier}"
        params = {"identifierType": id_type}
        return self._call_api("GET", GET_ALERT_URL, params=params)

    def close_alert(self, identifier: str, id_type: str = "ID", data: dict = None) -> dict:
        CLOSE_ALERT_URL = f"{self.api_url}alerts/{identifier}/close"
        params = {"identifierType": id_type}
        if data:
            self.validator.validate(data)
        return self._call_api("POST", CLOSE_ALERT_URL, params=params, json_data=data)

    def get_on_calls(self, identifier: str, id_type: str = "ID", flat: bool = False, date: str = None) -> dict:
        GET_ON_CALLS_URL = f"{self.api_url}schedules/{identifier}/on-calls"
        params = {"scheduleIdentifierType": id_type, "flat": flat}
        if date:
            params["date"] = date
        return self._call_api("GET", GET_ON_CALLS_URL, params=params)

    def test_api(self) -> dict:
        GET_TEST_URL = f"{self.api_url}alerts/count"
        return self._call_api("GET", GET_TEST_URL)

    def _rate_limiting(max_tries: int) -> dict:
        def _decorate(func: Callable):
            def _wrapper(self, *args, **kwargs):
                retry = True
                attemps_counter, delay = 0, 0
                while retry and attemps_counter < max_tries:
                    if attemps_counter:
                        time.sleep(delay)
                    try:
                        retry = False
                        return func(self, *args, **kwargs)
                    except PluginException as e:
                        attemps_counter += 1
                        delay = 1 * attemps_counter
                        if e.cause == PluginException.causes[PluginException.Preset.RATE_LIMIT]:
                            self.logger.info(
                                RETRY_MESSAGE.format(delay=delay, attemps_counter=attemps_counter, max_tries=max_tries)
                            )
                            retry = True
                return func(self, *args, **kwargs)

            return _wrapper

        return _decorate

    @_rate_limiting(max_tries=10)
    def _call_api(self, method: str, url: str, json_data: dict = None, params: dict = None) -> dict:
        headers = {"Authorization": f"GenieKey {self.api_key}"}
        try:
            response = requests.request(method, url, json=json_data, params=params, headers=headers)

            if response.status_code in (401, 403):
                raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)
            if response.status_code == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND)
            if response.status_code == 429:
                raise PluginException(preset=PluginException.Preset.RATE_LIMIT)
            if 200 <= response.status_code < 300:
                return response.json()

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)

        except requests.exceptions.HTTPError as e:
            self.logger.info(f"Call to OpsGenie API failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)

    def _retry_request(self, request_id: str, max_tries: int) -> str:
        request_response = self._get_request_status(request_id)
        attemps_counter, delay = 0, 0
        while not request_response.get("data").get("isSuccess") and attemps_counter < max_tries:
            time.sleep(delay)
            request_response = self._get_request_status(request_id)
            attemps_counter += 1
            delay = 1 * attemps_counter
            self.logger.info(
                GET_REQUEST_ID_RETRY_MESSAGE.format(delay=delay, attemps_counter=attemps_counter, max_tries=max_tries)
            )
        alert_id = request_response.get("data").get("alertId")
        if alert_id:
            return alert_id
        raise PluginException(preset=PluginException.Preset.NOT_FOUND)

    def _get_request_status(self, identifier: str) -> dict:
        GET_REQUEST_STATUS_URL = f"{self.api_url}alerts/requests/{identifier}"
        return self._call_api("GET", GET_REQUEST_STATUS_URL)
