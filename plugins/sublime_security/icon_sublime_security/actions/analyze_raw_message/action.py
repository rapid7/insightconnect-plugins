import insightconnect_plugin_runtime
from .schema import AnalyzeRawMessageInput, AnalyzeRawMessageOutput, Input, Output, Component
# Custom imports below


class AnalyzeRawMessage(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="analyze_raw_message",
                description=Component.DESCRIPTION,
                input=AnalyzeRawMessageInput(),
                output=AnalyzeRawMessageOutput())

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        raw_message = params.get(Input.RAW_MESSAGE)
        # END INPUT BINDING - DO NOT REMOVE

        return {
            Output.ANALYSIS: None,
        }
