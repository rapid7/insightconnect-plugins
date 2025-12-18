import insightconnect_plugin_runtime
from .schema import GetSamplesInput, GetSamplesOutput, Output, Input

# Custom imports below


class GetSamples(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_samples",
            description="Get all samples in the system or details about specific ones. You can also search by hashes",
            input=GetSamplesInput(),
            output=GetSamplesOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        sample_type = params.get(Input.SAMPLE_TYPE, "all")
        sample = params.get(Input.SAMPLE, "")
        optional_params = params.get(Input.OPTIONAL_PARAMS, {})
        # END INPUT BINDING - DO NOT REMOVE

        response = self.connection.api.get_samples(sample_type, sample, optional_params)
        clean_data = insightconnect_plugin_runtime.helper.clean(response.get("data", []))
        if isinstance(clean_data, dict):
            clean_data = [clean_data]
        return {Output.RESULTS: clean_data}
