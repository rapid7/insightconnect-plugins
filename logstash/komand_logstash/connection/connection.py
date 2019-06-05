import komand
from .schema import ConnectionSchema
# Custom imports below
import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.url = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")
        url = params.get('url')
        try:
            r = requests.head(url)
            if r.status_code != 200:
                self.logger.error('Logstash: Connect: error %s', params)
        except requests.ConnectionError:
            self.logger.error('Logstash: Connect: error %s', params)
            raise Exception('Logstash: Connect: connection failed')

        self.url = url
