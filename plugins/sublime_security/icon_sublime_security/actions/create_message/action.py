import insightconnect_plugin_runtime
from .schema import CreateMessageInput, CreateMessageOutput, Input, Output, Component
# Custom imports below


class CreateMessage(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="create_message",
                description=Component.DESCRIPTION,
                input=CreateMessageInput(),
                output=CreateMessageOutput())

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        message = params.get(Input.MESSAGE)
        # END INPUT BINDING - DO NOT REMOVE

        return {
            Output.MESSAGE_ID: None,
        }
