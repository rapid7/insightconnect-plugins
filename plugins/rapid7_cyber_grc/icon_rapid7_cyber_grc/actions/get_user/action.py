import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import GetUserInput, GetUserOutput, Input, Output, Component

# Custom imports below


class GetUser(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_user", description=Component.DESCRIPTION, input=GetUserInput(), output=GetUserOutput()
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        id = params.get(Input.ID)
        select = params.get(Input.SELECT)
        # END INPUT BINDING - DO NOT REMOVE
        return {Output.USER: self.connection.client.get_record("Users", id, select=select)}
