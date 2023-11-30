import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from requests import Session
from icon_rapid7_insightvm_cloud.util.api import IVM_Cloud


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.ivm_cloud_api = None
        self.api_url = None
        self.session = None
        self.region = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        self.region = params.get(Input.REGION)
        self.api_url = f"https://{self.region}.api.insight.rapid7.com/vm/v4/integration/"
        self.session = Session()
        self.ivm_cloud_api = IVM_Cloud(params.get(Input.CREDENTIALS).get("secretKey"), self.logger, self.api_url)

    def test(self):
        self.api_url = f"https://{self.region}.api.insight.rapid7.com/validate"
        self.ivm_cloud_api.test_api(self.api_url)
        return {"success": True}
