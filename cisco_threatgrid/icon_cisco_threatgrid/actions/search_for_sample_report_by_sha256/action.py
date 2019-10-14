import komand
from komand.exceptions import PluginException
from .schema import SearchForSampleReportBySha256Input, SearchForSampleReportBySha256Output, Input, Output, Component
# Custom imports below
import requests


class SearchForSampleReportBySha256(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_for_sample_report_by_sha256',
                description=Component.DESCRIPTION,
                input=SearchForSampleReportBySha256Input(),
                output=SearchForSampleReportBySha256Output())

    def run(self, params={}):
        sha256 = params.get(Input.SHA256)

        self.logger.info(f"Looking for sample with sha246 filename: {sha256}")
        result = self.connection.api.search_sha256(q=sha256)

        try:
            results = result.get("data").get("items")
        except requests.HTTPError as e:
            raise PluginException(cause="ThreatGrid query for domain failed.",
                                  assistance=f"ThreatGrid query failed, check your API key.\n "
                                  f"Exception returned was: {e} \n"
                                  f"Response returned was: {result.text}")

        if len(results) < 1:
            raise PluginException(cause=f"Could not find sample with sha256 {sha256}.",
                                  assistance=f"Please check your input.")

        # If someone reports a common file or URL, this will return multiple reports. I'm not sure
        # how to narrow down that result by just the hash
        report_list = []
        for result in results:
            report_list.append(result.get("item"))

        return {Output.SAMPLE_REPORT_LIST: komand.helper.clean(report_list)}
