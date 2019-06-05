from .schema import ConnectionSchema
import komand
# Custom imports below
from urllib.parse import urlparse


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def base_url(self):
        parsed_uri = urlparse(self.server)
        return '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)

    def connect(self, params={}):
        self.server = params.get('server')
        self.api_key = params.get('api_key').get('secretKey')
        self.secret = params.get('api_secret').get('secretKey')

        if not self.server.endswith('/api') and not self.server.endswith('/api/'):
            self.server += '/api'
