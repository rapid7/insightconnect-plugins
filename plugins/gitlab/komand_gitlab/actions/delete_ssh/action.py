import insightconnect_plugin_runtime
from .schema import DeleteSshInput, DeleteSshOutput, Input, Output, Component

# Custom imports below


class DeleteSsh(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_ssh",
            description=Component.DESCRIPTION,
            input=DeleteSshInput(),
            output=DeleteSshOutput(),
        )

    def run(self, params={}):
        # TODO - Change their type to string
        user_id = params.get(Input.ID)
        key_id = params.get(Input.KEY_ID)
        self.connection.client.delete_ssh(user_id=user_id, key_id=key_id)

        return {Output.STATUS: True}
