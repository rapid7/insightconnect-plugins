import json
from logging import Logger
import requests
from typing import Union
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean
from icon_bitwarden.util.endpoints import (
    COLLECTIONS_ENDPOINT,
    EVENTS_ENDPOINT,
    GROUPS_ENDPOINT,
    MEMBERS_ENDPOINT,
    MEMBERS_ID_ENDPOINT,
    MEMBERS_GROUP_IDS_ENDPOINT,
    REINVITE_MEMBER_ENDPOINT,
    TOKEN_ENDPOINT,
)
from icon_bitwarden.util.constants import Assistance, Cause, ValueType


class BitwardenAPI:
    def __init__(self, client_id: str, client_secret: str, logger: Logger):
        self._client_id = client_id
        self._client_secret = client_secret
        self._logger = logger
        self._auth_token = None

    @property
    def auth_token(self) -> str:
        self._logger.info("[API] Getting authentication token...")
        response = requests.request(
            method="POST",
            url=TOKEN_ENDPOINT,
            data={
                "grant_type": "client_credentials",
                "scope": "api.organization",
                "client_id": self._client_id,
                "client_secret": self._client_secret,
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        if response.status_code == 200:
            self._auth_token = response.json().get("access_token")
            return self._auth_token
        if response.status_code == 400:
            raise PluginException(cause=Cause.INVALID_REQUEST, assistance=Assistance.VERIFY_INPUT, data=response.text)
        if response.status_code == 401:
            raise PluginException(cause=Cause.INVALID_AUTH_DATA, assistance=Assistance.VERIFY_AUTH, data=response.text)
        else:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)

    @auth_token.setter
    def auth_token(self, auth_token):
        self._auth_token = auth_token

    def get_headers(self) -> dict:
        return {"Content-Type": "application/json", "Authorization": f"Bearer {self.auth_token}"}

    def retrieve_member(self, member_id: str) -> dict:
        return self.make_json_request(method="GET", url=MEMBERS_ID_ENDPOINT.format(id=member_id))

    def list_all_collections(self) -> dict:
        response_json = self.make_json_request(method="GET", url=COLLECTIONS_ENDPOINT)
        return response_json.get("data")

    def list_all_groups(self) -> dict:
        return self.make_json_request(method="GET", url=GROUPS_ENDPOINT)

    def list_all_members(self) -> dict:
        return self.make_json_request(method="GET", url=MEMBERS_ENDPOINT)

    def list_events(self, parameters: dict) -> list:
        return self.make_json_request(method="GET", url=EVENTS_ENDPOINT, params=parameters)

    def reinvite_member(self, member_id: str) -> bool:
        self.make_request(method="POST", url=REINVITE_MEMBER_ENDPOINT.format(id=member_id))
        return True

    def retrieve_members_group_ids(self, member_id: str) -> list:
        return self.make_json_request(method="GET", url=MEMBERS_GROUP_IDS_ENDPOINT.format(id=member_id))

    def update_members_group_ids(self, member_id: str, json_data: dict) -> bool:
        self.make_request(method="PUT", url=MEMBERS_GROUP_IDS_ENDPOINT.format(id=member_id), json_data=json_data)
        return True

    def create_member(self, json_data: dict) -> dict:
        return self.make_json_request(method="POST", url=MEMBERS_ENDPOINT, json_data=json_data)

    def update_member(self, member_id: str, json_data: dict) -> dict:
        return self.make_json_request(method="PUT", url=MEMBERS_ID_ENDPOINT.format(id=member_id), json_data=json_data)

    def delete_member(self, member_id: str) -> bool:
        self.make_request(method="DELETE", url=MEMBERS_ID_ENDPOINT.format(id=member_id))
        return True

    def make_request(self, method: str, url: str, json_data: dict = None, params: dict = None) -> requests.Response:
        try:
            response = requests.request(
                method=method, url=url, headers=self.get_headers(), json=json_data, params=params
            )

            if response.status_code == 400:
                raise PluginException(
                    cause=Cause.INVALID_REQUEST, assistance=Assistance.VERIFY_INPUT, data=response.text
                )
            if response.status_code == 401:
                raise PluginException(
                    cause=Cause.INVALID_AUTH_DATA, assistance=Assistance.VERIFY_AUTH, data=response.text
                )
            if response.status_code == 404:
                raise PluginException(cause=Cause.NOT_FOUND, assistance=Assistance.VERIFY_INPUT, data=response.text)
            if response.status_code == 429:
                raise PluginException(
                    cause=Cause.TOO_MANY_REQUESTS, preset=PluginException.Preset.RATE_LIMIT, data=response.text
                )
            if 400 < response.status_code < 500:
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
            if response.status_code >= 500:
                raise PluginException(cause=Cause.SERVER_ERROR, assistance=Assistance.SERVER_ERROR, data=response.text)
            if 200 <= response.status_code < 300:
                return response

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except requests.exceptions.HTTPError as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    def make_json_request(
        self, method: str, url: str, json_data: dict = None, params: dict = None
    ) -> Union[dict, list]:
        try:
            response = self.make_request(method=method, url=url, json_data=json_data, params=params)
            return clean(response.json())
        except json.decoder.JSONDecodeError as error:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)
