import insightconnect_plugin_runtime

from .schema import Component, ImportHashSamplesInput, ImportHashSamplesOutput, Input, Output

# Custom imports below


class ImportHashSamples(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="import_hash_samples",
            description=Component.DESCRIPTION,
            input=ImportHashSamplesInput(),
            output=ImportHashSamplesOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        query = params.get(Input.QUERY, "")
        # END INPUT BINDING - DO NOT REMOVE

        return {Output.RESPONSE: self.connection.api_client.import_hash(query, report=False)}
