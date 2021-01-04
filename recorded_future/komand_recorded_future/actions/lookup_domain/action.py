import komand

from .schema import LookupDomainInput, LookupDomainOutput, Input
from komand.exceptions import PluginException


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
            domain = params.get(Input.DOMAIN)
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
                "timestamps"
            ]

            if not comment:
                comment = None
            domain_report = self.connection.client.lookup_domain(domain, fields=fields, comment=comment)
            if domain_report.get("warnings", False):
                self.logger.warning(f"Warning: {domain_report.get('warnings')}")
            return komand.helper.clean(domain_report["data"])
        except Exception as e:
            PluginException(cause=f"Error: {e}", assistance="Review exception")
