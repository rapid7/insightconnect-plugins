import komand
from komand.exceptions import PluginException
from komand.exceptions import ConnectionTestException
from .schema import SearchForSampleReportByDomainInput, SearchForSampleReportByDomainOutput, Input, Output, Component
# Custom imports below
import json
from urllib.parse import urlparse

class SearchForSampleReportByDomain(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_for_sample_report_by_domain',
                description=Component.DESCRIPTION,
                input=SearchForSampleReportByDomainInput(),
                output=SearchForSampleReportByDomainOutput())

    def run(self, params={}):
        in_domain = params.get(Input.DOMAIN)
        domain = urlparse(in_domain).netloc

        if not domain: # url parse couldn't make sense of the input, use what the user gave us.
            domain = in_domain

        self.logger.info(f"Searching for domain: {domain}")
        result = self.connection.api.search_domain(
            q=domain
        )

        # Custom error handler for action
        try:
            results = result.get("data").get("items")
        except json.JSONDecodeError:
            raise PluginException(
                preset=ConnectionTestException.Preset.INVALID_JSON,
                data=str(result)
            )

        if results:
            result_object = results[0].get("item")
        else:
            result_object = {"status": f"Report not found for domain: {domain}"}

        return {Output.SAMPLE_REPORT: komand.helper.clean(result_object)}
