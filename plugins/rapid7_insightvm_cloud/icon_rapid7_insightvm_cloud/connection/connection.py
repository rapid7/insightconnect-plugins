import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from icon_rapid7_insightvm_cloud.util.api import IVM_Cloud


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.ivm_cloud_api = None
        self.api_key = None
        self.region = None

    def connect(self, params={}) -> None:
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        self.region = params.get(Input.REGION, "us").strip()
        self.api_key = params.get(Input.CREDENTIALS, {}).get("secretKey", "").strip()
        # END INPUT BINDING - DO NOT REMOVE

        self.logger.info("Connect: Connecting...")
        user_agent_version = "test-version" if not hasattr(self, "meta.version") else self.meta.version
        self.ivm_cloud_api = IVM_Cloud(self.region, self.api_key, user_agent_version, self.logger)

    def test(self):
        self.ivm_cloud_api.test_api(f"https://{self.region}.api.insight.rapid7.com/validate")
        return {"success": True}
