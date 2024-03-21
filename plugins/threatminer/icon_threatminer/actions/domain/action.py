import insightconnect_plugin_runtime

from .schema import Component, DomainInput, DomainOutput, Input, Output

# Custom imports below


class Domain(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="domain",
            description=Component.DESCRIPTION,
            input=DomainInput(),
            output=DomainOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        domain = params.get(Input.DOMAIN, "")
        query_type = params.get(Input.QUERY_TYPE, "WHOIS")
        # END INPUT BINDING - DO NOT REMOVE

        return {Output.RESPONSE: self.connection.api_client.domain_lookup(domain, query_type)}
