import insightconnect_plugin_runtime
from .schema import GetScansInput, GetScansOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightappsec.util.endpoints import Scans
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean_dict
import json


class GetScans(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_scans",
            description=Component.DESCRIPTION,
            input=GetScansInput(),
            output=GetScansOutput(),
        )

    def run(self, params={}):
        request = ResourceHelper(self.connection.session, self.logger)

        url = Scans.scans(self.connection.url)

        response = request.resource_request(url, "get", params=clean_dict(params))

        try:
            result = json.loads(response["resource"])
            result = result["data"]
        except json.decoder.JSONDecodeError as error:
            self.logger.error(f"InsightAppSec response: {response}")
            raise PluginException(
                cause="The response from InsightAppSec was not in JSON format. Contact support for help.",
                assistance=" See log for more details",
                data=error,
            )

        output = []
        for item in result:
            temp = {
                "id": item["id"],
                "app_id": item["app"]["id"],
                "scan_config_id": item["scan_config"]["id"],
                "submitter": item["submitter"],
                "submit_time": item["submit_time"],
                "completion_time": item.get("completion_time", ""),
                "status": item["status"],
                "failure_reason": item.get("failure_reason", ""),
                "links": item["links"],
            }
            output.append(temp)
        return {Output.SCANS: output}
