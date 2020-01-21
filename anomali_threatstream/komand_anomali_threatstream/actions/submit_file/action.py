import komand
from komand.exceptions import PluginException
from .schema import SubmitFileInput, SubmitFileOutput, Input, Output, Component
# Custom imports below
import base64
from copy import copy


class SubmitFile(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='submit_file',
                description=Component.DESCRIPTION,
                input=SubmitFileInput(),
                output=SubmitFileOutput())

    def run(self, params={}):
        self.request = copy(self.connection.request)
        self.request.url, self.request.method = f"{self.request.url}/submit/new/", "POST"

        platform = params.get(Input.PLATFORM)
        detail = params.get(Input.DETAIL)
        premium = str(params.get(Input.USE_PREMIUM_SANDBOX)).lower()
        classification = params.get(Input.CLASSIFICATION, 'private')
        f = params.get(Input.FILE)

        data = {
            "report_radio-platform": platform,
            "use_premium_sandbox": premium,
            "report_radio-classification": classification,
            "detail": detail
        }

        file_bytes = base64.b64decode(f['content'])
        self.request.files = {"file": (f["filename"], file_bytes)}
        self.request.data = data
        self.logger.info(f"Submitting file to {self.request.url}")
        response = self.connection.session.send(self.request.prepare(), verify=self.request.verify)

        if response.status_code == 400:
            raise PluginException(cause="Received a 400 from Anomali",
                                  data=response.text)

        js = response.json()
        reports = []
        for os in js['reports'].keys():
            report = js['reports'][os]
            report['platform'] = os
            reports.append(report)
        return {Output.SUCCESS: js['success'], Output.REPORTS: reports}
