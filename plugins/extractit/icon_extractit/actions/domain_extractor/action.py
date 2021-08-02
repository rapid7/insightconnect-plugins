import insightconnect_plugin_runtime
from .schema import DomainExtractorInput, DomainExtractorOutput, Input, Output, Component

# Custom imports below
from icon_extractit.util.util import Regex
from icon_extractit.util.extractor import extract, clear_domains, strip_subdomains


class DomainExtractor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="domain_extractor",
            description=Component.DESCRIPTION,
            input=DomainExtractorInput(),
            output=DomainExtractorOutput(),
        )

    def run(self, params={}):
        matches = clear_domains(extract(Regex.Domain, params.get(Input.STR), params.get(Input.FILE)))
        if not params.get(Input.SUBDOMAIN):
            matches = strip_subdomains(matches)
        return {Output.DOMAINS: matches}
