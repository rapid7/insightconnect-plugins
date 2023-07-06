import requests
from logging import Logger
import time
from requests.auth import HTTPBasicAuth
from insightconnect_plugin_runtime.exceptions import PluginException
from json import JSONDecodeError
from komand_proofpoint_tap.util.exceptions import ApiException


def rate_limiting(max_tries: int):
    def _decorate(func):
        def _wrapper(*args, **kwargs):
            self = args[0]
            retry = True
            counter, delay = 0, 0
            while retry and counter < max_tries:
                if counter:
                    time.sleep(delay)
                try:
                    retry = False
                    return func(*args, **kwargs)
                except ApiException as error:
                    counter += 1
                    delay = 2 ** (counter * 0.6)
                    if error.cause == PluginException.causes[PluginException.Preset.RATE_LIMIT]:
                        self.logger.info(f"Rate limiting error occurred. Retrying in {delay:.1f} seconds.")
                        retry = True
            return func(*args, **kwargs)

        return _wrapper

    return _decorate


class ProofpointTapApi:
    def __init__(self, service_principal: dict, secret: dict, logger: Logger):
        self.base_url = "https://tap-api-v2.proofpoint.com/v2/"
        if service_principal and secret:
            self.service_principal = service_principal.get("secretKey")
            self.secret = secret.get("secretKey")
            self.authorized = True
        else:
            self.authorized = False
        self.logger = logger

    def check_authorization(self):
        if not self.authorized:
            raise PluginException(
                cause="Proofpoint Tap authorization is required for this action.",
                assistance="Please check that credentials are correct and try again.",
            )
        return True

    @rate_limiting(10)
    def _call_api(self, method: str, endpoint: str, params: dict = {}, json_data: dict = {}):  # noqa: C901
        try:
            response = requests.request(
                url=f"{self.base_url}{endpoint}",
                method=method,
                params=params,
                json=json_data,
                auth=HTTPBasicAuth(self.service_principal, self.secret) if self.authorized else None,
            )
            if response.status_code == 401:
                raise ApiException(
                    cause="Invalid service principal or secret provided.",
                    assistance="Verify your service principal and secret are correct.",
                    status_code=response.status_code,
                    data=response.text,
                )
            elif response.status_code == 403:
                raise ApiException(
                    preset=PluginException.Preset.UNAUTHORIZED,
                    status_code=response.status_code,
                    data=response.text,
                )
            elif response.status_code == 404:
                raise ApiException(
                    cause="No results found.",
                    assistance="Please provide valid inputs and try again.",
                    status_code=response.status_code,
                    data=response.text,
                )
            elif response.status_code == 400:
                raise ApiException(
                    preset=PluginException.Preset.BAD_REQUEST,
                    status_code=response.status_code,
                    data=response.text,
                )
            elif response.status_code == 429:
                raise ApiException(
                    preset=PluginException.Preset.RATE_LIMIT,
                    status_code=response.status_code,
                    data=response.text,
                )
            elif 400 < response.status_code < 500:
                raise ApiException(
                    preset=PluginException.Preset.UNKNOWN,
                    status_code=response.status_code,
                    data=response.text,
                )
            elif response.status_code >= 500:
                raise ApiException(
                    preset=PluginException.Preset.SERVER_ERROR,
                    status_code=response.status_code,
                    data=response.text,
                )
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
        query_params["limit"] = 200
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
