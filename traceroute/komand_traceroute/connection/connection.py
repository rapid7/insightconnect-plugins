import komand
# Custom imports below
from .schema import ConnectionSchema


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        pass
