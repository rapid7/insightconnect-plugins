import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException

# Custom imports below
from icon_abnormal_security.util.api import AbnormalSecurityAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        self.api = AbnormalSecurityAPI(
            url=params.get(Input.URL),
            api_key=params.get(Input.API_KEY).get("secretKey"),
            logger=self.logger,
        )

    def test(self):
        try:
            self.api.test_api()
        except PluginException:
            raise ConnectionTestException(
                cause="Connection Test Failed.", assistance="Please check that your API key is correct."
            )
        return {}
