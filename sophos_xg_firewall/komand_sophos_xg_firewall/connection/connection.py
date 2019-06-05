import komand
from .schema import ConnectionSchema
# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.host = None
        self.port = None
        self.username = None
        self.password = None

    def connect(self, params):
        self.host = params["host"]
        self.port = params["port"]
        self.username = params.get('credentials').get('username')
        self.password = params.get('credentials').get('password')

