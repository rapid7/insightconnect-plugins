import insightconnect_plugin_runtime
from .schema import GetIndicatorScanStatusInput, GetIndicatorScanStatusOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.helper import clean


class GetIndicatorScanStatus(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_indicator_scan_status",
            description=Component.DESCRIPTION,
            input=GetIndicatorScanStatusInput(),
            output=GetIndicatorScanStatusOutput(),
        )

    def run(self, params={}):
        response = self.connection.client.get_scan_status(params.get(Input.TASK_ID))
        return clean({Output.TASK_ID: response.get("TaskId"), Output.STATUS: response.get("Status")})
