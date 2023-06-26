import insightconnect_plugin_runtime
from .schema import SubmitUrlInput, SubmitUrlOutput

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
        url = params.get("url")
        optional_params = params.get("optional_params")
        analyzer_mode = params.get("analyzer_mode")
        if analyzer_mode != "default":
            optional_params["analyzer_mode"] = analyzer_mode
        resp = self.connection.api.submit_url(url, optional_params)
        clean_data = insightconnect_plugin_runtime.helper.clean(resp["data"])
        return {"results": clean_data}
