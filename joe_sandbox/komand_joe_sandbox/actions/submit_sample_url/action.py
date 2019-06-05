import komand
from .schema import SubmitSampleUrlInput, SubmitSampleUrlOutput, Input, Output
# Custom imports below
from base64 import b64decode


class SubmitSampleUrl(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='submit_sample_url',
                description='Submit a sample at a given URL for analysis and return the associated web IDs for the sample',
                input=SubmitSampleUrlInput(),
                output=SubmitSampleUrlOutput())

    def run(self, params={}):
        sample_url = params.get('sample_url')
        parameters = params.get('parameters', {})
        additional_parameters = params.get('additional_parameters', {})

        additional_parameters.update({'accept-tac': 1})

        webids = self.connection.api.submit_sample_url(
            sample_url, parameters, additional_parameters
        )
        return webids
