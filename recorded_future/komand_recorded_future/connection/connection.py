import komand
from .schema import ConnectionSchema
# Custom imports below
from rfapi import ApiV2Client
from komand_recorded_future.util import demo_test
import yaml


class Connection(komand.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None
        self.token = None

    def connect(self, params):
        self.token = params.get("api_key").get("secretKey")
        self.app_version = self.setup_custom_header()
        self.app_name = "rapid7_insightconnect"
        self.headers = {
            "User-Agent": f"{self.app_name}/{self.app_version}",
            "X-RFToken": self.token
        }

        self.client = ApiV2Client(auth=self.token, app_name=self.app_name, app_version=self.app_version)

    def test(self):
        return demo_test.demo_test(self.token, self.logger)

    def setup_custom_header(self):
        with open("../../plugin.spec.yaml") as f:
            spec = yaml.load(f)

        return spec.get("version")


