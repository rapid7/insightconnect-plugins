import insightconnect_plugin_runtime
from .schema import SubmitSampleUrlInput, SubmitSampleUrlOutput, Input, Output, Component
# Custom imports below


class SubmitSampleUrl(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="submit_sample_url",
            description=Component.DESCRIPTION,
            input=SubmitSampleUrlInput(),
            output=SubmitSampleUrlOutput())

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        # END INPUT BINDING - DO NOT REMOVE
        # TODO - If input bindings for connection can be done check to same if it you can do the same here
        sample_url = params.get("sample_url")
        parameters = params.get("parameters", {})
        additional_parameters = params.get("additional_parameters", {})

        additional_parameters.update({"accept-tac": 1})

        webids = self.connection.api.submit_sample_url(
            sample_url, parameters, additional_parameters)
        return webids
