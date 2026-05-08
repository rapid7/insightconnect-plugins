import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import CountTokensInput, CountTokensOutput, Input, Output, Component


class CountTokens(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="count_tokens", description=Component.DESCRIPTION, input=CountTokensInput(), output=CountTokensOutput()
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        prompt = params.get(Input.PROMPT)
        system_prompt = params.get(Input.SYSTEM_PROMPT)
        # END INPUT BINDING - DO NOT REMOVE

        response = self.connection.client.count_tokens(
            prompt=prompt,
            system_prompt=system_prompt,
        )

        return {
            Output.INPUT_TOKENS: response.get("input_tokens", 0),
        }
