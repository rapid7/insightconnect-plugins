import komand
from .schema import ConnectionSchema, Input
from komand.exceptions import ConnectionTestException
# Custom imports below
import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
            self.logger.info("Connect: Connecting..")
            self.host = params.get(Input.URL)
            self.token = params.get(Input.API_KEY).get('secretKey')
            self.connector = params.get(Input.CONNECTOR)

    def test(self):
        host = self.host
        token = self.token
        connector = self.connector
        devices = '/integrationServices/v3/device'
        headers = {'X-Auth-Token': f'{token}/{connector}'}
        url = host + devices

        result = requests.get(url, headers=headers)
        if result.status_code == 200:
            return {'success': True}
        if result.status_code == 401:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY)
        raise ConnectionTestException(f'An unknown error occurred. Response code was: {result.status_code}'
                                      f' If the problem persists please contact support for help. Response was: {result.text}')
