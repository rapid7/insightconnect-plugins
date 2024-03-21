import insightconnect_plugin_runtime

from .schema import Component, Input, Output, SamplesInput, SamplesOutput

# Custom imports below


class Samples(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="samples",
            description=Component.DESCRIPTION,
            input=SamplesInput(),
            output=SamplesOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        query = params.get(Input.QUERY, "")
        query_type = params.get(Input.QUERY_TYPE, "")
        # END INPUT BINDING - DO NOT REMOVE

        return {Output.RESPONSE: self.connection.api_client.samples(query, query_type)}
