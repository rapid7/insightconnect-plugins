import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import GetAnalysisVerdictInput, GetAnalysisVerdictOutput, Input, Output, Component

# Custom imports below
from anyrun import RunTimeException
from anyrun.connectors.sandbox.base_connector import BaseSandboxConnector

from icon_any_run.util.config import Config


class GetAnalysisVerdict(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_analysis_verdict",
            description=Component.DESCRIPTION,
            input=GetAnalysisVerdictInput(),
            output=GetAnalysisVerdictOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        analysis_uuid = params.get(Input.ANALYSIS_UUID, "")
        # END INPUT BINDING - DO NOT REMOVE

        try:
            with BaseSandboxConnector(self.connection.sandbox_api_key, integration=Config.VERSION) as connector:
                for status in connector.get_task_status(analysis_uuid):
                    self.logger.info(status)

                verdict = connector.get_analysis_verdict(analysis_uuid)

            return {Output.VERDICT: verdict}
        except RunTimeException as error:
            raise PluginException(
                cause="Failed to fetch analysis verdict.",
                assistance=error.description,
                data=error.json,
            )
