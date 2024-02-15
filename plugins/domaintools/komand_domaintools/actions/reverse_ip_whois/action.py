import insightconnect_plugin_runtime

from .schema import ReverseIpWhoisInput, ReverseIpWhoisOutput
from ...util.util import make_request


class ReverseIpWhois(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="reverse_ip_whois",
            description="Provides a list of IP network ranges with Whois records that match a specific query",
            input=ReverseIpWhoisInput(),
            output=ReverseIpWhoisOutput(),
        )

    def run(self, params={}):
        params = insightconnect_plugin_runtime.helper.clean_dict(params)
        response = make_request(self.connection.api.reverse_ip_whois, **params)
        return response
