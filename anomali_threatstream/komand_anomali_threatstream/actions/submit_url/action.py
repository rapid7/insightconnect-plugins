import komand
from .schema import SubmitUrlInput, SubmitUrlOutput, Input, Output, Component

# Custom imports below
from copy import copy
from json.decoder import JSONDecodeError
from komand.exceptions import PluginException


class SubmitUrl(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='submit_url',
                description=Component.DESCRIPTION,
                input=SubmitUrlInput(),
                output=SubmitUrlOutput())

    def run(self, params={}):
        self.request = copy(self.connection.request)
        self.request.url, self.request.method = self.request.url + "/submit/new/", "POST"

        platform = params.get(Input.PLATFORM)
        detail = params.get(Input.DETAIL)
        premium = str(params.get(Input.USE_PREMIUM_SANDBOX)).lower()
        classification = params.get(Input.CLASSIFICATION, 'private')
        url = params.get(Input.URL)

        data = {
            "report_radio-platform": platform,
            "use_premium_sandbox": premium,
            "report_radio-classification": classification,
            "detail": detail,
            "report_radio-url": url
        }

        self.request.data = data
        self.logger.info(f"Submitting URL to {self.request.url}")
        response = self.connection.session.send(self.request.prepare(), verify=self.request.verify)

        if response.status_code not in range(200, 299):
            raise PluginException(cause="Received %d HTTP status code from ThreatStream." % response.status_code,
                                  assistance="Please verify your ThreatStream server status and try again. "
                                             "If the issue persists please contact support. "
                                             "Server response was: %s" % response.text)
        try:
            js = response.json()
        except JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)

        reports = []
        for os in js['reports'].keys():
            report = js['reports'][os]
            report['platform'] = os
            reports.append(report)
        return {Output.SUCCESS: js['success'], Output.REPORTS: reports}
