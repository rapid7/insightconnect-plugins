import insightconnect_plugin_runtime
from .schema import SearchAnalysisInput, SearchAnalysisOutput, Input, Output, Component
# Custom imports below


class SearchAnalysis(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="search_analysis",
                description=Component.DESCRIPTION,
                input=SearchAnalysisInput(),
                output=SearchAnalysisOutput())

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        # END INPUT BINDING - DO NOT REMOVE
        # TODO - If input bindings for connection can be done check to same if it you can do the same here

        query = params.get("query")
        analyses = self.connection.api.analysis_search(query)

        return {"analyses": analyses}
