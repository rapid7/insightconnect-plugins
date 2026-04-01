import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import LinuxFileAnalysisInput, LinuxFileAnalysisOutput, Input, Output, Component

# Custom imports below
from anyrun import RunTimeException
from anyrun.connectors import SandboxConnector

from icon_any_run.util.config import Config


class LinuxFileAnalysis(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="linux_file_analysis",
            description=Component.DESCRIPTION,
            input=LinuxFileAnalysisInput(),
            output=LinuxFileAnalysisOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        file_content = params.pop(Input.FILE_CONTENT)
        filename = params.pop(Input.FILENAME)
        # END INPUT BINDING - DO NOT REMOVE
        try:
            with SandboxConnector.linux(self.connection.sandbox_api_key, integration=Config.VERSION) as connector:
                analysis_uuid = connector.run_file_analysis(file_content, filename, **params)

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
