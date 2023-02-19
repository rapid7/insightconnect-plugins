import json
import requests
from typing import Optional
from insightconnect_plugin_runtime.exceptions import PluginException


class CiscoUmbrellaEnforcementAPI:
    VERSION = "1.0"

    def __init__(self, customer_key, verify):
        self.verify = verify
        self.url = f"https://s-platform.api.opendns.com/{CiscoUmbrellaEnforcementAPI.VERSION}"
        self.params = {"customerKey": customer_key}

    def get_domains(self):
        """
        Method to make a GET request for list domains action.
        :return: Response containing list of domains
        """
        return self._call_api("GET", "/domains")

    def add_event(self, data):
        """
        Method to make a POST request to register a domain.
        :param data: List of domain information
        :return:
        """
        return self._call_api("POST", "/events", data=data)

    def delete_event(self, name: Optional[str] = None, domain_id: Optional[int] = None):
        """
        Method to make a DELETE request to delete a domain either by name or ID.
        :param name: Name of the domain
        :param domain_id: ID for the domain
        :return: Status code
        """
        if name and domain_id:
            raise PluginException(
                cause="Only one input for delete can be provided.",
                assistance="Either choose name or domain_id, but not both.",
            )

        if name:
            return self._call_api("DELETE", f"/domains/{name}")

        if domain_id:
            return self._call_api("DELETE", f"/domains/{domain_id}")

    def _call_api(
        self,
        # method -> GET/POST/DELETE
        method: str,
        # path -> url
        path: str,
        # data -> payload
        data: Optional = None,
    ):

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        response = requests.request(
            method, self.url + path, params=self.params, data=json.dumps(data), headers=headers, verify=self.verify
        )

        # Error handling
        if response.status_code == 400:
            raise PluginException(cause="Invalid request.")
        if response.status_code == 401:
            raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD)
        if response.status_code == 403:
            raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)
        if response.status_code == 404:
            raise PluginException(preset=PluginException.Preset.NOT_FOUND)
        if response.status_code >= 500:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR)
        if 200 <= response.status_code <= 202:
            return response.json()
        # DELETE returns nothing, so breaks with .json(), so handle seperately.
        if response.status_code == 204:
            return response.text
