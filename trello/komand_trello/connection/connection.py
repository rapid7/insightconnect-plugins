import komand
from .schema import ConnectionSchema
# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting..")
        version = params.get("version", "1")
        server = params.get("api_token").get("domain", "https://api.trello.com/")
        server += str(version)
        api_key = params.get("api_key").get("secretKey")
        token = params.get("api_token").get("token", "")

        if api_key is "":
            self.logger.info('Connect: Unauthenticated API will be used')

        self.server = server
        self.api_key = api_key
        self.token = token
