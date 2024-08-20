import insightconnect_plugin_runtime
from .schema import GetScanInput, GetScanOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightappsec.util.endpoints import Scans
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper
from insightconnect_plugin_runtime.exceptions import PluginException
import json


class GetScan(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_scan", description=Component.DESCRIPTION, input=GetScanInput(), output=GetScanOutput()
        )

    def run(self, params={}):
        scan_id = params.get(Input.SCAN_ID)
        request = ResourceHelper(self.connection.session, self.logger)

        url = Scans.scans(self.connection.url)
        url = f"{url}/{scan_id}"

        response = request.resource_request(url, "get")
        try:
            result = json.loads(response["resource"])
        except json.decoder.JSONDecodeError as error:
            self.logger.error(f"InsightAppSec response: {response}")
            raise PluginException(
                cause="The response from InsightAppSec was not in JSON format. Contact support for help.",
                assistance=" See log for more details",
                data=error,
            )

        try:
            output = {
                "id": result["id"],
                "app_id": result["app"]["id"],
                "scan_config_id": result["scan_config"]["id"],
                "submitter": result["submitter"],
                "submit_time": result["submit_time"],
                "completion_time": result.get("completion_time", ""),
                "status": result["status"],
                "failure_reason": result.get("failure_reason", ""),
                "links": result["links"],
            }
            return {Output.SCAN: output}
        except KeyError as error:
            self.logger.error(result)
            raise PluginException(
                cause="The response from InsightAppSec was not in the correct format. Contact support for help.",
                assistance=" See log for more details",
                data=error,
            )
