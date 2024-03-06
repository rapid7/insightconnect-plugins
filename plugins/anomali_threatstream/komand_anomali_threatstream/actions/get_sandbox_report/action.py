import insightconnect_plugin_runtime
from .schema import GetSandboxReportInput, GetSandboxReportOutput, Input, Output, Component

# Custom imports below
from copy import copy
from insightconnect_plugin_runtime.exceptions import PluginException


class GetSandboxReport(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_sandbox_report",
            description=Component.DESCRIPTION,
            input=GetSandboxReportInput(),
            output=GetSandboxReportOutput(),
        )

    def run(self, params={}):
        self.request = copy(self.connection.api.request)
        report_id = params.get(Input.REPORT_ID)
        self.request.url, self.request.method = (
            f"{self.request.url}/submit/{report_id}/report/",
            "GET",
        )
        self.logger.info(f"Submitting URL to {self.request.url}")
        response_data = self.connection.api.send(self.request)

        try:
            domains_detail = response_data["results"]["network"]["domains"]
            info = response_data["results"]["info"]
            signatures = response_data["results"]["signatures"]
            screenshots = response_data["results"]["screenshots"]
        except KeyError:
            raise PluginException(
                cause="The output did not contain expected keys.",
                assistance="Contact support for help.",
                data=response_data,
            )

        domains = []
        for domain in domains_detail:
            for key, value in domain.items():
                if key == "domain":
                    domains.append(value)

        report = {
            "signatures": signatures,
            "screenshots": screenshots,
            "info": info,
            "domains": domains,
        }
        return {Output.SANDBOX_REPORT: report}
