import komand

from .schema import LookupDomainInput, LookupDomainOutput, Input
from komand.exceptions import PluginException
from urllib.parse import urlparse


class LookupDomain(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="lookup_domain",
            description="This action is used to return information about a specific domain entry",
            input=LookupDomainInput(),
            output=LookupDomainOutput(),
        )

    def run(self, params={}):
        try:
            original_domain = params.get(Input.DOMAIN)
            domain = self.get_domain(original_domain)
            comment = params.get(Input.COMMENT)
            fields = [
                "analystNotes",
                "counts",
                "enterpriseLists",
                "entity",
                "intelCard",
                "metrics",
                "relatedEntities",
                "risk",
                "sightings",
                "threatLists",
                "timestamps",
            ]

            if not comment:
                comment = None
            self.logger.info(f"Looking for: {domain}")
            domain_report = self.connection.client.lookup_domain(domain, fields=fields, comment=comment)
            if domain_report.get("warnings", False):
                self.logger.warning(f"Warning: {domain_report.get('warnings')}")
            clean_report = komand.helper.clean(domain_report["data"])
            return clean_report
        except Exception as e:
            raise PluginException(
                cause="Recorded Future did not return results.",
                assistance="This either indicates a malformed URL, or that the URL was not found in Recorded Future.",
                data=f"\nDomain input: {original_domain}\n Exception:\n{e}",
            )

    def get_domain(self, original_domain):
        stripped = urlparse(original_domain).netloc  # This returns null if it's not a URL
        if not stripped:
            stripped = original_domain.replace("https://", "").replace("http://", "").split("/")[0]
        return stripped
