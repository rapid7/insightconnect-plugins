import insightconnect_plugin_runtime

from icon_rapid7_insightvm_cloud.util.error_handling import ERRORS
from .schema import StopScanInput, StopScanOutput, Input, Output

# Custom imports below


class StopScan(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="stop_scan",
            description="Stop a currently running scan",
            input=StopScanInput(),
            output=StopScanOutput(),
        )

    def run(self, params={}):
        scan_id = params.get(Input.ID)
        url = f"scan/{scan_id}/stop"
        response = self.connection.ivm_cloud_api.call_api(url, "POST")
        if response == 202:
            return {Output.SUCCESS: True}
        else:
            return {Output.SUCCESS: False, Output.STATUS_CODE: response, Output.MESSAGE: ERRORS.get(response)}
