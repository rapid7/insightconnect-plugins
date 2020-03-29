import komand
from .schema import ConnectionSchema
# Custom imports below
import requests
from komand.exceptions import ConnectionTestException


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        pass

    def test(self):
        url = 'https://www.craigslist.org/about/'
        try:
            resp = requests.get(url)
            resp.raise_for_status()
        except Exception as e:
            self.logger.error(f'Failed to retrieve test url: {url}')
            raise ConnectionTestException(cause="Problem with connect to server", data=e)

        self.logger.info(f'Successful request to {url}')
        return {'success': 'https://www.craigslist.org/about/'}
