import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import GetIocInput, GetIocOutput, Input, Output, Component

# Custom imports below
from anyrun import RunTimeException
from anyrun.connectors.sandbox.base_connector import BaseSandboxConnector

from icon_any_run.util.config import Config
from icon_any_run.util.tools import prepare_csv_payload


class GetIoc(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_ioc", description=Component.DESCRIPTION, input=GetIocInput(), output=GetIocOutput()
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        analysis_uuid = params.get(Input.ANALYSIS_UUID, "")
        # END INPUT BINDING - DO NOT REMOVE

        try:
            with BaseSandboxConnector(self.connection.sandbox_api_key, integration=Config.VERSION) as connector:
                for status in connector.get_analysis_report(analysis_uuid):
                    self.logger.info(status)

                report = connector.get_analysis_report(analysis_uuid, report_format="ioc")

            file = prepare_csv_payload(analysis_uuid, report)

            return {
                Output.COUNT: len(report) if report else 0,
                Output.REPORT: file,
            }
        except RunTimeException as error:
            raise PluginException(
                cause="Failed to retrieve IOCs.",
                assistance=error.description,
                data=error.json,
            )
