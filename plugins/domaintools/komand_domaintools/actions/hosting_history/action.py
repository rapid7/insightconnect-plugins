import insightconnect_plugin_runtime

from .schema import HostingHistoryInput, HostingHistoryOutput
from ...util.util import make_request


class HostingHistory(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="hosting_history",
            description="Provides a list of changes that have occurred in a Domain Name's registrar, IP address, and name servers",
            input=HostingHistoryInput(),
            output=HostingHistoryOutput(),
        )

    def run(self, params={}):
        query = params.get("domain")
        response = make_request(self.connection.api.hosting_history, query)
        return self._cleanup_response(response)

    def _cleanup_response(self, response):
        ip_history = response["response"]["ip_history"]
        for k, v in enumerate(ip_history):
            if v["pre_ip"] is None:
                ip_history[k]["pre_ip"] = ""

            if v["post_ip"] is None:
                ip_history[k]["post_ip"] = ""

        response["response"]["ip_history"] = ip_history
        return response
