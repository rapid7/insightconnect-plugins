import json
import requests
from insightconnect_plugin_runtime.exceptions import PluginException
import time
from requests import Response

from icon_zscaler.util.constants import Assistance, Cause


class ZscalerAPI:
    def __init__(self, url: str, api_key: str, username: str, password: object, logger: object):
        self.url = url.rstrip("/")
        self.url = f"{self.url}/api/v1"
        self.api_key = api_key
        self.username = username
        self.password = password
        self.logger = logger
        self.cookie = None

    def get_status(self) -> Response:
        return self.authenticated_call("GET", "status")

    def activate_configuration(self) -> Response:
        return self.authenticated_call("POST", "status/activate")

    def blacklist_url(self, blacklist_step: str, urls: list) -> bool:
        response = self.authenticated_call(
            "POST",
            f"security/advanced/blacklistUrls?action={blacklist_step}",
            data=json.dumps({"blacklistUrls": urls}),
        )

        return 200 <= response.status_code < 300

    def get_blacklist_url(self) -> str:
        return self.authenticated_call("GET", "security/advanced").json()

    def get_hash_report(self, hash: str):
        return self.authenticated_call(
            "GET",
            f"sandbox/report/{hash}?details=full",
        ).json()

    def url_lookup(self, lookup_url: list):
        return self.authenticated_call("POST", "urlLookup", data=json.dumps(lookup_url)).json()

    def get_users(self, filter_params: dict) -> dict:
        return self.authenticated_call(method="GET", path="users", params=filter_params).json()

    def search_department(self, department_name: str) -> list:
        return self.authenticated_call(method="GET", path="departments", params={"search": department_name}).json()

    def search_groups(self) -> list:
        """Note: The search string used to match against a group's name or comments attributes."""
        return self.authenticated_call(method="GET", path="groups").json()

    def create_user(self, user_data: dict) -> dict:
        return self.authenticated_call(method="POST", path="users", data=json.dumps(user_data)).json()

    def delete_user(self, user_id: int):
        response = self.authenticated_call(method="DELETE", path=f"users/{user_id}")
        return 200 <= response.status_code < 300

    def get_url_category_by_id(self, url_category_id: str) -> dict:
        return self.authenticated_call("GET", f"urlCategories/{url_category_id}").json()

    def list_url_categories(self, custom_only: bool = False) -> list:
        params = {"customOnly": True} if custom_only else {}
        return self.authenticated_call("GET", "urlCategories", params=params).json()

    def update_urls_in_url_category(self, category_id: str, action: str, url_category_data: object) -> dict:
        return self.authenticated_call(
            "PUT", f"urlCategories/{category_id}", data=json.dumps(url_category_data), params={"action": action}
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
                "timestamp": timestamp,
            },
        )

        return response.headers.get("Set-Cookie")

    def authenticated_call(self, method: str, path: str, params: dict = {}, data: str = None) -> Response:
        return self._call_api(
            method,
            path,
            params,
            data,
            headers={
                "content-type": "application/json",
                "cache-control": "no-cache",
                "cookie": self.get_authenticate_cookie(),
            },
        )

    def _call_api(
        self, method: str, path: str, params: dict = {}, data: str = None, json_data: dict = None, headers: dict = None
    ) -> Response:
        try:
            response = requests.request(
                method=method, url=f"{self.url}/{path}", params=params, data=data, json=json_data, headers=headers
            )

            if response.status_code == 401:
                raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD, data=response.text)
            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
            if response.status_code == 404:
                raise PluginException(
                    cause=Cause.RESOURCE_NOT_FOUND,
                    assistance=Assistance.VERIFY_INPUT,
                )
            if response.status_code == 400:
                raise PluginException(
                    cause=Cause.INVALID_DETAILS,
                    assistance=Assistance.VERIFY_INPUT,
                    data=response.text,
                )
            if 400 < response.status_code < 500:
                raise PluginException(
                    preset=PluginException.Preset.UNKNOWN,
                    data=response.json().get("message", response.text),
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
