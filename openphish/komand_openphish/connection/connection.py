import komand
from .schema import ConnectionSchema, Input
# Custom imports below
import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.url = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        self.url = params.get('url')

    def test(self):
        response = requests.get(self.url)
        if 200 <= response.status_code < 400:
            return {'Connection test successful': True}

        return {'Connection test successful': False}
