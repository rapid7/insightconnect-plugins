import requests
from insightconnect_plugin_runtime.exceptions import PluginException
import json


class AnyRunAPI:
    def __init__(self, authentication_header, logger):
        self.url = 'https://api.any.run/v1/analysis/'
        self.authentication_header = authentication_header
        self.logger = logger

    def get_history(self, team, skip, limit):
        return self._call_api("GET", self.url, params={"team": team, "skip": skip, "limit": limit})

    def get_report(self, task_id):
        return self._call_api("GET", self.url + task_id)

    def run_analysis(self, json_data, files):
        return self._call_api("POST", self.url, files=files, json_data=json_data)

    def _call_api(self, method, url, params=None, json_data=None, files=None):
        response = {"text": ""}
        self.logger.info(f"Authorization header: {self.authentication_header}")
        try:
            response = requests.request(method, url,
                                        files=files,
                                        json=json_data,
                                        params=params,
                                        headers=self.authentication_header)

            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.API_KEY)
            if response.status_code >= 400:
                response_data = response.json()
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response_data.message)
            if 200 <= response.status_code < 300:
                return response.json()

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            self.logger.info(f"Invalid json: {e}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
        except requests.exceptions.HTTPError as e:
            self.logger.info(f"Call to Any Run failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
