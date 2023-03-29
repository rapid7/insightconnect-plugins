import json
from logging import Logger
from typing import Optional, Any, Dict
import requests
from requests.auth import HTTPBasicAuth
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.clients.oauth import OAuth20ClientCredentialMixin
from icon_cisco_umbrella_destinations.util.endpoints import Endpoints


class CiscoUmbrellaManagementAPI(OAuth20ClientCredentialMixin):
    def __init__(self, api_key: str, api_secret: str, logger: Logger):
        super().__init__(api_key, api_secret, Endpoints.OAUTH20_TOKEN_URL)
        self.base_url = "https://api.umbrella.com/policies/v2/"
        self.logger = logger

    # DESTINATIONS LIST API

    # GET all destination lists
    # https://developer.cisco.com/docs/cloud-security/#!get-destination-lists
    def get_destination_lists(self) -> dict:
        return self._call_api(
            "GET",
            "destinationlists",
            None,
            None,
            None,
        )

    # GET destination list by ID
    # https://developer.cisco.com/docs/cloud-security/#!get-destination-list
    def get_destination_list(self, destination_list_id: int) -> dict:
        return self._call_api(
            "GET",
            f"destinationlists/{destination_list_id}",
            None,
            None,
            None,
        )

    # POST a new destination list
    # https://developer.cisco.com/docs/cloud-security/#!create-destination-list
    def create_destination_list(self, data: dict) -> dict:
        return self._call_api(
            "POST",
            "destinationlists",
            data,
            None,
            None,
        )

    # PATCH (Update) destination list
    # https://developer.cisco.com/docs/cloud-security/#!update-destination-lists
    def update_destination_list(self, destination_list_id: int, data: dict) -> dict:
        return self._call_api(
            "PATCH",
            f"destinationlists/{destination_list_id}",
            data,
            None,
            None,
        )

    # DELETE destination list
    # https://developer.cisco.com/docs/cloud-security/#!delete-destination-list
    def delete_destination_list(self, destination_list_id: int) -> dict:
        return self._call_api(
            "DELETE",
            f"destinationlists/{destination_list_id}",
            None,
            None,
            None,
        )

    # DESTINATIONS API

    # GET list of destinations related to destination list
    # https://developer.cisco.com/docs/cloud-security/#!get-destinations
    def get_destinations(self, destination_list_id: int) -> dict:
        return self._call_api(
            "GET",
            f"destinationlists/{destination_list_id}/destinations",
            None,
            None,
            None,
        )

    # POST destinations to existing destination list
    # https://developer.cisco.com/docs/cloud-security/#!create-destinations
    def create_destinations(self, destination_list_id: int, data: dict) -> dict:
        return self._call_api(
            "POST",
            f"destinationlists/{destination_list_id}/destinations",
            data,
            None,
            None,
        )

    # DELETE list of destinations from destination list
    # https://developer.cisco.com/docs/cloud-security/#!delete-destinations
    def delete_destinations(self, destination_list_id: int, data) -> dict:
        return self._call_api(
            "DELETE",
            f"destinationlists/{destination_list_id}/destinations/remove",
            data,
            None,
            None,
        )

    def _call_api(
        self,
        # method -> GET/POST/etc
        method: str,
        # path -> url
        path: str,
        # json_data -> Json to send in body
        json_data: Optional[dict] = None,
        # Params -> Query (Params) String
        params: Optional[dict] = None,
        # data(payload) -> dict in body
        data: Optional = None,
    ) -> dict:
        # Prevents json.dumps() on 'None' data
        if not data:
            data_string = None
        else:
            data_string = json.dumps(data)

        response = self.oauth.request(method, self.base_url + path, json=json_data, params=params, data=data_string)
        if response.status_code == 400:
            raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response.json())
        if response.status_code == 401:
            raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD, data=response.json())
        if response.status_code == 403:
            raise PluginException(preset=PluginException.Preset.UNAUTHORIZED, data=response.json())
        if response.status_code == 404:
            raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.json())
        if response.status_code >= 500:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.json())
        if 200 <= response.status_code < 300:
            return response.json()
