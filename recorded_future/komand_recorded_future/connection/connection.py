import komand
from .schema import ConnectionSchema
from rfapi import ApiV2Client
# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None


    def connect(self, params):
            self.token = params.get("api_key").get("secretKey")
            self.client = ApiV2Client(auth=self.token)
