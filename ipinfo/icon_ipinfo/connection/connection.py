import komand
from .schema import ConnectionSchema
# Custom imports below
import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")

        if params.get('credentials').get('token'):
            self.logger.info('API token provided')
            token = params.get('credentials').get('token')
        else:
            self.logger.info('API token not provided, unauthenticated requests will be attempted')
            token = ''

        if params.get('credentials').get('domain'):
            self.domain = params.get('credentials').get('domain')
        else:
            self.domain = 'http://ipinfo.io/'

        self.token = token

    def test(self):
        if self.token:
            url = f"{self.domain}8.8.8.8/json?token={self.token}"
        else:
            url = f"{self.domain}8.8.8.8/json"

        request = requests.get(url)
        dic = request.json()
        return dic
