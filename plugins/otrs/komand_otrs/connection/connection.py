import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from typing import Any

# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from komand_otrs.util.api import OTRSAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self) -> None:
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params: dict[str, Any] = {}) -> None:
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        server = params.get(Input.SERVER, "").strip()
        username = params.get(Input.CREDENTIALS, {}).get("username", "").strip()
        password = params.get(Input.CREDENTIALS, {}).get("password", "")
        # END INPUT BINDING - DO NOT REMOVE

        self.logger.info("Connect: Connecting...")
        self.client = OTRSAPI(server, username, password, self.logger)

    def test(self) -> dict[str, bool]:
        try:
            self.client.test_connection()
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
