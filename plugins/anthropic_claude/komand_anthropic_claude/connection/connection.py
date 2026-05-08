import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

from .schema import ConnectionSchema, Input
from komand_anthropic_claude.util.api import AnthropicAPI


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        api_key = params.get(Input.API_KEY, {}).get("secretKey", "").strip()
        model = params.get(Input.MODEL)
        # END INPUT BINDING - DO NOT REMOVE

        self.client = AnthropicAPI(
            api_key=api_key,
            model=model,
            logger=self.logger,
        )

    def test(self):
        try:
            self.client.test_connection()
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
        return {"success": True}
