import komand
from .schema import ConnectionSchema
# Custom imports below
from ..api import *


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")

        key = params.get("api_key").get("secretKey")
        if not key:
            self.logger.error("Connection: connect: Empty key")
            raise Exception("Connection: connect: Empty key")

        key = key.lower()
        p = re.compile('[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}')
        m = p.match(key)
        if not m:
            self.logger.error("Connection: connect: Wrong key")
            raise Exception("Connection: connect: Wrong key")

        self.api = Cisco_Api(key)
        self.testConnection()

    def testConnection(self):
        try:
            self.api.get_domains()
        except Exception:
            self.logger.error("Connection: connect: Wrong key")
            raise Exception("Connection: connect: Wrong key")
