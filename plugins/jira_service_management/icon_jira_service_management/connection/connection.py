import insightconnect_plugin_runtime

from .schema import ConnectionSchema, Input

from icon_jira_service_management.util.api import JiraServiceManagementApi

# Custom imports below


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client_id = None
        self.client_secret = None
        self.instance = None
        self.api = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        self.client_id = params.get(Input.CLIENT_ID).get("secretKey")
        self.client_secret = params.get(Input.CLIENT_SECRET).get("secretKey")
        self.instance = params.get(Input.INSTANCE)
        # END INPUT BINDING - DO NOT REMOVE

        self.api = JiraServiceManagementApi(
            client_id=self.client_id,
            client_secret=self.client_secret,
            instance=self.instance,
            logger=self.logger,
        )

        self.logger.info(f"{self.api.cloud_id} - {self.api.instance} - Connection established successfully.")
        self.logger.info(f"{self.api.authorization} - {self.api.instance} - Connection established successfully.")

    def test(self):
        # TODO: Implement connection test
        pass
