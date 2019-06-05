import komand
from .schema import SearchInput, SearchOutput
# Custom imports below
import json
import requests
import os


class Search(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='search',
                description='Search all data',
                input=SearchInput(),
                output=SearchOutput())

    def run(self, params={}):
        """TODO: Run action"""
        if self.connection.proxy:
            os.environ['http_proxy'] = params['proxy']
            os.environ['https_proxy'] = params['proxy']

        auth_url = self.connection.host + "/api/token"
        auth_body = {
            "email": self.connection.email,
            "password": self.connection.password,
            "grant_type": "password",
            "client_id": self.connection.clientid
        }
        auth_headers = { "content-type": "application/json" }

        try:
            auth_response = requests.post(auth_url, data=json.dumps(auth_body), headers=auth_headers, verify=False)
            auth_response_dict = json.loads(auth_response.text)
            auth_token = auth_response_dict['access_token']

            search_params = { 'limit': params['limit'], 'query': params['query'] }
            search_url = self.connection.host + "/api/search"
            search_headers = { 'authorization': "Bearer " + auth_token }

            try:
                search_results = requests.get(search_url, headers=search_headers, params=search_params, verify=False)
                results_list = json.loads(search_results.text)['data']
                return { 'results': results_list }

            except BaseException as e:
                self.logger.error("Could not run search. Error: " + str(e))

        except BaseException as e:
            self.logger.error("Could not authenticate with ThreatQ. Error " + str(e))


    def test(self):
        """TODO: Test action"""
        if self.connection.manual_connection_test:
            return { 'results': [
                {
                    'id': 0,
                    'object': 'Connection test result',
                    'value': 'Authorization token received'
                }
            ]}
