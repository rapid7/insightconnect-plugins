import insightconnect_plugin_runtime
from .schema import DomainsInput, DomainsOutput, Input, Output

# Custom imports below


class Domains(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="domains",
            description="To gather the lists of domains already added to the shared customer’s domain list, run a GET request against the domains endpoint of the API",
            input=DomainsInput(),
            output=DomainsOutput(),
        )

    def run(self, params={}):

        domains = self.connection.client.get_domains()

        return {Output.DOMAINS: domains}
