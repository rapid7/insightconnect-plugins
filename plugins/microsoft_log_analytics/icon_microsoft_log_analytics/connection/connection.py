from typing import Dict

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

# Custom imports below
from ..util.api import AzureLogAnalyticsClientAPI
from .schema import ConnectionSchema, Input


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        # START INPUT BINDING - DO NOT REMOVE
        client_id = params.get(Input.CLIENT_ID)
        client_secret = params.get(Input.CLIENT_SECRET, {}).get("secretKey")
        tenant_id = params.get(Input.TENANT_ID)
        # END INPUT BINDING - DO NOT REMOVE

        self.logger.info("Connect: Connecting...")
        self.client = AzureLogAnalyticsClientAPI(client_id, client_secret, tenant_id, self.logger)

    def test(self) -> Dict[str, bool]:
        try:
            self.client.test_connection()
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
