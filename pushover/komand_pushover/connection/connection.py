import komand
from .schema import ConnectionSchema
# Custom imports below
from komand.exceptions import ConnectionTestException
import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        """
        Connection config params are supplied as a dict in
        params or also accessible in self.parameters['key']

        The following will setup the var to be accessed
          self.blah = self.parameters['blah']
        in the action and trigger files as:
          blah = self.connection.blah
        """
        # TODO: Implement connection or 'pass' if no connection is necessary
        self.logger.info("Connect: Connecting...")
        self.token = params.get('token').get('secretKey')
        self.api_url = "https://api.pushover.net/1/messages.json"

    def test(self):
        res = requests.get("https://api.pushover.net/1/apps/limits.json?token=" + self.token)
        if(res.status_code == 200):
            return True
        elif(res.status_code == 400):
            if(res.json().get('token','') == "invalid"):
                raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY)
            else:
                raise ConnectionTestException(preset=ConnectionTestException.Preset.UNKNOWN, data=res.text)
        return False
