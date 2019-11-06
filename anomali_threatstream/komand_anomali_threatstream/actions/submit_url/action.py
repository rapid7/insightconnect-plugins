import komand
from komand.exceptions import PluginException
from .schema import SubmitUrlInput, SubmitUrlOutput, Input, Output, Component
# Custom imports below
from copy import copy


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
        premium = params.get(Input.USE_PREMIUM_SANDBOX)
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

        if response.status_code == 400:
            raise PluginException(cause="Received an HTTP status code 400 from Anamoli",
                                  data=response.text)

        js = response.json()
        reports = []
        for os in js['reports'].keys():
            report = js['reports'][os]
            report['platform'] = os
            reports.append(report)
        return {Output.SUCCESS: js['success'], Output.REPORTS: reports}
