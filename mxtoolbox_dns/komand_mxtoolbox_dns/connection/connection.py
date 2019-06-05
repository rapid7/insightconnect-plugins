import komand
# Custom imports below
from .schema import ConnectionSchema


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting..")
        self.token = params.get("api_key").get("secretKey", "")
        self.server = params.get("url", "https://api.mxtoolbox.com/api/v1/")

        if self.token == "":
            self.logger.info("No key given, calls will be made unauthenticated")
