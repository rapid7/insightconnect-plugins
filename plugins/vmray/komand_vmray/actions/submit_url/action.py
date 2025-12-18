import insightconnect_plugin_runtime
from .schema import SubmitUrlInput, SubmitUrlOutput, Output, Input

# Custom imports below


class SubmitUrl(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="submit_url",
            description="Submits a URL for analysis",
            input=SubmitUrlInput(),
            output=SubmitUrlOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        url = params.get(Input.URL, "")
        optional_params = params.get(Input.OPTIONAL_PARAMS, {})
        analyzer_mode = params.get(Input.ANALYZER_MODE, "default")
        # END INPUT BINDING - DO NOT REMOVE

        if analyzer_mode != "default":
            optional_params["analyzer_mode"] = analyzer_mode
        response = self.connection.api.submit_url(url, optional_params)
        clean_data = insightconnect_plugin_runtime.helper.clean(response.get("data", {}))
        return {Output.RESULTS: clean_data}
