import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

from .schema import ConnectionSchema, Input

# Custom imports below
from komand_confluence.util.api import ConfluenceAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params={}):
        """
        Connect to Confluence
        """
        self.logger.info("Connecting to Confluence: %s", params.get("url"))
        self.client = ConfluenceAPI(
            url=params.get(Input.URL, ""),
            username=params.get(Input.USERNAME, ""),
            api_token=params.get(Input.API_TOKEN, {}).get("secretKey"),
            cloud=params.get(Input.CLOUD, True),
        )

    def test(self):
        try:
            self.client.test()
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
