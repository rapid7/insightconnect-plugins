import komand
from .schema import ConnectionSchema
# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.FEED_URL = None

    def connect(self, params):
        self.FEED_URL = params.get("url")
