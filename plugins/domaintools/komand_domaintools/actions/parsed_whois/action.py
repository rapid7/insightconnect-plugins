import insightconnect_plugin_runtime
from .schema import ParsedWhoisInput, ParsedWhoisOutput, Input, Output, Component

# Custom imports below
from komand_domaintools.util import util


class ParsedWhois(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="parsed_whois",
            description=Component.DESCRIPTION,
            input=ParsedWhoisInput(),
            output=ParsedWhoisOutput(),
        )

    def run(self, params={}):
        query = params.get(Input.DOMAIN)
        response = util.make_request(self.connection.api.parsed_whois, query)
        return response
