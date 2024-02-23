import insightconnect_plugin_runtime
from .schema import ListAnalysesInput, ListAnalysesOutput, Output

# Custom imports below


class ListAnalyses(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_analyses",
            description="Fetch a list of all analyses",
            input=ListAnalysesInput(),
            output=ListAnalysesOutput(),
        )

    def run(self, params={}):
        analyses = self.connection.api.list()
        return {Output.ANALYSES: analyses}
