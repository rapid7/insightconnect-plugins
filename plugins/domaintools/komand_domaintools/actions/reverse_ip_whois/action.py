import insightconnect_plugin_runtime
from .schema import ReverseIpWhoisInput, ReverseIpWhoisOutput, Input, Output, Component

# Custom imports below
from komand_domaintools.util import util


class ReverseIpWhois(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="reverse_ip_whois",
            description=Component.DESCRIPTION,
            input=ReverseIpWhoisInput(),
            output=ReverseIpWhoisOutput(),
        )

    def run(self, params={}):
        params = insightconnect_plugin_runtime.helper.clean_dict(params)
        response = util.make_request(self.connection.api.reverse_ip_whois, **params)
        return response
