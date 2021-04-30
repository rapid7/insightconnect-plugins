import requests
from requests.auth import HTTPBasicAuth
from insightconnect_plugin_runtime.exceptions import PluginException
from json import JSONDecodeError


class ProofpointTapApi:
    def __init__(self, service_principal: dict, secret: dict):
        self.base_url = "https://tap-api-v2.proofpoint.com/v2/"
        self.service_principal = service_principal.get("secretKey")
        self.secret = secret.get("secretKey")

    def _call_api(self, method: str, endpoint: str, params: dict = None):
        response = requests.request(
            url=self.base_url + endpoint,
            method=method,
            params=params,
            auth=HTTPBasicAuth(self.service_principal, self.secret),
        )
        if response.status_code == 401:
            raise PluginException(
                cause="Invalid service principal or secret provided.",
                assistance="Verify your service principal and secret are correct.",
            )
        if response.status_code == 403:
            raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)
        if response.status_code == 404:
            raise PluginException(
                cause="No results found.",
                assistance="Please provide valid inputs and try again.",
            )
        if 400 <= response.status_code < 500:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        if response.status_code >= 500:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)
        try:
            return response.json()
        except JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)

    def siem_action(self, endpoint: str, query_params: dict) -> dict:
        return self._call_api("GET", endpoint, params=query_params)

    def get_top_clickers(self, query_params: dict) -> dict:
        users = []
        total_clickers = 0
        query_params["page"] = 1
        response = self._call_api("GET", "people/top-clickers", params=query_params)
        while response.get("users"):
            for i in response.get("users"):
                users.append(i)
            total_clickers += response.get("totalTopClickers")
            query_params["page"] += 1
            response = self._call_api("GET", "people/top-clickers", params=query_params)
        response["users"] = users
        response["totalTopClickers"] = total_clickers
        return response


class Endpoint:
    @staticmethod
    def get_blocked_clicks() -> str:
        return "siem/clicks/blocked"

    @staticmethod
    def get_permitted_clicks() -> str:
        return "siem/clicks/permitted"

    @staticmethod
    def get_blocked_messages() -> str:
        return "siem/messages/blocked"

    @staticmethod
    def get_delivered_threats() -> str:
        return "siem/messages/delivered"

    @staticmethod
    def get_all_threats() -> str:
        return "siem/all"
