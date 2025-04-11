import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below

from icon_rapid7_surface_command.util.surface_command.api_connection import ApiConnection


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        self.api_key = params.get(Input.API_KEY)
        self.region = params.get(Input.REGION)
        # END INPUT BINDING - DO NOT REMOVE

        self.api = ApiConnection(self.api_key.get("secretKey"), self.region, self.logger)
        self.logger.info("Setup Complete")

    def test(self):
        # TODO: Implement connection test
        pass
