import insightconnect_plugin_runtime
from .schema import ReverseIpInput, ReverseIpOutput, Input, Output, Component

# Custom imports below
from komand_domaintools.util import util


class ReverseIp(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="reverse_ip",
            description=Component.DESCRIPTION,
            input=ReverseIpInput(),
            output=ReverseIpOutput(),
        )

    def run(self, params={}):
        params = insightconnect_plugin_runtime.helper.clean_dict(params)
        response = util.make_request(self.connection.api.reverse_ip, **params)
        return response
