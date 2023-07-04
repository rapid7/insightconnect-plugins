import insightconnect_plugin_runtime
from .schema import GetSamplesInput, GetSamplesOutput, Output

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
        sample_type, sample, optional_params = (
            params.get("sample_type"),
            params.get("sample"),
            params.get("optional_params"),
        )

        resp = self.connection.api.get_samples(sample_type, sample, optional_params)
        clean_data = insightconnect_plugin_runtime.helper.clean(resp.get("data", []))
        if isinstance(clean_data, dict):
            clean_data = [clean_data]
        return {Output.RESULTS: clean_data}
