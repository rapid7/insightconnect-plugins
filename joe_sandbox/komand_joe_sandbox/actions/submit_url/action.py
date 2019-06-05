import komand
from .schema import SubmitUrlInput, SubmitUrlOutput, Input, Output
# Custom imports below


class SubmitUrl(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='submit_url',
                description='Submit a website for analysis and return the associated web IDs for the sample',
                input=SubmitUrlInput(),
                output=SubmitUrlOutput())

    def run(self, params={}):
        url = params.get('url')
        parameters = params.get('parameters', {})
        additional_parameters = params.get('additional_parameters', {})

        additional_parameters.update({'accept-tac': 1})

        webids = self.connection.api.submit_url(
            url, parameters, additional_parameters
        )
        return webids
