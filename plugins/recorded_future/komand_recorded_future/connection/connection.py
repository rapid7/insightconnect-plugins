import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from komand_recorded_future.util.api import RecordedFutureApi
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from komand_recorded_future.util.api import Endpoint


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None
        self.token = None

    def connect(self, params={}):
        self.token = params.get(Input.API_KEY).get("secretKey")
        self.client = RecordedFutureApi(self.logger, self.meta, self.token)

    def test(self):
        try:
            self.client.make_request(Endpoint.list_hash_risk_rules())
        except PluginException:
            raise ConnectionTestException(
                cause="Connection error.", assistance="Please check that your API key is correct."
            )
        return {"status": "Success"}
