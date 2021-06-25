import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below

from komand_elasticsearch.util.api import ElasticSearchAPI
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params={}):
        use_authentication = params.get(Input.USE_AUTHENTICATION)
        if use_authentication:
            self.logger.info("Connect: Connecting..")
            self.client = ElasticSearchAPI(
                params.get(Input.URL),
                self.logger,
                params.get(Input.CREDENTIALS).get("username"),
                params.get(Input.CREDENTIALS).get("password"),
            )
        else:
            self.logger.info("Connect: Warning, No Auth Provided")
            self.client = ElasticSearchAPI(params.get(Input.URL), self.logger)

    def test(self):
        try:
            return {"success": self.client.test_auth()}
        except PluginException as e:
            raise ConnectionTestException(cause=e.cause, assistance=e.assistance, data=e.data)
