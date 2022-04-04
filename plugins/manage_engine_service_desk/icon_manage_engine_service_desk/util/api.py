import json
import requests
from typing import Optional
from logging import Logger
from insightconnect_plugin_runtime.exceptions import PluginException


class ManageEngineAPI:
    def __init__(self, api_key: str, logger=None):
        self.url = "https://sdpondemand.manageengine.eu/"
        self.api_key = api_key
        self.logger = logger

    # Add request
    # https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request.html#add-request
    def add_request(self, data: dict) -> dict:
        return self._call_api("POST", "api/v3/requests", data=data)

    # Edit request
    # https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request.html#edit-request
    def edit_request(self, data: dict, request_id: int) -> dict:
        return self._call_api("PUT", f"api/v3/requests/{request_id}", data=data)

    # Delete request
    # https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request.html#delete-request
    def delete_request(self, request_id: int):
        return self._call_api("DELETE", f"api/v3/requests/{request_id}", None)

    # Get request
    # https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request.html#get-request
    def get_request(self, request_id: int):
        return self._call_api("GET", f"api/v3/requests/{request_id}", None)

    # Get ALL requests
    # https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request.html#get-list-request
    def get_list_request(self) -> dict:
        return self._call_api(
            "GET",
            "api/v3/requests",
            None,
        )

    def _call_api(
        self,
        # method -> GET/POST/DELETE/etc
        method: str,
        # path == URL
        path: str,
        # data(payload) -> dict in body
        data: Optional = None,
    ) -> dict:

        headers = {
            "Accept": "application/v3+json",
            "Authorization": f"Zoho-oauthtoken {self.api_key}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        response = requests.request(
            method,
            self.url + path,
            data=data,
            headers=headers,
        )
        if response.status_code == 400:
            raise PluginException(cause="Theres a fair few reasons why this isn't working. Good luck figuring it out")
        if response.status_code == 403:
            raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)
        if response.status_code == 404:
            raise PluginException(preset=PluginException.Preset.NOT_FOUND)
        if response.status_code == 500:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR)
        if 200 <= response.status_code < 300:
            return response.json()

    def _extract_status_code(self, input_dict: dict):
        # TODO: Implement a method to extract the status code from the error message

        pass
