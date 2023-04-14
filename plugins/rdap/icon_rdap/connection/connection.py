import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

from icon_rdap.util.api import RdapAPI

from .schema import ConnectionSchema


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.rdap_client = None

    def connect(self, params):
        # pylint: disable=unused-argument
        self.rdap_client = RdapAPI(self.logger)

    def test(self):
        try:
            self.rdap_client.domain_lookup("example.com")
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
