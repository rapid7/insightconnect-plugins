import insightconnect_plugin_runtime
from .schema import GetScanEngineEventsInput, GetScanEngineEventsOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightappsec.util.endpoints import Scans
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper
from insightconnect_plugin_runtime.exceptions import PluginException
import json


class GetScanEngineEvents(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_scan_engine_events",
            description=Component.DESCRIPTION,
            input=GetScanEngineEventsInput(),
            output=GetScanEngineEventsOutput(),
        )

    def run(self, params={}):
        scan_id = params.get(Input.SCAN_ID)
        request = ResourceHelper(self.connection.session, self.logger)

        url = Scans.scan_engine_events(self.connection.url, scan_id)
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
        return {Output.EVENTS: result}
