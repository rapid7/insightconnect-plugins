import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import GetAnalysisReportInput, GetAnalysisReportOutput, Input, Output, Component

# Custom imports below
from anyrun import RunTimeException
from anyrun.connectors.sandbox.base_connector import BaseSandboxConnector

from icon_any_run.util.config import Config
from icon_any_run.util.tools import prepare_file_payload


class GetAnalysisReport(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_analysis_report",
            description=Component.DESCRIPTION,
            input=GetAnalysisReportInput(),
            output=GetAnalysisReportOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        report_format = params.get(Input.FORMAT, "")
        analysis_uuid = params.get(Input.ANALYSIS_UUID, "")
        # END INPUT BINDING - DO NOT REMOVE
        try:
            with BaseSandboxConnector(self.connection.sandbox_api_key, integration=Config.VERSION) as connector:
                for status in connector.get_task_status(analysis_uuid):
                    self.logger.info(status)

                report = connector.get_analysis_report(analysis_uuid, report_format)

            file_payload = prepare_file_payload(analysis_uuid, report_format, report)

            return {
                Output.ANALYSIS_UUID: analysis_uuid,
                Output.ANALYSIS_URL: f"https://app.any.run/tasks/{analysis_uuid}",
                Output.REPORT: file_payload,
            }
        except RunTimeException as error:
            raise PluginException(
                cause="Failed to download analysis report.",
                assistance=error.description,
                data=error.json,
            )
