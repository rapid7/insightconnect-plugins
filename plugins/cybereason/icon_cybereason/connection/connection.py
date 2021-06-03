import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from icon_cybereason.util.api import CybereasonAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        self.api = CybereasonAPI(
            hostname=params.get(Input.HOSTNAME),
            port=params.get(Input.PORT),
            username=params.get(Input.CREDENTIALS).get("username"),
            password=params.get(Input.CREDENTIALS).get("password"),
            logger=self.logger,
        )
        self.api.connect()

    def test(self):
        return {"connection": "success"}
