import insightconnect_plugin_runtime
from .schema import GetReportInput, GetReportOutput, Input, Output, Component
# Custom imports below
from ...util.util import Util


class GetReport(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_report",
            description=Component.DESCRIPTION,
            input=GetReportInput(),
            output=GetReportOutput(),
        )

    def run(self, params={}):
        task_id = params.get(Input.TASK_ID, "")
        desired_format = params.get(Input.FORMAT, "")

        if desired_format:
            endpoint = f"/tasks/report/{task_id}/{desired_format}"
        else:
            endpoint = f"/tasks/report/{task_id}"
        response = self.connection.api.send(endpoint, _json=False)
        content = response.content
        return {Output.REPORT: Util.prepare_decoded_value(content)}
