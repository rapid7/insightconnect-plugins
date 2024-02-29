import insightconnect_plugin_runtime
from .schema import DeleteAnalysisInput, DeleteAnalysisOutput, Input, Output, Component

# Custom imports below


class DeleteAnalysis(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_analysis",
            description=Component.DESCRIPTION,
            input=DeleteAnalysisInput(),
            output=DeleteAnalysisOutput(),
        )

    def run(self, params={}):
        webid = params.get(Input.WEBID)

        deleted = self.connection.api.analysis_delete(webid)
        return {Output.DELETED: deleted.get("deleted")}
