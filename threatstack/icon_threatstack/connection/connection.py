import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
# Custom imports below
from threatstack import ThreatStack
from threatstack.errors import ThreatStackAPIError, ThreatStackClientError, APIRateLimitError
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
import datetime


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
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        try:
            response = self.client.http_request(method="get", path="agents", params={"from": now, "until": now})
            self.logger.info(f"RESPONSE IS: {response}")
        except (ThreatStackAPIError, ThreatStackClientError, APIRateLimitError) as e:
            raise ConnectionTestException(cause="An error occurred!",
                                          assistance=e)

        return {"success": True}
