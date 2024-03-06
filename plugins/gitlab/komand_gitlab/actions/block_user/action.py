import insightconnect_plugin_runtime
from .schema import BlockUserInput, BlockUserOutput, Input, Output, Component

# Custom imports below


class BlockUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="block_user",
            description=Component.DESCRIPTION,
            input=BlockUserInput(),
            output=BlockUserOutput(),
        )

    def run(self, params={}):
        user_id = params.get(Input.ID)
        self.connection.client.block_user(user_id=user_id)
        return {Output.SUCCESS: True}
