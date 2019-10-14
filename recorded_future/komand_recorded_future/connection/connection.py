import komand
from .schema import ConnectionSchema

# Custom imports below
from rfapi import ApiV2Client
from komand_recorded_future.util import demo_test


class Connection(komand.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None
        self.token = None

    def connect(self, params):
        self.token = params.get("api_key").get("secretKey")
        self.client = ApiV2Client(auth=self.token)

    def test(self):
        return demo_test.demo_test(self.token, self.logger)
