import komand
from .schema import SampleSamplesInput, SampleSamplesOutput
# Custom imports below


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
            self.logger.error("SampleSamples: Run: Problem with request")
            raise e

        if "error" in sample_samples:
            self.logger.error("SampleSamples: Run: Only Threat Grid customers have access to artifact data")
            raise Exception("SampleSamples: Run: Only Threat Grid customers have access to artifact data")

        return sample_samples

    def test(self):
        return {"samples": []}
