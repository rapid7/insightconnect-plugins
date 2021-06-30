import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from icon_easyvista.util.api import EasyVistaApi
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        self.client = EasyVistaApi(params.get(Input.CLIENT_LOGIN), params.get(Input.ACCOUNT), params.get(Input.URL))

    def test(self):
        try:
            self.client.search_tickets("submit_date_ut:today")
        except PluginException:
            raise ConnectionTestException(
                cause="Connection error.",
                assistance="Please check that your username, password, account and hostname are correct.",
            )
        return {"status": "Success"}
