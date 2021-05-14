import insightconnect_plugin_runtime
from .schema import GetScanInput, GetScanOutput, Input
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


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

        response = self.connection.ivm_cloud_api.call_api("scan/" + scan_id, "GET")
        if response[1].get("finished") is None:
            raise PluginException(
                cause=f"Failed to get a valid response from InsightVM with given scan ID '{scan_id}'.",
                assistance="Please try a different scan ID.",
                data=400,
            )
        else:
            return response[1]
