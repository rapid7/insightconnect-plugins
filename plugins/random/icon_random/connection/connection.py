import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
# Custom imports below


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        # TODO: generate bound input variables for the user, to help handhold the user
        # TODO: ex. self.api_key = params.get(Input.API_KEY)
        # END INPUT BINDING - DO NOT REMOVE
        self.logger.info("Connect: Connecting...")

    def test(self):
        # TODO: Implement connection test
        pass