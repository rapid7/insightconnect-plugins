import insightconnect_plugin_runtime
from .schema import StopScanInput, StopScanOutput, Input, Output

# Custom imports below
import requests

_ERRORS = {
    400: "Bad Request",
    401: "Unauthorized",
    500: "Internal Server Error",
    503: "Service Unavailable",
    000: "Unknown Status Code",
}


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
        try:
            response = self.connection.ivm_cloud_api.call_api(url, "POST")
            if response == 202:
                return {Output.SUCCESS: True}
            else:
                return {Output.SUCCESS: False, Output.STATUS_CODE: response, Output.MESSAGE: _ERRORS.get(response)}
        except requests.RequestException as e:
            self.logger.error(e)
            raise
