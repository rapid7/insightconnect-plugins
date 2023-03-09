import json
from logging import Logger
import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean
from icon_cloudflare.util.constants import Assistance, Cause
from icon_cloudflare.util.endpoints import (
    ACCOUNTS_ENDPOINT,
    LISTS_ENDPOINT,
    ZONE_ACCESS_RULE_ENDPOINT,
    ZONE_ACCESS_RULES_ENDPOINT,
    ZONES_ENDPOINT,
)


class CloudflareAPI:
    def __init__(self, api_token: str, logger: Logger):
        self._logger = logger
        self._api_token = api_token

    def get_headers(self) -> dict:
        return {"Content-Type": "application/json", "Authorization": f"Bearer {self._api_token}"}

    def get_accounts(self, parameters: dict = None) -> dict:
        return self.make_json_request(method="GET", url=ACCOUNTS_ENDPOINT, params=parameters)

    def get_zones(self, parameters: dict) -> dict:
        return self.make_json_request(method="GET", url=ZONES_ENDPOINT, params=parameters)

    def get_lists(self, account_id: str) -> dict:
        return self.make_json_request(method="GET", url=LISTS_ENDPOINT.format(account_id=account_id))

    def create_zone_access_rule(self, zone_id: str, json_data: dict) -> dict:
        return self.make_json_request(
            method="POST", url=ZONE_ACCESS_RULES_ENDPOINT.format(zone_id=zone_id), json_data=json_data
        )

    def delete_zone_access_rule(self, zone_id: str, rule_id: str) -> bool:
        self.make_json_request(method="DELETE", url=ZONE_ACCESS_RULE_ENDPOINT.format(zone_id=zone_id, rule_id=rule_id))
        return True

    def get_zone_access_rules(self, zone_id: str, parameters: dict) -> dict:
        return self.make_json_request(
            method="GET", url=ZONE_ACCESS_RULES_ENDPOINT.format(zone_id=zone_id), params=parameters
        )

    def make_request(self, method: str, url: str, json_data: dict = None, params: dict = None) -> requests.Response:
        try:
            response = requests.request(
                method=method, url=url, headers=self.get_headers(), json=json_data, params=params
            )

            if response.status_code == 400:
                raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response.text)
            if response.status_code == 403:
                raise PluginException(
                    cause=Cause.INVALID_TOKEN, assistance=Assistance.INVALID_TOKEN, data=response.text
                )
            if response.status_code == 404:
                raise PluginException(cause=Cause.NOT_FOUND, assistance=Assistance.NOT_FOUND, data=response.text)
            if response.status_code == 429:
                raise PluginException(cause=PluginException.Preset.RATE_LIMIT, data=response.text)
            if 400 < response.status_code < 500:
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
            if response.status_code >= 500:
                raise PluginException(cause=PluginException.Preset.SERVER_ERROR, data=response.text)
            if 200 <= response.status_code < 300:
                return response

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except requests.exceptions.HTTPError as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    def make_json_request(self, method: str, url: str, json_data: dict = None, params: dict = None) -> dict:
        try:
            response = self.make_request(method=method, url=url, json_data=json_data, params=params)
            return clean(response.json())
        except json.decoder.JSONDecodeError as error:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)
