import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from icon_cylance_protect.util.api import CylanceProtectAPI
# Custom imports below


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        self.client = CylanceProtectAPI(
            self.logger,
            params.get(Input.URL),
            params.get(Input.TENANT_ID).get("secretKey"),
            params.get(Input.APPLICATION_ID).get("secretKey"),
            params.get(Input.APPLICATION_SECRET).get("secretKey")
        )

    def test(self):
        token = self.client.generate_token("device:read")
        if token is not None and len(token) > 0:
            return True

        return False
