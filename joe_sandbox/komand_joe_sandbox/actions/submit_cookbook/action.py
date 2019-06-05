import komand
from .schema import SubmitCookbookInput, SubmitCookbookOutput, Input, Output
# Custom imports below
from base64 import b64decode
import binascii


class SubmitCookbook(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='submit_cookbook',
                description='Submit a cookbook for analysis and return the associated web IDs for the cookbook',
                input=SubmitCookbookInput(),
                output=SubmitCookbookOutput())

    def run(self, params={}):
        cookbook = params.get('cookbook')
        parameters = params.get('parameters', {})
        additional_parameters = params.get('additional_parameters', {})

        additional_parameters.update({'accept-tac': 1})

        try:
            cookbook_bytes = b64decode(cookbook) if cookbook else None
        except binascii.Error:
            raise Exception(
                'Unable to decode base64 input for "cookbook". '
                'Contents of the file must be encoded with base64!'
            )

        webids = self.connection.api.submit_cookbook(
            cookbook_bytes, parameters, additional_parameters
        )
        return webids
