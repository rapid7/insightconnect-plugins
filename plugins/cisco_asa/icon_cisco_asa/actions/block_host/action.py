import insightconnect_plugin_runtime
from .schema import BlockHostInput, BlockHostOutput, Input, Output, Component

# Custom imports below


class BlockHost(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="block_host", description=Component.DESCRIPTION, input=BlockHostInput(), output=BlockHostOutput()
        )

    def run(self, params={}):
        return {
            Output.SUCCESS: self.connection.cisco_asa_api.block_host(
                params.get(Input.SHUN),
                params.get(Input.SOURCE_IP),
                params.get(Input.DESTINATION_IP),
                params.get(Input.SOURCE_PORT),
                params.get(Input.DESTINATION_PORT),
                params.get(Input.PROTOCOL),
            )
        }
