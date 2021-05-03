import insightconnect_plugin_runtime
from .schema import GetScanInput, GetScanOutput, Input

# Custom imports below
import requests


class GetScan(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_scan",
            description="Gets the status of a scan",
            input=GetScanInput(),
            output=GetScanOutput(),
        )

    def run(self, params={}):
        scan_id = params.get(Input.SCAN_ID)

        try:
            response = self.connection.ivm_cloud_api.call_api("scan/" + scan_id, "GET")
            return response
        except requests.RequestException as e:
            self.logger.error(e)
            raise
