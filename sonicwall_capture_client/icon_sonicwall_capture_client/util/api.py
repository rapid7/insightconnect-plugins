import json
import requests
from collections import OrderedDict
from insightconnect_plugin_runtime.exceptions import PluginException


class SonicWallAPI:
    def __init__(self, username, password, logger):
        self.url = "https://captureclient.sonicwall.com/api/"
        self.verify_ssl = True
        self.logger = logger
        self.username = username
        self.password = password
        self.token = None

    def get_endpoint(self, device_id: str, install_token: str):
        return self._make_request(
            "GET",
            f"endpoints/{device_id}/{install_token}"
        )

    def get_endpoints_list(self):
        return self._run_with_pages_endpoints(
            "endpoints/list"
        )

    def get_access_token(self):
        if self.token:
            return self.token

        self.token = self._call_api("POST", "login", json_data={
            "email": self.username,
            "password": self.password
        }).get("token")

        return self.token

    def logout(self, token):
        self._call_api("DELETE", "login", token=token)

    def _run_with_pages_endpoints(self, path: str, value: str = None):
        objects = []
        limit = 100
        for page in range(0, 9999):
            response = self._make_request(
                "GET",
                path,
                params={
                    "limit": limit,
                    "skip": page * limit
                }
            )
            objects.extend(response.get("devices", []))

            if value and response.get("value") == value:
                return response.get("devices", [])

            if (page + 1) * limit > response.get("pagination", {}).get("totalItems", 0):
                break

        return objects

    def _make_request(self, method: str, path: str, json_data: dict = None, params: dict = None):
        token = self.get_access_token()
        try:
            response = self._call_api(method, path, token=token, json_data=json_data, params=params)
        except PluginException as e:
            raise PluginException(cause=e.cause, assistance=e.assistance, data=e.data)

        return response

    def _call_api(self, method: str, path: str, token: str = None, json_data: dict = None, params: dict = None):
        response = {"text": ""}
        headers_list = [('Accept', 'application/json')]
        if token:
            headers_list.append(('Authorization', token))

        try:
            response = requests.request(method, self.url + path,
                                        json=json_data,
                                        params=params,
                                        headers=OrderedDict(headers_list),
                                        verify=self.verify_ssl)

            if response.status_code == 401:
                raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD)
            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)
            if response.status_code >= 400:
                response_data = response.text
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response_data)
            if 200 <= response.status_code < 300:
                return response.json()

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            self.logger.info(f"Invalid JSON: {e}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
        except requests.exceptions.HTTPError as e:
            self.logger.info(f"Call to SonicWall Capture Client API failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
