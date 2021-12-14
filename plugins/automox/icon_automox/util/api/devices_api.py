from typing import Dict, List
from icon_automox.util.api_client import ApiClient


class DevicesAPI():
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client
        self.url = f"{api_client.endpoint}/servers"

    def get_devices(self, init_params={}, group_id=None) -> List[Dict]:
        """
        Retrieve Automox console endpoints
        :return: Iterator containing list of endpoints
        """
        params = self.api_client.first_page(init_params)
        if group_id is not None and (group_id != 0):
            params["groupId"] = group_id
        while True:
            endpoints = self.api_client.call_api("get", self.url, params)

            yield endpoints

            if len(endpoints) < ApiClient.PAGE_SIZE:
                break

            self.api_client.next_page(params)

    @staticmethod
    def sanitize_endpoint(endpoint) -> Dict:
        for field in ['total_count']:
            try:
                del endpoint[field]
            except KeyError:
                pass
        return endpoint

    def get_device_software(self, device_id, init_params={}) -> List[Dict]:
        """
        Retrieve Automox endpoint software by device id
        :return: Iterator containing list of software
        """
        params = self.api_client.first_page(init_params)
        while True:
            software = self.api_client.call_api("get", f"{self.url}/{device_id}/packages", params)

            yield software

            if len(software) < ApiClient.PAGE_SIZE:
                break

            self.api_client.next_page(params)
