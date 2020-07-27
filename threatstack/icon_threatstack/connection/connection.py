import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
# Custom imports below
from threatstack import ThreatStack


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params):
        api_key = params.get(Input.API_KEY)["secretKey"]
        user_id = params.get(Input.USER_ID)
        org_id = params.get(Input.ORG_ID)
        timeout = params.get(Input.TIMEOUT, 120)

        self.client = ThreatStack(api_key=api_key,
                                  user_id=user_id,
                                  org_id=org_id,
                                  api_version=2,
                                  timeout=timeout)

    def test(self):
        # TODO: Implement test
        pass