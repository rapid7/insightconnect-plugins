import insightconnect_plugin_runtime

from .schema import ConnectionSchema, Input

# Custom imports below
from icon_sqlmap.util.api import SqlmapApi
from icon_sqlmap.util.constants import DEFAULT_API_HOST, DEFAULT_API_PORT


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_host = None
        self.api_port = None
        self.sqlmap_client = None

    def connect(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        self.api_host = params.get(Input.API_HOST, "").strip() or DEFAULT_API_HOST
        self.api_port = params.get(Input.API_PORT, "").strip() or DEFAULT_API_PORT
        # END INPUT BINDING - DO NOT REMOVE

        self.logger.info("Connect: Connecting...")
        self.sqlmap_client = SqlmapApi(self.api_host, self.api_port, self.logger)

    def test(self) -> dict[str, bool]:
        return {"success": True}
