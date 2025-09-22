import time

import insightconnect_plugin_runtime

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
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        scan_id = params.get(Input.ID)
        # END INPUT BINDING - DO NOT REMOVE

        url = f"scan/{scan_id}/stop"
        self.connection.ivm_cloud_api.call_api(url, "POST")
        time.sleep(5)
        response = self.connection.ivm_cloud_api.call_api("scan/" + scan_id, "GET")
        if response.get("status") == "Stopped":
            return {Output.SUCCESS: True}
        else:
            return {
                Output.SUCCESS: False,
                Output.STATUS_CODE: response.get("status_code"),
                Output.MESSAGE: f"Failed to stop scan with ID '{scan_id}'. Status of scan is {response.get('status')}",
            }
