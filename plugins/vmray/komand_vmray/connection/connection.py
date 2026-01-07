import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
from .schema import ConnectionSchema, Input

# Custom imports below
from ..util.api import VMRay


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api = None

    def connect(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        api_key = params.get(Input.API_KEY, {}).get("secretKey", "").strip()
        url = params.get(Input.URL, "").strip()
        # END INPUT BINDING - DO NOT REMOVE

        self.logger.info("Connect: Connecting...")
        self.api = VMRay(url=url, api_key=api_key, logger=self.logger)

    def test(self):
        try:
            self.api.test_call()
            return {"success": True}
        except PluginException as exception:
            raise ConnectionTestException(cause=exception.cause, assistance=exception.assistance, data=exception.data)
