import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import GetAnalyzerByTypeInput, GetAnalyzerByTypeOutput, Input, Output, Component

# Custom imports below
from icon_cortex_v2.util.util import filter_analyzers


class GetAnalyzerByType(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_analyzer_by_type",
            description=Component.DESCRIPTION,
            input=GetAnalyzerByTypeInput(),
            output=GetAnalyzerByTypeOutput(),
        )

    def run(self, params={}):
        try:
            return {Output.LIST: filter_analyzers(self.connection.API.get_analyzer_by_type(params.get(Input.TYPE)))}
        except Exception as e:
            raise PluginException("Failed to get analyzers.", assistance=f"{e}")
