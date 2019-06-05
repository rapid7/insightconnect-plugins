import komand
from .schema import ConnectionSchema
# Custom imports below
from ..util.api import VMRay


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api = None

    def connect(self, params):
        _api_key = params.get("api_key").get("secretKey")
        self.logger.info("Connect: Connecting...")
        self.api = VMRay(
            url=params.get("url"),
            api_key=_api_key,
            logger=self.logger
        )

    def test(self):
        self.api.test_call()