import komand
from .schema import ConnectionSchema, Input

# Custom imports below
from icon_rapid7_attackerkb.util.api import AttackerKB


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.attackerKB_api = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        self.attackerKB_api = AttackerKB(params.get(Input.CREDENTIALS).get("secretKey"),
                                         self.logger,
                                         params.get(Input.MAX_PAGES, 100))

    def test(self):
        self.attackerKB_api.call_api("api-docs/openapi_spec.json")
