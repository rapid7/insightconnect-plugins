import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import (
    ConnectionTestException,
    PluginException,
)

# Custom imports below
from icon_luminar.util.api import LuminarManager

from .schema import ConnectionSchema, Input


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        self.base_url = params.get(Input.BASE_URL)
        self.account_id = params.get(Input.ACCOUNT_ID)
        self.client_id = params.get(Input.CLIENT_ID)
        self.client_secret = params.get(Input.CLIENT_SECRET, {}).get("secretKey")
        # END INPUT BINDING - DO NOT REMOVE
        self.client = LuminarManager(
            cognyte_client_id=self.client_id,
            cognyte_client_secret=self.client_secret,
            cognyte_account_id=self.account_id,
            cognyte_base_url=self.base_url,
            logger=self.logger,
        )

    def test(self):
        try:
            return {"success": self.client.access_token() != None}
        except PluginException as error:
            raise ConnectionTestException(
                cause=error.cause, assistance=error.assistance, data=error.data
            )
