import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from komand_proofpoint_tap.util.api import ProofpointTapApi
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params={}):
        if params.get(Input.SERVICE_PRINCIPAL) and params.get(Input.SECRET):
            self.logger.info("Connect: Connecting...")
            self.client = ProofpointTapApi(params.get(Input.SERVICE_PRINCIPAL), params.get(Input.SECRET))
        else:
            pass

    def test(self):
        try:
            self.client.get_top_clickers({"window": 14})
        except AttributeError:
            raise PluginException(
                cause="Connection configuration required.", assistance="Please set up your connection and try again."
            )
        except PluginException:
            raise ConnectionTestException(
                cause="Connection error.",
                assistance="Please check that your service principal and secret are correct.",
            )
        return {"status": "Success"}
