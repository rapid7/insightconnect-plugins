import komand
from .schema import SampleSamplesInput, SampleSamplesOutput
# Custom imports below
from komand.exceptions import PluginException


class SampleSamples(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='sample_samples',
                description='Return other samples associated with a sample',
                input=SampleSamplesInput(),
                output=SampleSamplesOutput())

    def run(self, params={}):
        hash = params.get('hash')
        limit = params.get('limit', None)
        offset = params.get('offset', None)
        
        if not limit or limit == 0:
            limit = 10
        
        if not offset:
            offset = 0

        try:
            sample_samples = self.connection.investigate.sample_samples(hash, limit=limit, offset=offset)
        except Exception as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN)

        if "error" in sample_samples:
            raise PluginException(cause='Unable to return artifact data.', assistance='Only Threat Grid customers have access to artifact data.')

        return sample_samples

    def test(self):
        return {"samples": []}
