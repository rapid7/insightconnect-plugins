import insightconnect_plugin_runtime
from .schema import ConnectionSchema

# Custom imports below
from ..util.api import ConfluenceAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        """
        Connect to Confluence
        """
        self.logger.info("Connecting to Confluence: %s", params.get("url"))
        self.client = ConfluenceAPI(
            url=params.get("url"),
            username=params.get("username"),
            api_token=params.get("api_token").get("secretKey"),
            cloud=params.get("cloud")
        )
        self.client.login()

    def test(self):
        self.client.health_check()
        return {"success": True}
