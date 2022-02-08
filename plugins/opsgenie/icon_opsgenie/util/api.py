import requests

from insightconnect_plugin_runtime.exceptions import PluginException

from .validators import InputDataValidator


class ApiClient:
    def __init__(self, api_key: str, logger=None) -> None:
        self.api_url = "https://api.opsgenie.com/v2/"
        self.api_key = api_key
        self.logger = logger
        self.validator = InputDataValidator()

    def create_alert(self, data: dict) -> dict:
        CREATE_ALERT_URL = f"{self.api_url}alerts/"
        self.validator.validate(data)
        return self._call_api("POST", CREATE_ALERT_URL, json_data=data)

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

    def _call_api(self, method: str, url: str, json_data: dict = None, params: dict = None) -> dict:
        headers = {"Authorization": f"GenieKey {self.api_key}"}
        try:
            response = requests.request(method, url, json=json_data, params=params, headers=headers)

            if response.status_code in (401, 403):
                raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)
            if response.status_code == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND)
            if 200 <= response.status_code < 300:
                return response.json()

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)

        except requests.exceptions.HTTPError as e:
            self.logger.info(f"Call to OpsGenie API failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
