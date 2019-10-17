import komand
from .schema import ConnectionSchema
# Custom imports below
from komand.exceptions import ConnectionTestException
import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        self.token = params.get('api_key').get('secretKey')
        self.server = params.get('server', 'https://api.echotrail.io:443')

    def test(self):
        url = self.server + '/v1/private/insights/cmd.exe/rank'
        headers = {'X-Api-Key': self.token}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return { "success": True }
        elif response.status_code == 403:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY)
        elif response.status_code == 404:
            raise ConnectionTestException(cause="Unable to reach instance at: %s." % url,
                                          assistance="Verify the server at the URL configured in your plugin "
                                                     "connection is correct.")
        elif response.status_code == 429:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.RATE_LIMIT)
        elif response.status_code == 503:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVER_ERROR)
        else:
            raise ConnectionTestException(cause="Unhandled error occurred: %s" % response.content)
