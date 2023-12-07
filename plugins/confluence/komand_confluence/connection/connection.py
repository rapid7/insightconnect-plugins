import insightconnect_plugin_runtime
from .schema import ConnectionSchema

# Custom imports below
from ..util.api import API


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        """
        Connect to Confluence
        """
        self.logger.info("Connecting to Confluence: %s", params.get("url"))
        self.client = API(
            url=params.get("url"),
            username=params.get("credentials").get("username"),
            password=params.get("credentials").get("password"),
            cloud=True
        )
