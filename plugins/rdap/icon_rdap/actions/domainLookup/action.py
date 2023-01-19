import insightconnect_plugin_runtime
from .schema import DomainLookupInput, DomainLookupOutput, Input, Output, Component
from icon_rdap.util.api import RdapAPI
from icon_rdap.util.helpers import convert_keys_to_camel


class DomainLookup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="domainLookup",
            description=Component.DESCRIPTION,
            input=DomainLookupInput(),
            output=DomainLookupOutput(),
        )

    def run(self, params={}):
        domain = params.get(Input.DOMAIN)
        self.logger.info(f"[ACTION LOG] Getting information for domain: {domain} .\n")

        domain_result = RdapAPI(logger=self.logger).domain_lookup(domain=domain)
        self.logger.info(f"[ACTION LOG] Domain result: {domain_result}\n")

        return {Output.RESULTS: convert_keys_to_camel(domain_result)}
