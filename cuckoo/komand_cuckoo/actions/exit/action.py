import komand
from .schema import ExitInput, ExitOutput
# Custom imports below
import json
import requests


class Exit(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='exit',
                description='Shuts down the server if in debug mode and using the werkzeug server',
                input=ExitInput(),
                output=ExitOutput())

    def run(self, params={}):
        server = self.connection.server
        endpoint = server + "/exit"
        
        try:
            r = requests.get(endpoint)
            r.raise_for_status()
            response = r.json()
            return response
        
        except Exception as e:
            self.logger.error("Error: " + str(e))

    def test(self):
        out = self.connection.test()
        out['message'] = 'Test passed'
        return out