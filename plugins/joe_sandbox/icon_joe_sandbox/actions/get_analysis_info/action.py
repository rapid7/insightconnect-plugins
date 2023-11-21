import insightconnect_plugin_runtime
from .schema import GetAnalysisInfoInput, GetAnalysisInfoOutput, Input, Output, Component
# Custom imports below


class GetAnalysisInfo(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="get_analysis_info",
                description=Component.DESCRIPTION,
                input=GetAnalysisInfoInput(),
                output=GetAnalysisInfoOutput())

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        # END INPUT BINDING - DO NOT REMOVE
        # TODO - If input bindings for connection can be done check to same if it you can do the same here
        webid = params.get("webid")

        analysis = self.connection.api.analysis_info(webid = webid)
        return {"analysis": analysis}

