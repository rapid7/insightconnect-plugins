import komand
from .schema import ConnectionSchema, Input
from komand.exceptions import ConnectionTestException
# Custom imports below
import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        api_key = params.get(Input.API_KEY).get("secretKey")
        self.url = params.get(Input.URL)
        if not self.url.endswith('/'):
            self.url = f'{self.url}/'

        self.session = requests.session()
        self.session.headers.update({'X-Api-Key': api_key})

        self.logger.info("Connect: Connecting...")

    def test(self):
        response = self.session.get(f'{self.url}validate')
        if response.status_code == 401:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.UNAUTHORIZED)
        elif response.status_code in range(500, 599):
            raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE)
        elif response.status_code == 200:
            return response.json()
        else:
            self.logger.error(response.text)
            raise ConnectionTestException(cause=f'An unknown error occurred.'
                                                f' InsightIDR responded with a {response.status_code} code.',
                                          assistance=f' See log for more details. If the problem persists, please contact support.')
