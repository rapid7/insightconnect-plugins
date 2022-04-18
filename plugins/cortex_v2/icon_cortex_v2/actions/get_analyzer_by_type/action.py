import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import GetAnalyzerByTypeInput, GetAnalyzerByTypeOutput, Input, Output

# Custom imports below


class GetAnalyzerByType(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_analyzer_by_type",
            description="List analyzers that can act upon a given datatype",
            input=GetAnalyzerByTypeInput(),
            output=GetAnalyzerByTypeOutput(),
        )

    def run(self, params={}):
        try:
            return {Output.LIST: self.connection.API.get_analyzer_by_type(params.get(Input.TYPE))}
        except Exception as e:
            raise PluginException(f"Failed to get analyzers.", assistance=f"{e}")
