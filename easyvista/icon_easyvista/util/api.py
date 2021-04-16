from insightconnect_plugin_runtime.exceptions import PluginException
from json import JSONDecodeError
import requests
from requests.auth import HTTPBasicAuth
from urllib.parse import urlsplit


class EasyVistaApi:
    def __init__(self, client_login: dict, account: int, url: str):
        self.base_url = f"{self.split_url(url)}/api/v1/{account}/"
        self.username = client_login.get("username")
        self.password = client_login.get("password")

    def _call_api(self, method: str, endpoint: str, json: dict = None):

        response = requests.request(
            url=self.base_url + endpoint,
            method=method,
            json=json,
            auth=HTTPBasicAuth(self.username, self.password),
        )
        if response.status_code == 401:
            raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD)
        if response.status_code == 403:
            raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)
        if response.status_code == 404:
            raise PluginException(
                cause="No results found. Invalid or unreachable endpoint provided.",
                assistance="Please provide valid inputs or verify the endpoint/URL/hostname configured in your plugin"
                " connection is correct.",
            )
        if 400 <= response.status_code < 500:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        if response.status_code >= 500:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)
        try:
            return response.json()
        except JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)

    def ticket_action(self, method: str, payload: dict, rfc_number: str = None) -> dict:
        if method == "POST":
            endpoint = "requests"
        else:
            endpoint = f"requests/{rfc_number}"
        return self.get_reference_number_and_href(self._call_api(method, endpoint, json=payload))

    def search_tickets(self, query: str) -> dict:
        return self._call_api("GET", f"requests?search={query}")

    @staticmethod
    def get_reference_number_and_href(response: dict) -> dict:
        try:
            href = response.get("HREF")
            return {"href_hyperlink": href, "reference_number": href.split("/requests/")[1]}
        except (AttributeError, IndexError) as e:
            raise PluginException(
                cause="EasyVista returned unexpected response.",
                assistance="Please check that the provided inputs are correct and try again.",
                data=e,
            )

    @staticmethod
    def split_url(url: str) -> str:
        scheme, netloc, paths, queries, fragments = urlsplit(url.strip())
        return f"{scheme}://{netloc}"
