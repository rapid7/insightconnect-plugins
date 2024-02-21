import insightconnect_plugin_runtime
from .schema import WhoisHistoryInput, WhoisHistoryOutput, Input, Output, Component

# Custom imports below
from komand_domaintools.util import util


class WhoisHistory(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="whois_history",
            description=Component.DESCRIPTION,
            input=WhoisHistoryInput(),
            output=WhoisHistoryOutput(),
        )

    def run(self, params={}):
        query = params.get(Input.DOMAIN)
        response = util.make_request(self.connection.api.whois_history, query)
        return response
