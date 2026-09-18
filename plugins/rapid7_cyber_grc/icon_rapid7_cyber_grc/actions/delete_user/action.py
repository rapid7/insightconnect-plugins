import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import DeleteUserInput, DeleteUserOutput, Input, Output, Component

# Custom imports below


class DeleteUser(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_user", description=Component.DESCRIPTION, input=DeleteUserInput(), output=DeleteUserOutput()
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        id = params.get(Input.ID)
        # END INPUT BINDING - DO NOT REMOVE
        return {Output.RESULT: self.connection.client.delete_record("Users", id)}
