from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException

import insightconnect_plugin_runtime
from icon_hybrid_analysis.util import constans

# Custom imports below
from .schema import ConnectionSchema, Input
from ..util.api import HybridAnalysisAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        self.api = HybridAnalysisAPI(
            url=params.get(Input.URL, constans.DEFAULT_URL),
            api_key=params.get(Input.API_KEY).get("secretKey"),
            logger=self.logger,
        )

    def test(self):
        """Test action"""
        self.logger.info("Test Connection")
        try:
            self.api.lookup_by_hash("040c0111aef474d8b7bfa9a7caa0e06b4f1049c7ae8c66611a53fc2599f0b90f")
        except PluginException as e:
            raise ConnectionTestException(cause=e.cause, assistance=e.assistance, data=e)
        return {}
