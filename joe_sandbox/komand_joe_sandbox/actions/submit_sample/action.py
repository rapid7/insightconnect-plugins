import komand
from .schema import SubmitSampleInput, SubmitSampleOutput, Input, Output
# Custom imports below
from base64 import b64decode
import binascii


class SubmitSample(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='submit_sample',
                description='Submit a sample for analysis and return the associated web IDs for the sample',
                input=SubmitSampleInput(),
                output=SubmitSampleOutput())

    def run(self, params={}):
        sample = params.get('sample')
        cookbook = params.get('cookbook')
        parameters = params.get('parameters', {})
        additional_parameters = params.get('additional_parameters', {})

        additional_parameters.update({'accept-tac': 1})
        try:
            sample_bytes = b64decode(sample)
        except binascii.Error:
            raise Exception(
                'Unable to decode base64 input for "sample". '
                'Contents of the file must be encoded with base64!'
            )

        try:
            cookbook_bytes = b64decode(cookbook) if cookbook else None
        except binascii.Error:
            raise Exception(
                'Unable to decode base64 input for "cookbook". '
                'Contents of the file must be encoded with base64!'
            )

        webids = self.connection.api.submit_sample(
            sample_bytes, cookbook_bytes, parameters, additional_parameters
        )
        return webids
