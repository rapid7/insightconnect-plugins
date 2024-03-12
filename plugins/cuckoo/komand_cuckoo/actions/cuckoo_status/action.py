import insightconnect_plugin_runtime
from .schema import CuckooStatusInput, CuckooStatusOutput

# Custom imports below
import json
import requests


class CuckooStatus(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="cuckoo_status",
            description="Returns status of the cuckoo server",
            input=CuckooStatusInput(),
            output=CuckooStatusOutput(),
        )

    def run(self, params={}):
        server = self.connection.server
        endpoint = f"{server}/cuckoo/status"

        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            response = response.json()
            return response

        except Exception as exception:
            self.logger.error(f"Error: {str(exception)}")
