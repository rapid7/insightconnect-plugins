import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        self.hostname = params.get(Input.HOSTNAME)
        self.port = params.get(Input.PORT)
        self.username = params.get(Input.USERNAME)
        # END INPUT BINDING - DO NOT REMOVE

    def test(self):
        # TODO: Implement connection test
        pass
