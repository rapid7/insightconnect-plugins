import komand
import dumbno
from .schema import ConnectionSchema
# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        self.host   = params.get('host')
        self.port   = params.get('port', 9000)
        self.dumbno = dumbno.ACLClient(self.host, port=self.port)
