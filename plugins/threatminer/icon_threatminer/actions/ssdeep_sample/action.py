import insightconnect_plugin_runtime

from .schema import Component, Input, Output, SsdeepSampleInput, SsdeepSampleOutput

# Custom imports below


class SsdeepSample(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="ssdeep_sample",
            description=Component.DESCRIPTION,
            input=SsdeepSampleInput(),
            output=SsdeepSampleOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        query = params.get(Input.QUERY, "")
        # END INPUT BINDING - DO NOT REMOVE

        return {Output.RESPONSE: self.connection.api_client.ssdeep(query, report=False)}
