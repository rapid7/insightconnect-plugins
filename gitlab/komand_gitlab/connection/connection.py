import komand
from .schema import ConnectionSchema
# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.token = None
        self.username = None
        self.url = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")
        self.token    = params.get('credentials').get('password')
        self.username = params.get('credentials').get('username')
        self.url = params.get('url') + '/api/v4'
