import insightconnect_plugin_runtime

from .schema import WhoisInput, WhoisOutput
from ...util.util import make_request


class Whois(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="whois",
            description="Provides the ownership record for a domain name or IP address with basic registration details",
            input=WhoisInput(),
            output=WhoisOutput(),
        )

    def run(self, params={}):
        query = params.get("query")
        response = make_request(self.connection.api.whois, query)
        return response
