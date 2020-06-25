import komand
import json
import requests
from komand.exceptions import PluginException
from requests.exceptions import RequestException


class Api:
    def __init__(self, connection):
        self.connection = connection
        self.logger = connection.logger

    def execute(self, method: str, url: str, payload: dict) -> dict:
        self.connection.create_jwt_token(url, method.upper(), json.dumps(payload))
        request_url = self.connection.url + url

        response = None
        try:
            response = requests.request(method, request_url,
                                        json=payload,
                                        headers=self.connection.header_dict)

            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.API_KEY)
            if response.status_code >= 400:
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.json())
            if 200 <= response.status_code < 300:
                return komand.helper.clean(response.json())

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            self.logger.info(f"Invalid json: {e}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
        except requests.exceptions.HTTPError as e:
            self.logger.info(f"Call to Trend Micro Apex failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
