from insightconnect_plugin_runtime.helper import clean
from insightconnect_plugin_runtime.exceptions import PluginException
from logging import Logger
from urllib.parse import urlsplit
from armorblox.client import Client


class ArmorbloxAPI(Client):

    def __init__(self, api_key: str, tenant_name: str, logger = Logger):
        super().__init__(api_key=api_key, instance_name=tenant_name)
        self.logger = logger
        self.incidents_list = []

    def process_incidents(self, params):
        self.incidents_list = []
        try:
            response_json, next_page_token, total_count = self.incidents.list(params=params)
            self.incidents_list.extend(response_json)
            while next_page_token:
                params["page_token"] = next_page_token
                response_json, next_page_token, total_count = self.incidents.list(params=params)
                self.incidents_list.extend(response_json)
        except Exception as credentials_exp:
            PluginException('Incorrect Credentials. ' + str(credentials_exp))

    def get_incidents(self, from_date: str = None, to_date: str = None):
        """
        Hits the Armorblox API and fetch incidents.
        
        :param from_date: Custom time filter parameter
        :param to_date: Custom time filter parameter
        
        :return: List of incidents
        """
        params = {
            "from_date": from_date,
            "to_date": to_date,
            "orderBy": "ASC"
        }
        self.process_incidents(params)
        return self.incidents_list

    def get_remediation_action(self, incident_id):
        """
        Returns the remediation action(s) for the input incident.
        """
        rm_action_response = self.incidents.get(incident_id)
        if 'remediation_actions' in rm_action_response.keys():
            remediation_actions = rm_action_response['remediation_actions'][0]
        else:
            remediation_actions = ''
        return remediation_actions

    def test_api(self):
        return self.get_incidents()
