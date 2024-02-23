import insightconnect_plugin_runtime
from .schema import SearchAnalysisInput, SearchAnalysisOutput, Input, Output

# Custom imports below


class SearchAnalysis(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_analysis",
            description="Lists the web IDs of the analyses that match the given query. Searches in MD5, SHA1, SHA256, filename, cookbook name, comment, url and report ID",
            input=SearchAnalysisInput(),
            output=SearchAnalysisOutput(),
        )

    def run(self, params={}):
        query = params.get(Input.QUERY)
        analyses = self.connection.api.search(query)
        return {Output.ANALYSES: analyses}
