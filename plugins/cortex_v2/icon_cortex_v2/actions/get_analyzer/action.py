import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import GetAnalyzerInput, GetAnalyzerOutput, Input, Output

# Custom imports below


class GetAnalyzer(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_analyzer",
            description="List enabled analyzers within Cortex",
            input=GetAnalyzerInput(),
            output=GetAnalyzerOutput(),
        )

    def run(self, params={}):
        analyzer_id = params.get(Input.ANALYZER_ID)
        if analyzer_id:
            self.logger.info(f"User specified analyzer ID: {analyzer_id}")
        else:
            self.logger.info("Getting all analyzers...")
        try:
            return {Output.LIST: self.connection.API.get_analyzer_by_id(analyzer_id)}
        except Exception as e:
            raise PluginException(f"Failed to get analyzers.", assistance=f"{e}")
