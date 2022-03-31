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
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/vnd.manageengine.sdp.v3+json",
        }
        response = requests.request(
            method,
            self.url + path,
            data=data,
            headers=headers,
            # auth=auth
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
