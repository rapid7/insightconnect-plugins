import komand
from .schema import ConnectionSchema, Input
# Custom imports below
from OTXv2 import OTXv2


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params):
        api_key, otx_server = params.get(Input.API_KEY).get("secretKey", None), params.get(Input.URL)
        try:
            self.client = OTXv2(api_key, server=otx_server)
        except Exception as e:
            raise Exception(f"An error has occurred while connecting: {e}")

    def test(self):
        try:
            self.client.search_users("")
        except Exception as e:
            raise Exception(f"Unable to connect, error: {e}")