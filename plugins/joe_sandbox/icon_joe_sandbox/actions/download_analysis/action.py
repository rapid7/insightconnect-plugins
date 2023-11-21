import insightconnect_plugin_runtime
from .schema import DownloadAnalysisInput, DownloadAnalysisOutput, Input, Output, Component
# Custom imports below
from base64 import b64encode

class DownloadAnalysis(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="download_analysis",
                description=Component.DESCRIPTION,
                input=DownloadAnalysisInput(),
                output=DownloadAnalysisOutput())

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        # END INPUT BINDING - DO NOT REMOVE
        # TODO - If input bindings for connection can be done check to same if it you can do the same here
        webid = params.get("webid")
        run = params.get("run")
        type_ = params.get("type", "html")

        resource_name, resource_content = self.connection.api.analysis_download(webid, type_, run)
        
        return {
                "resource_name": resource_name,
                "resource_content": b64encode(resource_content).decode(),
                }

