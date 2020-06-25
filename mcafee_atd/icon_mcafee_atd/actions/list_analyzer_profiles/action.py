import insightconnect_plugin_runtime
from .schema import ListAnalyzerProfilesInput, ListAnalyzerProfilesOutput, Output, Component
# Custom imports below
from insightconnect_plugin_runtime import helper


class ListAnalyzerProfiles(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_analyzer_profiles',
                description=Component.DESCRIPTION,
                input=ListAnalyzerProfilesInput(),
                output=ListAnalyzerProfilesOutput())

    def run(self, params={}):
        result = self.connection.mcafee_atd_api.list_analyzer_profiles()
        return {
            Output.PROFILER_RESULTS: helper.clean(result.get("results", [])),
            Output.SUCCESS: result.get("success", False)
        }
