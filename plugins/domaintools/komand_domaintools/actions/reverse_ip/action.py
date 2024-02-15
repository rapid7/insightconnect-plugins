import insightconnect_plugin_runtime

from .schema import ReverseIpInput, ReverseIpOutput
from ...util.util import make_request


class ReverseIp(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="reverse_ip",
            description="Provides a list of domain names that share the same Internet host (i.e. the same IP address)",
            input=ReverseIpInput(),
            output=ReverseIpOutput(),
        )

    def run(self, params={}):
        params = insightconnect_plugin_runtime.helper.clean_dict(params)
        response = make_request(self.connection.api.reverse_ip, **params)
        return response
