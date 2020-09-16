import json
import requests
from insightconnect_plugin_runtime.exceptions import PluginException
import time
from requests import Response


class ZscalerAPI:
    def __init__(self, url: str, api_key: str, username: str, password: object, logger: object):
        self.url = url.rstrip("/")
        self.url = f"{self.url}/api/v1"
        self.api_key = api_key
        self.username = username
        self.password = password
        self.logger = logger
        self.cookie = None

    def get_status(self):
        return self.authenticated_call(
            "GET",
            "status"
        )

    def get_hash_report(self, hash: str):
        return self.authenticated_call(
            "GET",
            f"sandbox/report/{hash}?details=full",
        ).json()

    def url_lookup(self, lookup_url: list):
        return self.authenticated_call(
            "POST",
            "urlLookup",
            data=json.dumps(lookup_url)
        ).json()

    def get_authenticate_cookie(self):
        timestamp = str(int(time.time() * 1000))
        response = self._call_api(
            "POST",
            "authenticatedSession",
            json_data={
                "apiKey": self.obfuscate_api_key(timestamp),
                "username": self.username,
                "password": self.password,
                "timestamp": timestamp
            }
        )

        return response.headers.get("Set-Cookie")

    def authenticated_call(
            self,
            method: str,
            path: str,
            data: str = None
    ) -> Response:
        return self._call_api(
            method,
            path,
            data,
            headers={
                'content-type': "application/json",
                'cache-control': "no-cache",
                'cookie': self.get_authenticate_cookie()
            }
        )

    def _call_api(
            self,
            method: str,
            path: str,
            data: str = None,
            json_data: dict = None,
            headers: dict = None
    ) -> Response:
        try:
            response = requests.request(
                method,
                f"{self.url}/{path}",
                data=data,
                json=json_data,
                headers=headers
            )

            if response.status_code == 401:
                raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD, data=response.text)
            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
            if response.status_code == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.text)
            if 400 <= response.status_code < 500:
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
            if response.status_code >= 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)

            if 200 <= response.status_code < 300:
                return response

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=e)
        except requests.exceptions.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)

    def obfuscate_api_key(self, now: str):
        seed = self.api_key
        n = now[-6:]
        r = str(int(n) >> 1).zfill(6)
        key = ""
        for i in range(0, len(str(n)), 1):
            key += seed[int(str(n)[i])]
        for j in range(0, len(str(r)), 1):
            key += seed[int(str(r)[j]) + 2]

        return key
