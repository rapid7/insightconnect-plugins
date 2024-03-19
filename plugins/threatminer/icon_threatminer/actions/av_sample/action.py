import insightconnect_plugin_runtime

from .schema import AvSampleInput, AvSampleOutput, Component, Input, Output

# Custom imports below


class AvSample(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="av_sample",
            description=Component.DESCRIPTION,
            input=AvSampleInput(),
            output=AvSampleOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        query = params.get(Input.QUERY, "")
        # END INPUT BINDING - DO NOT REMOVE

        return {Output.RESPONSE: self.connection.api_client.av_detection(query, report=False)}
