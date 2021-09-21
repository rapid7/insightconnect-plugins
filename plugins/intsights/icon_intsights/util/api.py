import json
import time

import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from requests.auth import HTTPBasicAuth


class IntSightAPI:
    def __init__(self, account_id, api_key):
        self.account_id = account_id
        self.api_key = api_key
        self.url = 'https://api.intsights.com'

    def get_indicator_by_value(self, ioc_value: str) -> dict:
        response = self.make_request('GET', f'public/v2/iocs/ioc-by-value?iocValue={ioc_value}')
        if response.status_code == 204:
            return {}

        return response.json()

    def enrich_indicator(self, ioc_value: str) -> dict:
        while True:
            response = self.make_request('GET', f'public/v1/iocs/enrich/{ioc_value}').json()
            if response.get('Status', 'InProgress') in ['Done', 'Failed']:
                break
            time.sleep(5)

        return response

    def test_credentials(self) -> bool:
        return self.make_request('HEAD', 'public/v1/test-credentials').status_code == 200

    def make_request(self, method: str, path: str) -> requests.Response:
        try:
            response = requests.request(
                method=method,
                url=f"{self.url}/{path}",
                headers={"Content-Type": "application/json"},
                verify=True,
                auth=HTTPBasicAuth(self.account_id, self.api_key),
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
                return response

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=e)
        except requests.exceptions.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)
