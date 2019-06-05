import komand
from .schema import GetSamplesInput, GetSamplesOutput
# Custom imports below


class GetSamples(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_samples',
                description='Get all samples in the system or details about specific ones. You can also search by hashes',
                input=GetSamplesInput(),
                output=GetSamplesOutput())

    def run(self, params={}):
        sample_type, sample, optional_params = params.get("sample_type"), params.get("sample"), params.get("optional_params")

        resp = self.connection.api.get_samples(sample_type, sample, optional_params)
        clean_data = komand.helper.clean(resp["data"])
        return {"results": clean_data}
