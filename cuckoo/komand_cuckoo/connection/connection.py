import komand
from .schema import ConnectionSchema
# Custom imports below
import json
import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting..")
        server = params.get('url')
        self.server = server

    def test(self):
        server = self.server
        endpoint = server + "/cuckoo/status"
        try:
            r = requests.get(endpoint)
            r.raise_for_status()
            response = r.json()
            return response
        except Exception as e:
            self.logger.error("Error: " + str(e))
