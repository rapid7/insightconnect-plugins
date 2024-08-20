import insightconnect_plugin_runtime
from .schema import GetScanConfigsInput, GetScanConfigsOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightappsec.util.endpoints import ScanConfig
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper
from insightconnect_plugin_runtime.exceptions import PluginException
import json


class GetScanConfigs(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_scan_configs",
            description=Component.DESCRIPTION,
            input=GetScanConfigsInput(),
            output=GetScanConfigsOutput(),
        )

    def run(self, params={}):
        request = ResourceHelper(self.connection.session, self.logger)

        url = ScanConfig.scan_config(self.connection.url)

        request_params = {}
        for item in params:
            if params[item]:
                request_params[item] = params[item]
        response = request.resource_request(url, "get", params=request_params)
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
                "config_name": item["name"],
                "config_description": item.get("description", ""),
                "app_id": item["app"]["id"],
                "attack_template_id": item["attack_template"]["id"],
                "errors": item.get("errors", []),
                "links": item["links"],
            }
            output.append(temp)
        return {Output.SCAN_CONFIGS: output}
