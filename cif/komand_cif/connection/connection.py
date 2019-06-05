import komand
from .schema import ConnectionSchema
# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.url = None
        self.verify = None
        self.api_token = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        self.api_token = params.get('api_key').get('secretKey')
        self.url = params.get('url')
        self.verify = params.get('ssl_verify', True)
        self.logger.info('URL: %s', self.url)

