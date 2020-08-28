import requests
from insightconnect_plugin_runtime.exceptions import PluginException
import json


class PaloAltoMineMeldAPI:
    def __init__(self, url: str, username: str, password: str, ssl_verify: bool, logger: object):
        self.url = url
        self.username = username
        self.password = password
        self.ssl_verify = ssl_verify
        self.logger = logger

    def update_external_dynamic_list(self, list_name, updated_indicators_list):
        return self._call_api("PUT", f"{self.url}/config/data/{list_name}_indicators",
                              json_data=updated_indicators_list)

    def get_indicators(self, list_name):
        return self._call_api("GET", f"{self.url}/config/data/{list_name}_indicators")

    def health_check(self):
        return self._call_api("GET", f"{self.url}/config/full", full_response=True).status_code == 200

    def _call_api(self, method, url, params=None, json_data=None, full_response: bool = False):
        response = {"text": ""}
        try:
            response = requests.request(
                method,
                url,
                json=json_data,
                params=params,
                auth=(self.username, self.password),
                verify=self.ssl_verify
            )

            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.API_KEY)
            if response.status_code >= 400:
                response_data = response.json()
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response_data.message)

            if 200 <= response.status_code < 300:
                if full_response:
                    return response

                return response.json()

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            self.logger.info(f"Invalid json: {e}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
        except requests.exceptions.HTTPError as e:
            self.logger.info(f"Call to Palo Alto MineMeld failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
