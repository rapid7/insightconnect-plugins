import insightconnect_plugin_runtime
from .schema import SubmitFileInput, SubmitFileOutput, Input, Output, Component

# Custom imports below
import base64
from copy import copy


class SubmitFile(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="submit_file",
            description=Component.DESCRIPTION,
            input=SubmitFileInput(),
            output=SubmitFileOutput(),
        )

    def run(self, params={}):
        self.request = copy(self.connection.api.request)
        self.request.url, self.request.method = f"{self.request.url}/v1/submit/new/", "POST"

        platform = params.get(Input.PLATFORM)
        detail = params.get(Input.DETAIL)
        premium = str(params.get(Input.USE_PREMIUM_SANDBOX)).lower()
        classification = params.get(Input.CLASSIFICATION, "private")
        f = params.get(Input.FILE)

        data = {
            "report_radio-platform": platform,
            "use_premium_sandbox": premium,
            "report_radio-classification": classification,
            "detail": detail,
        }

        file_bytes = base64.b64decode(f["content"])
        self.request.files = {"file": (f["filename"], file_bytes)}
        self.request.data = data
        self.logger.info(f"Submitting file to {self.request.url}")
        response_data = self.connection.api.send(self.request)

        reports = []
        for os in response_data.get("reports", {}).keys():
            report = response_data.get("reports", {}).get(os)
            report["platform"] = os
            reports.append(report)
        return {Output.SUCCESS: response_data.get("success"), Output.REPORTS: reports}
