import insightconnect_plugin_runtime
from .schema import SubmitSampleUrlInput, SubmitSampleUrlOutput, Input, Output, Component

# Custom imports below


class SubmitSampleUrl(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="submit_sample_url",
            description=Component.DESCRIPTION,
            input=SubmitSampleUrlInput(),
            output=SubmitSampleUrlOutput(),
        )

    def run(self, params={}):
        sample_url = params.get(Input.SAMPLE_URL)
        parameters = params.get(Input.PARAMETERS, {})
        additional_parameters = params.get(Input.ADDITIONAL_PARAMETERS, {})

        additional_parameters.update({"accept-tac": 1})

        submission_id = self.connection.api.submit_sample_url(sample_url, parameters, additional_parameters)
        return {Output.SUBMISSION_ID: submission_id}
