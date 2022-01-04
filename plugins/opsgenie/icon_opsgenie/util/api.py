import json
import requests

from insightconnect_plugin_runtime.exceptions import PluginException


class ApiClient:
    def __init__(self, api_key: str, logger=None) -> None:
        self.api_url = "https://api.opsgenie.com/v2/"
        self.api_key = api_key
        self.logger = logger

    def create_alert(self, data: dict) -> dict:
        CREATE_ALERT_URL = f"{self.api_url}alerts/"
        return self._call_api("POST", CREATE_ALERT_URL, data=data)

    def get_alert(self, id: str, id_type: str = "ID") -> dict:
        GET_ALERT_URL = f"{self.api_url}alerts/{id}"
        params = {"identifierType": id_type}
        return self._call_api("GET", GET_ALERT_URL, params=params)

    def close_alert(self, id: str, id_type: str = "ID", data: dict = None) -> dict:
        CLOSE_ALERT_URL = f"{self.api_url}alerts/{id}/close"
        params = {"identifierType": id_type}
        return self._call_api("POST", CLOSE_ALERT_URL, params=params, data=data)

    def get_on_calls(self, id: str, id_type: str = "ID", flat: bool = False, date: str = None) -> dict:
        GET_ON_CALLS_URL = f"{self.api_url}schedules/{id}/on-calls"
        params = {"scheduleIdentifierType": id_type, "flat": flat}

        if date:
            params["date"] = date

        return self._call_api("GET", GET_ON_CALLS_URL, params=params)

    def test_api(self) -> dict:
        GET_TEAM_URL = f"{self.api_url}teams"
        return self._call_api("GET", GET_TEAM_URL)

    def _call_api(self, method: str, url: str, json_data: dict = None, params: dict = None, data: dict = None) -> dict:
        headers = {"Authorization": f"GenieKey {self.api_key}"}
        try:
            if data is None:
                data_string = None
            else:
                data_string = json.dumps(data)

            response = requests.request(method, url, json=json_data, params=params, data=data_string, headers=headers)

            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)
            if response.status_code == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND)
            if 200 <= response.status_code < 300:
                return response.json()

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)

        except json.decoder.JSONDecodeError as e:
            self.logger.info(f"Invalid JSON entered: {e}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)

        except requests.exceptions.HTTPError as e:
            self.logger.info(f"Call to OpsGenie API failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
