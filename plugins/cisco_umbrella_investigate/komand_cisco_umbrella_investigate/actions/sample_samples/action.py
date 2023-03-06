import insightconnect_plugin_runtime
from .schema import SampleSamplesInput, SampleSamplesOutput, Input, Output

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class SampleSamples(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="sample_samples",
            description="Return other samples associated with a sample",
            input=SampleSamplesInput(),
            output=SampleSamplesOutput(),
        )

    def run(self, params={}):
        hash_ = params.get(Input.HASH)
        limit = params.get(Input.LIMIT)
        offset = params.get(Input.OFFSET)

        if not limit or limit == 0:
            limit = 10

        if not offset:
            offset = 0

        try:
            sample_samples = self.connection.investigate.sample_samples(hash_, limit=limit, offset=offset)
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

        if "error" in sample_samples:
            raise PluginException(
                cause="Unable to return artifact data.",
                assistance="Only Threat Grid customers have access to artifact data.",
            )

        return sample_samples
