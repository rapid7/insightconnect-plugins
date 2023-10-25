import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from komand_sentinelone.util.api import SentineloneAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        self.client = SentineloneAPI(
            f"https://{params.get(Input.INSTANCE)}.sentinelone.net",
            params.get(Input.APIKEY, {}).get("secretKey"),
            params.get(Input.USERTYPE),
            self.logger,
        )

    def test(self):
        try:
            self.client.get_activity_types()
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
