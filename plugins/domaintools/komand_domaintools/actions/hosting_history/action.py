import insightconnect_plugin_runtime
from .schema import HostingHistoryInput, HostingHistoryOutput, Input, Output, Component

# Custom imports below
from komand_domaintools.util import util


class HostingHistory(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="hosting_history",
            description=Component.DESCRIPTION,
            input=HostingHistoryInput(),
            output=HostingHistoryOutput(),
        )

    def run(self, params={}):
        query = params.get(Input.DOMAIN)
        response = util.make_request(self.connection.api.hosting_history, query)
        return self._cleanup_response(response)

    def _cleanup_response(self, response):
        ip_history = response.get("response", {}).get("ip_history")
        for key, value in enumerate(ip_history):
            if value.get("pre_ip") is None:
                ip_history[key]["pre_ip"] = ""

            if value.get("post_ip") is None:
                ip_history[key]["post_ip"] = ""

        response.get("response", {})["ip_history"] = ip_history
        return response
