import requests
from requests.auth import HTTPBasicAuth
from insightconnect_plugin_runtime.exceptions import PluginException
from json import JSONDecodeError


class ProofpointTapApi:
    def __init__(self, service_principal: dict, secret: dict):
        self.base_url = "https://tap-api-v2.proofpoint.com/v2/"
        if service_principal and secret:
            self.service_principal = service_principal.get("secretKey")
            self.secret = secret.get("secretKey")
            self.authorized = True
        else:
            self.authorized = False

    def check_authorization(self):
        if not self.authorized:
            raise PluginException(
                cause="Proofpoint Tap authorization is required for this action.",
                assistance="Please check that credentials are correct and try again.",
            )
        return True

    def _call_api(self, method: str, endpoint: str, params: dict = None, json_data: dict = None):
        try:
            response = requests.request(
                url=self.base_url + endpoint,
                method=method,
                params=params,
                json=json_data,
                auth=HTTPBasicAuth(self.service_principal, self.secret) if self.authorized else None,
            )
            if response.status_code == 401:
                raise PluginException(
                    cause="Invalid service principal or secret provided.",
                    assistance="Verify your service principal and secret are correct.",
                )
            elif response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)
            elif response.status_code == 404:
                raise PluginException(
                    cause="No results found.",
                    assistance="Please provide valid inputs and try again.",
                )
            elif 400 <= response.status_code < 500:
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
            elif response.status_code >= 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)
            elif 200 <= response.status_code < 300:
                if not response.text:
                    return {}
                return response.json()
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=e)
        except requests.exceptions.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)

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
            total_clickers += response.get("totalTopClickers", 0)
            query_params["page"] += 1
            response = self._call_api("GET", "people/top-clickers", params=query_params)
        return {"users": users, "totalTopClickers": total_clickers, "interval": response.get("interval")}

    def get_decoded_url(self, payload: dict):
        return self._call_api("POST", "url/decode", json_data=payload)

    def get_forensics(self, payload: dict):
        return self._call_api("GET", "forensics", params=payload)


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
