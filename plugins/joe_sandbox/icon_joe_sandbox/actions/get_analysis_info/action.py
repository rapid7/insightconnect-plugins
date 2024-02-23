import insightconnect_plugin_runtime
from .schema import GetAnalysisInfoInput, GetAnalysisInfoOutput, Input, Output

# Custom imports below
from insightconnect_plugin_runtime.helper import clean


class GetAnalysisInfo(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_analysis_info",
            description="Show the status and most important attributes of an analysis",
            input=GetAnalysisInfoInput(),
            output=GetAnalysisInfoOutput(),
        )

    def run(self, params={}):
        webid = params.get(Input.WEBID)

        analysis = self.connection.api.info(webid)
        return {Output.ANALYSIS: clean(analysis)}
