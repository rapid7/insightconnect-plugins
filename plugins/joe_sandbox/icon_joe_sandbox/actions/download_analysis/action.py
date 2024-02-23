import insightconnect_plugin_runtime
from .schema import DownloadAnalysisInput, DownloadAnalysisOutput, Input, Output

# Custom imports below
from base64 import b64encode


class DownloadAnalysis(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="download_analysis",
            description="Download a resource for an analysis. This can be a full report, binaries, screenshots, etc",
            input=DownloadAnalysisInput(),
            output=DownloadAnalysisOutput(),
        )

    def run(self, params={}):
        webid = params.get(Input.WEBID)
        run = params.get(Input.RUN)
        type_ = params.get(Input.TYPE, "html")

        resource_name, resource_content = self.connection.api.download(webid, type_, run)

        return {
            Output.RESOURCE_NAME: resource_name,
            Output.RESOURCE_CONTENT: b64encode(resource_content).decode(),
        }
