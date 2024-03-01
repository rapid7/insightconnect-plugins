import insightconnect_plugin_runtime
from .schema import GetAnalysisInfoInput, GetAnalysisInfoOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.helper import clean

class GetAnalysisInfo(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_analysis_info",
            description=Component.DESCRIPTION,
            input=GetAnalysisInfoInput(),
            output=GetAnalysisInfoOutput(),
        )

    def run(self, params={}):
        webid = params.get(Input.WEBID)

        analysis = self.connection.api.analysis_info(webid)

        analysis = clean(analysis)
        return {Output.ANALYSIS: analysis}
