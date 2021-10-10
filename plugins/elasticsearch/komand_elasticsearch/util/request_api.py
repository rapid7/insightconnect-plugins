import json
import requests
from logging import Logger
from insightconnect_plugin_runtime.exceptions import PluginException
from requests.auth import HTTPBasicAuth
from insightconnect_plugin_runtime import helper


class RequestAPI:
    def __init__(self, url: str, logger: Logger, ssl_verify: bool, username: str = None, password: str = None):
        self.url: str = url.rstrip("/")
        self.username: str = username
        self.password: str = password
        self.ssl_verify: bool = ssl_verify
        self.logger: Logger = logger

    def get_main_version(self) -> str:
        number: str = self._call_api("GET", "").get("version", {}).get("number", "")
        if number:
            return number[0]

        return "7"

    def cluster_health(self) -> dict:
        return self._call_api("GET", "_cluster/health")

    def test_auth(self):
        return self._call_api("GET", "/")

    def _index(self, index: str, _type: str, _id: str = None, params: dict = None, document: dict = None) -> dict:
        if _id:
            return self._call_api("PUT", f"{index}/{_type}/{_id}", params, json_data=document)

        return self._call_api("POST", f"{index}/{_type}", params, json_data=document)

    def _search_first_page(self, path: str, routing: str, scroll_time: str, json_data: dict = {}):
        query = None
        if json_data:
            query = {"query": json_data, "version": "true"}

        return self._call_api(
            method="GET",
            path=path,
            params=helper.clean({"routing": routing, "size": 5, "scroll": scroll_time}),
            json_data=query,
        )

    def _get_scroll_page(self, scroll_id: str, scroll_time: str):
        return self._call_api(
            method="GET", path="_search/scroll", json_data={"scroll": scroll_time, "scroll_id": scroll_id}
        )

    def _search_documents(self, path: str, routing: str, json_data: dict = {}) -> dict:
        scroll_time = "10m"
        first_page = self._search_first_page(path=path, routing=routing, scroll_time=scroll_time, json_data=json_data)
        scroll_id = first_page.get("_scroll_id")
        hits = first_page.get("hits", {}).get("hits", [])
        took = first_page.get("took", 0)
        total = first_page.get("hits", {}).get("total")
        if isinstance(total, dict):
            total = total.get("value", 0)
        elif total is None:
            total = 0

        for _ in range(0, 9999):
            if scroll_id:
                try:
                    scroll_page = self._get_scroll_page(scroll_id, scroll_time)
                    page_hits = scroll_page.get("hits", {}).get("hits", [])
                    if not page_hits:
                        break
                    hits.extend(page_hits)
                    took += scroll_page.get("took", 0)
                    scroll_id = scroll_page.get("_scroll_id")
                except PluginException:
                    break

        return {
            "took": took,
            "timed_out": first_page.get("timed_out", "false"),
            "terminated_early": first_page.get("terminated_early", "false"),
            "_shards": first_page.get("_shards", {}),
            "hits": {
                "total": {"value": total},
                "max_score": first_page.get("hits", {}).get("max_score", 0),
                "hits": hits,
            },
        }

    def _call_api(self, method: str, path: str, params: dict = None, json_data: dict = None) -> dict:
        try:
            response = requests.request(
                method,
                f"{self.url}/{path}",
                params=params,
                json=json_data,
                headers={"Content-Type": "application/json"},
                verify=self.ssl_verify,
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
