import insightconnect_plugin_runtime

from .schema import ConnectionSchema, Input
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException


from icon_jira_service_management.util.api import JiraServiceManagementApi

# Custom imports below


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_token = None
        self.cloud_id = None
        self.email = None
        self.api = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        self.api_token = params.get(Input.API_TOKEN, {}).get("secretKey", "").strip()
        self.cloud_id = params.get(Input.CLOUD_ID, {}).strip()
        self.email = params.get(Input.EMAIL, "").strip()
        # END INPUT BINDING - DO NOT REMOVE

        self.api = JiraServiceManagementApi(
            api_token=self.api_token,
            cloud_id=self.cloud_id,
            email=self.email,
        )

    def test(self):
        self.logger.info("Testing API connection...")
        try:
            self.api.test_api()
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
