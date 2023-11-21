import insightconnect_plugin_runtime
from .schema import SubmitUrlInput, SubmitUrlOutput, Input, Output, Component
# Custom imports below


class SubmitUrl(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="submit_url",
            description=Component.DESCRIPTION,
            input=SubmitUrlInput(),
            output=SubmitUrlOutput())

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        # END INPUT BINDING - DO NOT REMOVE
        
        url = params.get("url")
        parameters = params.get("parameters", {})
        additional_parameters = params.get("additional_parameters", {})

        additional_parameters.update({"accept-tac": 1})

        self.logger.info(f"URL: {url} parameters: {parameters} additional_parameters: {additional_parameters}")

        submission_id_request = self.connection.api.submit_url(
            url, parameters, additional_parameters)

        submission_id_number = submission_id_request.get("submission_id")
        self.logger.info(f"Submission_id_request: {submission_id_request} Submission_id_number: {submission_id_number}")

        return {'submission_id': submission_id_number}
