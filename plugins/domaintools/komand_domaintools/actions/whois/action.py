import insightconnect_plugin_runtime
from .schema import WhoisInput, WhoisOutput, Input, Output, Component

# Custom imports below
from komand_domaintools.util import util


class Whois(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="whois",
            description=Component.DESCRIPTION,
            input=WhoisInput(),
            output=WhoisOutput(),
        )

    def run(self, params={}):
        query = params.get(Input.QUERY)
        response = util.make_request(self.connection.api.whois, query)
        return response
