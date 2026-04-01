import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import GetAnalysisHistoryInput, GetAnalysisHistoryOutput, Output, Component

# Custom imports below
from anyrun import RunTimeException
from anyrun.connectors.sandbox.base_connector import BaseSandboxConnector

from icon_any_run.util.config import Config


class GetAnalysisHistory(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_analysis_history",
            description=Component.DESCRIPTION,
            input=GetAnalysisHistoryInput(),
            output=GetAnalysisHistoryOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        try:
            with BaseSandboxConnector(self.connection.sandbox_api_key, integration=Config.VERSION) as connector:
                history_tasks = connector.get_analysis_history(**params)

            return {Output.ANALYSES: history_tasks}
        except RunTimeException as error:
            raise PluginException(
                cause="Failed to fetch analysis history.",
                assistance=error.description,
                data=error.json,
            )
