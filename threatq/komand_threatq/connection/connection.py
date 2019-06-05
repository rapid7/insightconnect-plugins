import komand
from .schema import ConnectionSchema
# Custom imports below
from threatqsdk import Threatq
import os
import requests
import json


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.threatq = None


    def connect(self, params={}):
        """ Connect will create a ThreatQ object to use in the plugin"""
        self.logger.info('Connect: Connecting..')

        self.host = params['host']
        self.clientid = params['client_id']['secretKey']
        self.email = params['credentials']['username']
        self.password = params['credentials']['password']
        self.proxy = params['proxy']

        threatq = Threatq(threatq_host=self.host,
                          auth={
                              'clientid': self.clientid,
                              'auth': {
                                  'email': self.email,
                                  'password': self.password,
                              },
                          },
                          proxy=self.proxy)

        self.threatq = threatq

    def manual_connection_test(self, params):
        if self.proxy:
            os.environ['http_proxy'] = params['proxy']
            os.environ['https_proxy'] = params['proxy']

        auth_url = self.host + "/api/token"
        auth_body = {
            "email": self.email,
            "password": self.password,
            "grant_type": "password",
            "client_id": self.clientid
        }
        auth_headers = { "content-type": "application/json" }

        auth_response = requests.post(auth_url, data=json.dumps(auth_body), headers=auth_headers, verify=False)
        auth_response_dict = json.loads(auth_response.text)
        auth_token = auth_response_dict['access_token']

        if auth_token:
            return True
        else:
            return False
