import komand
from .schema import ConnectionSchema
# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.api_key = params.get('credentials').get('secretKey')
        self.base = 'https://www.abuseipdb.com'

        self.logger.info('Connect: Connecting to %s...' % self.base)
