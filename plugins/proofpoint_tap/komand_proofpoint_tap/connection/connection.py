import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from komand_proofpoint_tap.util.api import ProofpointTapApi
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None
        self.is_authorized = False

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        self.client = ProofpointTapApi(
            params.get(Input.SERVICEPRINCIPAL, {}), params.get(Input.SECRET, {}), self.logger
        )

    def test(self):
        if self.client.authorized:
            try:
                self.client.get_top_clickers({"window": 14})
            except PluginException:
                raise ConnectionTestException(
                    cause="Connection error.",
                    assistance="Please check that your service principal and secret are correct.",
                )
        return {"status": "Success"}
