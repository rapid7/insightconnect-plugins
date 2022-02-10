import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import (
    PluginException,
    ConnectionTestException,
)
from .schema import ConnectionSchema, Input

from ..util.api import CiscoUmbrellaManagementAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        # Gather input variables
        pubKey = params.get(Input.API_KEY).get("secretKey")
        priKey = params.get(Input.API_SECRET).get("secretKey")
        orgID = params.get(Input.ORGANIZATION_ID)

        # Main client function with input variables
        self.client = CiscoUmbrellaManagementAPI(api_key=pubKey, api_secret=priKey, organization_id=orgID)

    def test(self):
        try:
            self.client.get_destination_lists()
            return {"success": True}
        except PluginException as e:
            raise ConnectionTestException(cause=e.cause, assistance=e.assistance, data=e.data)
