import insightconnect_plugin_runtime
from .schema import GetAnalysisInput, GetAnalysisOutput, Output

# Custom imports below


class GetAnalysis(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_analysis",
            description="Get all dynamic and static analyses in the system or details about specific ones",
            input=GetAnalysisInput(),
            output=GetAnalysisOutput(),
        )

    def run(self, params={}):
        id_type = params.get("id_type")
        analysis_id = params.get("id")
        optional_params = params.get("optional_params")
        resp = self.connection.api.get_analysis(analysis_id, id_type, optional_params)
        clean_results = insightconnect_plugin_runtime.helper.clean(resp.get("data", []))
        if isinstance(clean_results, dict):
            clean_results = [clean_results]
        return {Output.RESULTS: clean_results}
