import json
from json import JSONDecodeError
from logging import Logger
from typing import Optional
import requests
from requests.auth import HTTPBasicAuth
from insightconnect_plugin_runtime.exceptions import PluginException


class CiscoUmbrellaManagementAPI:
    def __init__(self, api_key: str, api_secret: str, organization_id: int, logger=None):
        self.url = "https://management.api.umbrella.com/v1/"
        self.api_key = api_key
        self.api_secret = api_secret
        self.org_id = organization_id
        self.logger = logger

    # DESTINATIONS LIST API

    # GET all destination lists
    # https://developer.cisco.com/docs/cloud-security/#!get-destination-lists
    def get_destination_lists(self) -> dict:
        return self._call_api(
            "GET",
            f"organizations/{self.org_id}/destinationlists",
            None,
            None,
            None,
            action_name="GET all destination lists",
        )

    # GET destination list by ID
    # https://developer.cisco.com/docs/cloud-security/#!get-destination-list
    def get_destination_list(self, destination_list_id: int) -> dict:
        return self._call_api(
            "GET",
            f"organizations/{self.org_id}/destinationlists/{destination_list_id}",
            None,
            None,
            None,
            action_name="GET destination list by ID",
        )

    # POST a new destination list
    # https://developer.cisco.com/docs/cloud-security/#!create-destination-list
    def create_destination_list(self, data: dict) -> dict:
        return self._call_api(
            "POST",
            f"organizations/{self.org_id}/destinationlists",
            None,
            None,
            data=data,
            action_name="Create a new destination list",
        )

    # PATCH (Update) destination list
    # https://developer.cisco.com/docs/cloud-security/#!update-destination-lists
    def update_destination_list(self, destination_list_id: int, data: dict) -> dict:
        return self._call_api(
            "PATCH",
            f"organizations/{self.org_id}/destinationlists/{destination_list_id}",
            None,
            None,
            data=data,
            action_name="Update destination list name by ID",
        )

    # DELETE destination list
    # https://developer.cisco.com/docs/cloud-security/#!delete-destination-list
    def delete_destination_list(self, destination_list_id: int) -> dict:
        return self._call_api(
            "DELETE",
            f"organizations/{self.org_id}/destinationlists/{destination_list_id}",
            None,
            None,
            None,
            action_name="Delete destination list by ID",
        )

    # DESTINATIONS API

    # GET list of destinations related to destination list
    # https://developer.cisco.com/docs/cloud-security/#!get-destinations
    def get_destinations(self, destination_list_id: int) -> dict:
        return self._call_api(
            "GET",
            f"organizations/{self.org_id}/destinationlists/{destination_list_id}/destinations",
            None,
            None,
            None,
            action_name="GET list of destinations in destionation list",
        )

    # POST destinations to existing destination list
    # https://developer.cisco.com/docs/cloud-security/#!create-destinations
    def create_destinations(self, destination_list_id: int, data: dict) -> dict:
        return self._call_api(
            "POST",
            f"organizations/{self.org_id}/destinationlists/{destination_list_id}/destinations",
            None,
            None,
            data=data,
            action_name="Create destinations in existing destination list",
        )

    # DELETE list of destinations from destination list
    # https://developer.cisco.com/docs/cloud-security/#!delete-destinations
    def delete_destinations(self, destination_list_id: int, data) -> dict:
        return self._call_api(
            "DELETE",
            f"organizations/{self.org_id}/destinationlists/{destination_list_id}/destinations/remove",
            None,
            None,
            data=data,
            action_name="Delete destinations from destination list",
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
        # Action name -> Hard coded written action name for error messages
        action_name: Optional[str] = None,
    ) -> dict:

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        try:
            # Prevents json.dumps() on 'None' data
            if data is None:
                data_string = None
            else:
                data_string = json.dumps(data)
            response = requests.request(
                method,
                self.url + path,
                json=json_data,
                params=params,
                data=data_string,
                headers=headers,
                auth=HTTPBasicAuth(self.api_key, self.api_secret),
            )

            if response.status_code == 401:
                raise PluginException(
                    preset=PluginException.Preset.USERNAME_PASSWORD,
                    cause=f"Invalid request for {action_name}. Invalid API key provided.",
                    assistance="Verify your API key is correct.",
                )
            if response.status_code == 403:
                raise PluginException(
                    preset=PluginException.Preset.UNAUTHORIZED,
                    cause=f"Invalid request for {action_name}. Unauthorized access to this service.",
                    assistance="Verify the permissions for your account and try again.",
                )
            if response.status_code == 404:
                raise PluginException(
                    preset=PluginException.Preset.NOT_FOUND,
                    cause=f"Invalid request for {action_name}. The requested item was not found.",
                    assistance="Check the syntax of your query and try again.",
                )
            if response.status_code >= 500:
                raise PluginException(
                    preset=PluginException.Preset.SERVER_ERROR,
                    cause=f"Invalid request for {action_name}. Server Error.",
                    data=response.text,
                )
            if 200 <= response.status_code < 300:
                try:
                    return response.json()
                except JSONDecodeError:
                    raise PluginException(
                        preset=PluginException.Preset.INVALID_JSON,
                        cause=f"Invalid request for {action_name}. Invalid JSON returned",
                        data=response.text,
                    )

        except requests.exceptions.HTTPError as e:
            self.logger.info(f"Call to Cisco Umbrella Management API failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text) from e
