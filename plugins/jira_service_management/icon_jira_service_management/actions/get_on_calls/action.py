import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import GetOnCallsInput, GetOnCallsOutput, Input, Output, Component

# Custom imports below


class GetOnCalls(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_on_calls", description=Component.DESCRIPTION, input=GetOnCallsInput(), output=GetOnCallsOutput()
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        name = params.get(Input.NAME)
        # END INPUT BINDING - DO NOT REMOVE

        return {
            Output.MESSAGE: None,
        }
