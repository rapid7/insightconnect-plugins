import komand
from komand.exceptions import PluginException
from .schema import (
    SearchForSampleReportBySha256Input,
    SearchForSampleReportBySha256Output,
    Input,
    Output,
    Component,
)

# Custom imports below


class SearchForSampleReportBySha256(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_for_sample_report_by_sha256",
            description=Component.DESCRIPTION,
            input=SearchForSampleReportBySha256Input(),
            output=SearchForSampleReportBySha256Output(),
        )

    def run(self, params={}):
        sha256 = params.get(Input.SHA256)
        self.logger.info(f"Looking for sample with SHA256: {sha256}")
        results = self.connection.api.search_sha256(sha256=sha256)
        try:
            result = results.get("data").get("items")[0]
        except IndexError:
            raise PluginException(
                cause=f"Report not found for SHA256: {sha256}.",
                assistance="Please check your input.\n",
                data=str(results),
            )
        except AttributeError:
            raise PluginException(
                cause=f"Could not find sample with SHA256 {sha256}.",
                assistance="Please check your input.\n",
                data=str(results),
            )
        return {Output.SAMPLE_REPORT_LIST: komand.helper.clean(result)}
