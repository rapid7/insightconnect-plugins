import komand
from .schema import ConnectionSchema
# Custom imports below
from urllib.parse import urljoin
from pycrits import pycrits, pycritsFetchError


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.crits = None

    def connect(self, params):
        url = params['url']
        user = params['username']
        key = params.get('api_key').get('secretKey')
        verify_ssl = params['ssl_verify']
        self.crits = pycrits(url, user, key, verify=verify_ssl)

        try:
            url = urljoin(url, '/api/v1')
            self.crits._do_fetch(url)

        except pycritsFetchError as e:
            self.logger.error('CRITs: Connect: error {}', str(e))
            raise Exception('CRITs: Connect: connection failed')
