import insightconnect_plugin_runtime
from .schema import DomainLookupInput, DomainLookupOutput, Input, Output, Component
from icon_rdap.util.helpers import extract_nameservers, parse_entities, return_non_empty, extract_public_ids


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

        self.logger.info(f"[ACTION LOG] Getting information for domain: {domain}")
        domain_result = self.connection.rdap_client.domain_lookup(domain=domain)
        self.logger.info(f"[ACTION LOG] Domain result: {domain_result}\n")
        parsed_entities = parse_entities(domain_result.get("entities", []))

        return return_non_empty(
            {
                Output.NAME: domain_result.get("ldhName"),
                Output.REGISTRYDOMAINID: domain_result.get("handle"),
                Output.STATUS: domain_result.get("status"),
                Output.PUBLICIDS: domain_result.get("publicIds", []) + extract_public_ids(parsed_entities),
                Output.ENTITIES: parsed_entities,
                Output.EVENTS: domain_result.get("events", []),
                Output.NAMESERVERS: extract_nameservers(domain_result.get("nameservers", [])),
                Output.SECUREDNS: domain_result.get("secureDNS"),
                Output.VARIANTS: domain_result.get("variants", []),
            }
        )
