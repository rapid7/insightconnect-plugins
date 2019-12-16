import komand
from .schema import ConnectionSchema


# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")
        version = params.get("version", "v2")
        server = params.get("host", "https://hipchat.com/")
        server += version

        user = params.get("credentials").get("username", "")
        token = params.get("credentials").get("password", "")

        if token == "":
            self.logger.info('Connect: Unauthenticated API will be used')

        self.server = server
        self.token = token
        self.user = user
