import komand
from .schema import ConnectionSchema, Input
# Custom imports below
from threatstack import ThreatStack


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params):
        api_key = params.get(Input.API_KEY)["secretKey"]
        org_id = params.get(Input.ORG_ID)  # Optional
        api_version = params.get(Input.API_VERSION, 1)
        timeout = params.get(Input.TIMEOUT, 120)

        self.client = ThreatStack(api_key=api_key,
                                  org_id=org_id,
                                  api_version=api_version,
                                  timeout=timeout)

    def test(self):
        pass