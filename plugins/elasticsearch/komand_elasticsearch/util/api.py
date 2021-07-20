import json
import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from requests import Response
from requests.auth import HTTPBasicAuth


class ElasticSearchAPI:
    def __init__(self, url: str, logger: object, username: str = None, password: str = None):
        self.url = url.rstrip("/")
        self.username = username
        self.password = password
        self.logger = logger

    def test_auth(self):
        return self._call_api("GET", "/")

    def index(self, index: str, _id: str = None, params: dict = None, document: dict = None):
        if _id:
            return self._call_api("PUT", f"{index}/_doc/{_id}", params, json_data=document)

        return self._call_api("POST", f"{index}/_doc", params, json_data=document)

    def put_index(self, index: str, _id: str, params: dict = None):
        return self._call_api("PUT", f"{index}/_doc/{_id}", params)

    def update(self, index: str, _id: str, params: dict = None, script: dict = None):
        return self._call_api("POST", f"{index}/_update/{_id}", params, {"script": script})

    def search_documents(self, index: str, json_data: dict = {}, params: dict = None):

        json_data["version"] = True

        return self._call_api("GET", f"{index}/_search?", params, json_data)

    def cluster_health(self):
        return self._call_api("GET", "_cluster/health")

    def _call_api(self, method: str, path: str, params: dict = None, json_data: dict = None) -> Response:
        try:
            response = requests.request(
                method,
                f"{self.url}/{path}",
                params=params,
                json=json_data,
                headers={"Content-Type": "application/json"},
                auth=HTTPBasicAuth(self.username, self.password) if self.username else None,
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
                    data=response.json().get("message", response.text),
                )
            if response.status_code >= 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)

            if 200 <= response.status_code < 300:
                return response.json()

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=e)
        except requests.exceptions.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)
