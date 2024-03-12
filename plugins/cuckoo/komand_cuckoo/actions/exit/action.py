import insightconnect_plugin_runtime
from .schema import ExitInput, ExitOutput

# Custom imports below
import json
import requests


class Exit(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="exit",
            description="Shuts down the server if in debug mode and using the werkzeug server",
            input=ExitInput(),
            output=ExitOutput(),
        )

    def run(self, params={}):
        server = self.connection.server
        endpoint = f"{server}/exit"

        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            response = response.json()
            return response

        except Exception as exception:
            self.logger.error("Error: " + str(exception))
