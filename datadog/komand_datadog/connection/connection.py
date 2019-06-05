import komand
from .schema import ConnectionSchema, Input
from komand.exceptions import ConnectionTestException
# Custom imports below
import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        api_key = params.get(Input.API_KEY).get('secretKey')
        app_key = params.get(Input.APP_KEY)
        self.url = params.get(Input.URL)

        self.auth = {
            'api_key': api_key,
            'application_key': app_key
        }
        self.session = requests.Session()

        self.logger.info("Connect: Connecting...")

    def test(self):
        result = self.session.get(url=f'{self.url}validate', params=self.auth)
        if result.status_code == 200:
            return result.json()
        elif result.status_code == 403:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.USERNAME_PASSWORD)
        else:
            raise ConnectionTestException(cause=f'Unknown connection error: Status code {result.status_code}.'
                                                f' Error message {result.text}',
                                          assistance='Contact support for help')
