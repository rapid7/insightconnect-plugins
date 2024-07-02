import insightconnect_plugin_runtime
from .schema import AnalyzeMessageByIdInput, AnalyzeMessageByIdOutput, Input, Output, Component
# Custom imports below


class AnalyzeMessageById(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="analyze_message_by_id",
                description=Component.DESCRIPTION,
                input=AnalyzeMessageByIdInput(),
                output=AnalyzeMessageByIdOutput())

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        message_id = params.get(Input.MESSAGE_ID)
        # END INPUT BINDING - DO NOT REMOVE

        return {
            Output.ANALYSIS: None,
        }
