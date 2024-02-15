import insightconnect_plugin_runtime

from .schema import ParsedWhoisInput, ParsedWhoisOutput
from ...util.util import make_request


class ParsedWhois(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="parsed_whois",
            description="Provides parsed information extracted from the raw Whois record",
            input=ParsedWhoisInput(),
            output=ParsedWhoisOutput(),
        )

    def run(self, params={}):
        query = params.get("domain")
        response = make_request(self.connection.api.parsed_whois, query)
        return response
