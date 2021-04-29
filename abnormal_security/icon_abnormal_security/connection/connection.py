import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from icon_abnormal_security.util.api import AbnormalSecurityAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        self.logger.info(params.get(Input.API_KEY).get("secretKey"))
        self.api = AbnormalSecurityAPI(
            hostname=params.get(Input.HOSTNAME),
            api_key=params.get(Input.API_KEY).get("secretKey"),
            logger=self.logger,
        )
        self.api.connect()

    def test(self):
        return {"connection": "success"}
