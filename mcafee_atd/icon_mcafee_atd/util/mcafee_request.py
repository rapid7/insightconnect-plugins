import requests
from insightconnect_plugin_runtime.exceptions import PluginException
import json


class McAfeeRequest:
    def __init__(self, url: str, port: int, verify_ssl: bool, logger: object):
        self.url = f"{url}:{str(port)}/php"
        self.verify_ssl = verify_ssl
        self.logger = logger

    def make_json_request(self, method, path, params=None, data=None, headers=None, files=None):
        response = {"text": ""}

        try:
            response = requests.request(
                method,
                f"{self.url}/{path}",
                data=data,
                params=params,
                files=files,
                headers=headers,
                verify=self.verify_ssl
            )

            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.API_KEY)
            if response.status_code >= 400:
                response_data = response.json()
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response_data.get("message"))
            if 200 <= response.status_code < 300:
                return response.json()

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            self.logger.info(f"Invalid JSON: {e}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
        except requests.exceptions.HTTPError as e:
            self.logger.info(f"Call to McAfee ATD API failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
