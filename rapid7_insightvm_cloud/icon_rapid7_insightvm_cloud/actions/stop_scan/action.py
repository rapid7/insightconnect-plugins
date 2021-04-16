import insightconnect_plugin_runtime
from .schema import StopScanInput, StopScanOutput, Input, Output, Component
# Custom imports below
import requests


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
        url = "scan/"+scan_id+"/stop"
        try:
            response = self.connection.ivm_cloud_api.call_api(url, "POST")
            if response == 202:
                return {Output.SUCCESS: True}
            else:
                return {Output.SUCCESS: False}
        except requests.RequestException as e:
            self.logger.error(e)
            raise
