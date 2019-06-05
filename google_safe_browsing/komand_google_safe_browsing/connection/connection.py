import komand
from .schema import ConnectionSchema
# Custom imports below


class Connection(komand.Connection):

    API_KEY = None

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.API_KEY = params.get("credentials").get("secretKey")