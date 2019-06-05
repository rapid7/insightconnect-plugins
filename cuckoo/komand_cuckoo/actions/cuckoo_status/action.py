import komand
from .schema import CuckooStatusInput, CuckooStatusOutput
# Custom imports below
import json
import requests


class CuckooStatus(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='cuckoo_status',
                description='Returns status of the cuckoo server',
                input=CuckooStatusInput(),
                output=CuckooStatusOutput())

    def run(self, params={}):
        server = self.connection.server
        endpoint = server + "/cuckoo/status"
        
        try:
            r = requests.get(endpoint)
            r.raise_for_status()
            response = r.json()
            return response
        
        except Exception as e:
            self.logger.error("Error: " + str(e))

    def test(self):
        return self.connection.test()