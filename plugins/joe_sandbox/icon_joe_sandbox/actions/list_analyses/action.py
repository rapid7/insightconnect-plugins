import insightconnect_plugin_runtime
from .schema import ListAnalysesInput, ListAnalysesOutput, Output, Component

# Custom imports below


class ListAnalyses(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_analyses",
            description=Component.DESCRIPTION,
            input=ListAnalysesInput(),
            output=ListAnalysesOutput(),
        )

    def run(self):
        analyses = self.connection.api.analysis_list()
        return {Output.ANALYSES: analyses}
