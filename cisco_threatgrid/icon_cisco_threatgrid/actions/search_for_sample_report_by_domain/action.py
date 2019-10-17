import komand
from komand.exceptions import PluginException
from komand.exceptions import ConnectionTestException
from .schema import SearchForSampleReportByDomainInput, SearchForSampleReportByDomainOutput, Input, Output, Component
# Custom imports below
import json


class SearchForSampleReportByDomain(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_for_sample_report_by_domain',
                description=Component.DESCRIPTION,
                input=SearchForSampleReportByDomainInput(),
                output=SearchForSampleReportByDomainOutput())

    def run(self, params={}):
        domain = params.get(Input.DOMAIN)

        domain_filename = domain + "_.url"
        result = self.connection.api.search_domain(
            q=domain_filename
        )

        # Custom error handler for action
        try:
            results = result.get("data").get("items")
            if len(results) < 1:
                raise PluginException(cause=f"Could not find sample with domain {domain}",
                                      assistance=f"Please check your input domain and verify it matches the sample "
                                                 f"filename. It should look exactly like \'{domain_filename}\'")
        except json.JSONDecodeError as e:
            raise PluginException(
                preset=ConnectionTestException.Preset.INVALID_JSON,
                data=results.text
            )

        result_object = results[0].get("item")

        return {Output.SAMPLE_REPORT: komand.helper.clean(result_object)}
