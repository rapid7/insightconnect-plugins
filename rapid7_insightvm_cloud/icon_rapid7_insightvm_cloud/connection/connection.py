import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
# Custom imports below
from icon_rapid7_insightvm_cloud.util.api import IVM_Cloud


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.ivm_cloud_api = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        self.ivm_cloud_api = IVM_Cloud(
            params.get(Input.CREDENTIALS).get("secretKey"),
            self.logger,
            params.get(Input.MAX_PAGES, 100),
            params.get(Input.REGION)
        )

    def test(self):
        self.ivm_cloud_api.call_api("scan")
