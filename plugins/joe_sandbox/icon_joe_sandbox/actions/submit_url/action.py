import insightconnect_plugin_runtime
from .schema import SubmitUrlInput, SubmitUrlOutput, Input, Output

# Custom imports below


class SubmitUrl(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="submit_url",
            description="Submit a website for analysis and return the associated web IDs for the sample",
            input=SubmitUrlInput(),
            output=SubmitUrlOutput(),
        )

    def run(self, params={}):
        url = params.get(Input.URL)
        parameters = params.get(Input.PARAMETERS, {})
        additional_parameters = params.get(Input.ADDITIONAL_PARAMETERS, {})

        additional_parameters.update({"accept-tac": 1})

        webids = self.connection.api.submit_url(url, parameters, additional_parameters)
        return {Output.WEBIDS: webids}
