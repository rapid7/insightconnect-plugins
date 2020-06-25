import insightconnect_plugin_runtime
# Custom imports below
from .schema import ConnectionSchema, Input
from ..util.api import McAfeeATDAPI
from ..util.mcafee_request import McAfeeRequest


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.authentication_header = None
        self.mcafee_atd_api = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        credentials = params.get(Input.CREDENTIALS)

        self.mcafee_atd_api = McAfeeATDAPI(
            McAfeeRequest(
                params.get(Input.URL).rstrip('/'),
                params.get(Input.PORT, 443),
                params.get(Input.VERIFY_SSL, True),
                self.logger
            ),
            credentials.get('username'),
            credentials.get('password'),
            self.logger
        )

    def test(self):
        return {
            "success": self.mcafee_atd_api.get_login_headers().get("VE-SDK-API") is not None
        }
