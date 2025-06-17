import insightconnect_plugin_runtime
from .schema import GetALogInput, GetALogOutput, Input, Output, Component
from komand_rapid7_insightidr.util.endpoints import Logs
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import json


class GetALog(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_a_log", description=Component.DESCRIPTION, input=GetALogInput(), output=GetALogOutput()
        )

    def run(self, params={}):
        self.connection.headers["Accept-version"] = "investigations-preview"
        request = ResourceHelper(self.connection.headers, self.logger)
        response = request.resource_request(Logs.get_a_log(self.connection.url, params.get(Input.ID)), "get")
        try:
            result = json.loads(response["resource"])

        except (json.decoder.JSONDecodeError, IndexError, KeyError):
            self.logger.error(f"InsightIDR response: {response}")
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details.",
            )

        return {Output.LOG: result}
