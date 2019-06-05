import komand
from .schema import GetEventInput, GetEventOutput
# Custom imports below
import json
import requests
import os


class GetEvent(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_event',
                description='Retrieve detailed information associated with a given event',
                input=GetEventInput(),
                output=GetEventOutput())

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

            with_param_list = ",".join(params.get("with"))
            get_params = { 'with': with_param_list }
            get_url = self.connection.host + "/api/events/" + str(params.get("id"))
            get_headers = { 'authorization': "Bearer " + auth_token }

            try:
                get_results = requests.get(get_url, headers=get_headers, params=get_params, verify=False)
                results = json.loads(get_results.text)
                return results

            except BaseException as e:
                self.logger.error("Could not retrieve event. Error: " + str(e))

        except BaseException as e:
            self.logger.error("Could not authenticate with ThreatQ. Error " + str(e))

    def test(self):
        """TODO: Test action"""
        if self.connection.manual_connection_test:
            return {
                "data": {
                    "message": "Connection succeeded"
                }
            }
