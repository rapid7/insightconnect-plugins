import komand
from .schema import ConnectionSchema
# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        self.logger.info("Connecting")
        server = 'https://www.cloudshark.org'
        token  = params.get('api_key').get('secretKey')

        if not token:
            self.logger.error('Cloudshark API token not supplied')
            raise Exception('Cloudshark API token not supplied')

        base   = server + '/api/v1/'

        self.server = server
        self.base   = base
        self.token  = token
