import insightconnect_plugin_runtime
from .schema import SearchAnalysisInput, SearchAnalysisOutput, Input, Output, Component

# Custom imports below


class SearchAnalysis(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_analysis",
            description=Component.DESCRIPTION,
            input=SearchAnalysisInput(),
            output=SearchAnalysisOutput(),
        )

    def run(self, params={}):
        query = params.get(Input.QUERY)
        analyses = self.connection.api.analysis_search(query)
        return {Output.ANALYSES: analyses}
