import insightconnect_plugin_runtime

from .schema import WhoisHistoryInput, WhoisHistoryOutput
from ...util.util import make_request


class WhoisHistory(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="whois_history",
            description="Provides a list of historic Whois records for a domain name",
            input=WhoisHistoryInput(),
            output=WhoisHistoryOutput(),
        )

    def run(self, params={}):
        query = params.get("domain")
        response = make_request(self.connection.api.whois_history, query)
        return response
