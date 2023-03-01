import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
from icon_topdesk.util.api import TopDeskAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_client = None

    def connect(self, params: dict = None):
        self.logger.info("Connect: Connecting...")
        self.api_client = TopDeskAPI(
            credentials=params.get(Input.CREDENTIALS),
            domain=params.get(Input.DOMAIN),
            logger=self.logger,
        )

    def test(self):
        try:
            self.api_client.get_incidents()
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
        return {"status": "Success"}
