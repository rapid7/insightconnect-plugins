import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

from .schema import ConnectionSchema, Input

# Custom imports below
from ..util.api import CyberGrcAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        self.api_key = params.get(Input.API_KEY)
        self.ssl_verify = params.get(Input.SSL_VERIFY)
        self.url = params.get(Input.URL)
        # END INPUT BINDING - DO NOT REMOVE

        self.client = CyberGrcAPI(
            url=self.url,
            api_key=self.api_key.get("secretKey"),
            ssl_verify=self.ssl_verify,
            logger=self.logger,
        )

    def test(self):
        # Statuses is a small read-only lookup collection, so this confirms the URL and
        # API key without depending on any particular GRC data being present.
        try:
            self.client.count_records("Statuses")
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
        return {"success": True}
