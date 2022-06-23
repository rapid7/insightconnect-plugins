import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import GetAnalyzerInput, GetAnalyzerOutput, Input, Output, Component

# Custom imports below
from icon_cortex_v2.util.util import filter_analyzer, filter_analyzers


class GetAnalyzer(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_analyzer",
            description=Component.DESCRIPTION,
            input=GetAnalyzerInput(),
            output=GetAnalyzerOutput(),
        )

    def run(self, params={}):
        analyzer_id = params.get(Input.ANALYZER_ID)
        try:
            if analyzer_id:
                self.logger.info(f"User specified analyzer ID: {analyzer_id}")
                result = [filter_analyzer(self.connection.API.get_analyzer_by_id(analyzer_id))]
            else:
                self.logger.info("Getting all analyzers...")
                result = filter_analyzers(self.connection.API.get_analyzers())
            return {Output.LIST: result}
        except Exception as error:
            raise PluginException("Failed to get analyzers.", assistance=f"{error}")
