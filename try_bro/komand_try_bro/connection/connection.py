import komand
from .schema import ConnectionSchema
# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.server = None

    def connect(self, params):
        self.server = params.get('server', 'http://try.bro.org')
