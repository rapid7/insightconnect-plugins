import komand
from .schema import ConnectionSchema
# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.key = ''
        self.secret = ''
        self.base = 'http://api.screenshotmachine.com/'

    def connect(self, params):
        """
        Connect to screenshot machine
        """
        self.key = params.get("key").get("secretKey")
        self.secret = params.get("secret").get("secretKey")
