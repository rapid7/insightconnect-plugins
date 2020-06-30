import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import GetReportInput, GetReportOutput, Input, Output, Component
# Custom imports below
import base64


class GetReport(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_report',
            description=Component.DESCRIPTION,
            input=GetReportInput(),
            output=GetReportOutput())

    def run(self, params={}):
        return_type = params.get(Input.REPORT_TYPE, "json").lower()
        type_id = params.get(Input.TYPE_ID, "MD5")
        if return_type == "sample" and type_id != "TASK ID":
            raise PluginException(
                cause="Type report error.",
                assistance="API allows use SAMPLE only when Type ID is TASK ID. "
                           "Please check to ensure all parameters are correct."
            )

        response = self.connection.mcafee_atd_api.get_report(
            params.get(Input.ID),
            return_type,
            type_id
        )

        report = {}
        if return_type == "json":
            report = response.json()
        return {
            Output.FILE: base64.b64encode(response.content).decode('utf-8'),
            Output.REPORT: report
        }
