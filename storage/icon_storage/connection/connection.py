import komand
from .schema import ConnectionSchema
# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    # No connection for this plugin
    def connect(self, params):
        pass

    def test(self):
        pass
