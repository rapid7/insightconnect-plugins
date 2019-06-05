import komand
from .schema import ConnectionSchema
# Custom imports below
from ..investigate import *


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")
        key = params.get('api_key').get('secretKey')
        pattern = re.compile("^[A-Za-z0-9]{8}-[A-Za-z0-9]{4}-[A-Za-z0-9]{4}-[A-Za-z0-9]{4}-[A-Za-z0-9]{12}$")

        if pattern.match(key):
            self.investigate = investigate.Investigate(key)
        else:
            self.logger.error("Connection: connect: Wrong api_key format. Should be: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")
            raise Exception("Connection: connect: Wrong api_key format. Should be: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")

        self.testConnection()

    def testConnection(self):
        try:
            self.investigate.categorization([])
        except Exception:
            self.logger.error("Connection: connect: Wrong api_key")
            raise Exception("Connection: connect: Wrong api_key")
