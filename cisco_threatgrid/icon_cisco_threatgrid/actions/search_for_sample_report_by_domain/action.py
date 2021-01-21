import komand
from komand.exceptions import PluginException
from .schema import SearchForSampleReportByDomainInput, SearchForSampleReportByDomainOutput, Input, Output, Component

# Custom imports below


class SearchForSampleReportByDomain(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_for_sample_report_by_domain",
            description=Component.DESCRIPTION,
            input=SearchForSampleReportByDomainInput(),
            output=SearchForSampleReportByDomainOutput(),
        )

    def run(self, params={}):
        domain = params.get(Input.DOMAIN)
        self.logger.info(f"Searching for domain: {domain}")
        result = self.connection.api.search_domain(domain=domain)
        try:
            results = result.get("data").get("items")[0].get("item")
        except IndexError:
            raise PluginException(
                cause=f"Report not found for domain: {domain}.",
                assistance="Please check your input.\n",
                data=str(result),
            )
        except AttributeError:
            raise PluginException(
                cause=f"Could not find sample for domain {domain}.",
                assistance="Please check your input.\n",
                data=str(result),
            )
        return {Output.SAMPLE_REPORT: komand.helper.clean(results)}
