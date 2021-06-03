from insightconnect_plugin_runtime.helper import clean
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
from logging import Logger
import requests
import json


class PagerDutyAPI:
    def __init__(self, api_key: str, logger: Logger):
        self.headers = {"Authorization": f"Token token={api_key}", "Content-Type": "application/json"}
        self.session = requests.session()
        self.logger = logger

    def get_on_calls(self, schedule_id: str = None) -> dict:
        params = {"limit": 100}
        if schedule_id:
            params = {"schedule_ids[]": schedule_id}
        return self.send_request("GET", "/oncalls", params)

    def send_request(self, method: str, path: str, params: dict = None, payload: dict = None) -> dict:
        try:
            response = self.session.request(
                method.upper(),
                "https://api.pagerduty.com" + path,
                params=params,
                json=payload,
                headers=self.headers,
            )

            if response.status_code == 401:
                raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD, data=response.text)
            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
            if response.status_code == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.text)
            if 400 <= response.status_code < 500:
                raise PluginException(
                    preset=PluginException.Preset.UNKNOWN,
                    data=response.text,
                )
            if response.status_code >= 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)

            if 200 <= response.status_code < 300:
                return clean(json.loads(response.content))

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=e)
        except requests.exceptions.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)
