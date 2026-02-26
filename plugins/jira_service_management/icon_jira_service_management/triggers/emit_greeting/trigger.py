import insightconnect_plugin_runtime
import time
from .schema import EmitGreetingInput, EmitGreetingOutput, Input, Output, Component

# Custom imports below


class EmitGreeting(insightconnect_plugin_runtime.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="emit_greeting",
            description=Component.DESCRIPTION,
            input=EmitGreetingInput(),
            output=EmitGreetingOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        interval = params.get(Input.INTERVAL)
        # END INPUT BINDING - DO NOT REMOVE

        while True:
            # TODO: Implement trigger functionality
            self.send(
                {
                    Output.GREETING: None,
                }
            )
            time.sleep(5)
