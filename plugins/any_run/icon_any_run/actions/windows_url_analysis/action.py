import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import WindowsUrlAnalysisInput, WindowsUrlAnalysisOutput, Output, Component

# Custom imports below
from anyrun import RunTimeException
from anyrun.connectors import SandboxConnector

from icon_any_run.util.config import Config


class WindowsUrlAnalysis(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="windows_url_analysis",
            description=Component.DESCRIPTION,
            input=WindowsUrlAnalysisInput(),
            output=WindowsUrlAnalysisOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        try:
            with SandboxConnector.windows(self.connection.sandbox_api_key, integration=Config.VERSION) as connector:
                analysis_uuid = connector.run_url_analysis(**params)

            return {
                Output.ANALYSIS_UUID: analysis_uuid,
                Output.ANALYSIS_URL: f"https://app.any.run/tasks/{analysis_uuid}",
            }
        except RunTimeException as error:
            raise PluginException(
                cause="Failed to start analysis.",
                assistance=error.description,
                data=error.json,
            )
