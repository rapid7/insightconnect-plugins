import komand
from .schema import GetSandboxReportInput, GetSandboxReportOutput, Input, Output, Component

# Custom imports below
from copy import copy
from komand.exceptions import PluginException


class GetSandboxReport(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_sandbox_report',
                description=Component.DESCRIPTION,
                input=GetSandboxReportInput(),
                output=GetSandboxReportOutput())

    def run(self, params={}):
        self.request = copy(self.connection.request)
        report_id = params.get(Input.REPORT_ID)
        self.request.url, self.request.method = f"{self.request.url}/submit/{report_id}/report/", "GET"
        self.logger.info(f"Submitting URL to {self.request.url}")
        response = self.connection.session.send(self.request.prepare(), verify=self.request.verify)

        if response.status_code not in range(200, 299):
            raise PluginException(cause="Received %d HTTP status code from ThreatStream." % response.status_code,
                                  assistance="Please verify your ThreatStream server status and try again. "
                                             "If the issue persists please contact support. "
                                             "Server response was: %s" % response.text)
        js = response.json()

        try:
            domains_detail = js['results']['network']['domains']
            info = js['results']['info']
            signatures = js['results']['signatures']
            screenshots = js['results']['screenshots']
        except KeyError:
            raise PluginException(cause='The output did not contain expected keys.',
                                  assistance='Contact support for help.',
                                  data=js)

        domains = []
        for domain in domains_detail:
            for key, value in domain.items():
                if key == 'domain':
                    domains.append(value)

        report = {'signatures': signatures,
                  'screenshots': screenshots,
                  'info': info,
                  'domains': domains
                  }

        return {Output.SANDBOX_REPORT: report}
