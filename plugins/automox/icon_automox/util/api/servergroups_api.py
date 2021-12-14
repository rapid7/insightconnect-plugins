from typing import Dict
from icon_automox.util.api_client import ApiClient


class ServerGroupsAPI():
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client
        self.url = f"{api_client.endpoint}/servergroups"

    def get_server_groups(self, init_params={}) -> Dict:
        """
        Retrieve Automox server groups
        :return: Dict of server group id to server group
        """
        params = self.api_client.first_page(init_params)
        server_group_dict = {}
        while True:
            server_groups = self.api_client.call_api("get", self.url, params)

            for sg in server_groups:
                server_group_id = sg.pop('id')
                # Remove duplicate keys that are on policy
                for k in ['wsus_config']:
                    del sg[k]
                server_group_dict[server_group_id] = sg

            if len(server_groups) < ApiClient.PAGE_SIZE:
                break

            self.api_client.next_page(params)

        return server_group_dict
