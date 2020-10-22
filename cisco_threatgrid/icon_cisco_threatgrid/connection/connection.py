import komand
from .schema import ConnectionSchema, Input

# Custom imports below
from icon_cisco_threatgrid.util.api import ThreatGrid


class Connection(komand.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api = None
        self.base_url = None

    def connect(self, params):

        input_region = params.get(Input.REGION)
        if input_region == "Europe":
            self.base_url = "https://panacea.threatgrid.eu"
        else:
            self.base_url = "https://panacea.threatgrid.com"

        ssl_verify = params.get(Input.SSL_VERIFY, False)
        self.api: ThreatGrid = ThreatGrid(
            api_key=params.get(Input.API_KEY).get("secretKey"),
            base_url=self.base_url,
            logger=self.logger,
            ssl_verify=ssl_verify
        )

    def test(self):
        _ = self.api.test_api()
        return {}
