from insightconnect_plugin_runtime.helper import clean
import requests
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
import json
from logging import Logger
from urllib.parse import urljoin


class AbnormalSecurityAPI:
    def __init__(self, hostname: str, api_key: str, logger: Logger):
        self.base_url = f"https://{hostname}/v1"
        self.api_key = api_key
        self.headers = {
            "x-mock-match-request-headers": "authorization",
            "authorization": f"Bearer {api_key}"
        }
        self.session = requests.session()
        self.logger = logger

    def connect(self):
        login_response = self.session.get(
            f"{self.base_url}/threats",
            headers=self.headers,
        )

        if login_response.status_code not in range(200, 299):
            raise ConnectionTestException(
                preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE,
                data="There is a problem connecting to Abnormal Security. Please check your API Key or permissions.",
            )

    def send_request(
        self, method: str, path: str, params: dict = None, payload: dict = None
    ) -> dict:
        try:
            response = self.session.request(
                method.upper(),
                urljoin(self.base_url, path),
                params=params,
                json=payload,
                headers=self.headers,
            )

            if response.status_code == 401:
                raise PluginException(
                    preset=PluginException.Preset.USERNAME_PASSWORD, data=response.text
                )
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
                raise PluginException(
                    preset=PluginException.Preset.SERVER_ERROR, data=response.text
                )

            if 200 <= response.status_code < 300:
                return clean(json.loads(response.content))

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=e)
        except requests.exceptions.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)
