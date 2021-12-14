from typing import Dict
from icon_automox.util.api_client import ApiClient


class OrgsAPI():
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client
        self.url = f"{api_client.endpoint}/orgs"

    def get_orgs(self, init_params={}) -> Dict:
        """
        Retrieve Automox organizations
        :return: Dict of organization id to org name
        """
        params = self.api_client.first_page(init_params)
        orgs_dict = {}
        while True:
            orgs = self.api_client.call_api("get", self.url, params)

            for o in orgs:
                orgs_dict[o['id']] = o['name']

            if len(orgs) < ApiClient.PAGE_SIZE:
                break

            self.api_client.next_page(params)

        return orgs_dict
