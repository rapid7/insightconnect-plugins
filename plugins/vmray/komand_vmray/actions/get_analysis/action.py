import insightconnect_plugin_runtime
from .schema import GetAnalysisInput, GetAnalysisOutput, Output, Input

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
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        analysis_id = params.get(Input.ID, "")
        id_type = params.get(Input.ID_TYPE, "all")
        optional_params = params.get(Input.OPTIONAL_PARAMS, {})
        # END INPUT BINDING - DO NOT REMOVE

        response = self.connection.api.get_analysis(analysis_id, id_type, optional_params)
        clean_results = insightconnect_plugin_runtime.helper.clean(response.get("data", []))
        if isinstance(clean_results, dict):
            clean_results = [clean_results]
        return {Output.RESULTS: clean_results}
