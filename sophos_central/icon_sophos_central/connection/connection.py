import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
# Custom imports below
from ..util.api import SophosCentralAPI
from insightconnect_plugin_runtime.exceptions import ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params=None):
        self.logger.info("Connect: Connecting...")
        self.client = SophosCentralAPI(
            params.get(Input.URL).rstrip("/"),
            params.get(Input.CLIENT_ID).get("secretKey"),
            params.get(Input.CLIENT_SECRET).get("secretKey"),
            params.get(Input.TENANT_ID, {}).get("secretKey"),
            self.logger
        )

    def test(self):
        try:
            return {
                "success": self.client.whoami(self.client.get_access_token())["id"] is not None
            }
        except Exception as e:
            raise ConnectionTestException(
                cause="Server error.",
                assistance="Please contact support for assistance",
                data=e
            )
