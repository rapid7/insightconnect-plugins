import insightconnect_plugin_runtime
from .schema import SubmitUrlInput, SubmitUrlOutput, Input, Output, Component

# Custom imports below
from copy import copy
from json.decoder import JSONDecodeError
from insightconnect_plugin_runtime.exceptions import PluginException


class SubmitUrl(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="submit_url",
            description=Component.DESCRIPTION,
            input=SubmitUrlInput(),
            output=SubmitUrlOutput(),
        )

    def run(self, params={}):
        self.request = copy(self.connection.request)
        self.request.url, self.request.method = self.request.url + "/submit/new/", "POST"

        platform = params.get(Input.PLATFORM)
        detail = params.get(Input.DETAIL)
        premium = str(params.get(Input.USE_PREMIUM_SANDBOX)).lower()
        classification = params.get(Input.CLASSIFICATION, "private")
        url = params.get(Input.URL)

        data = {
            "report_radio-platform": platform,
            "use_premium_sandbox": premium,
            "report_radio-classification": classification,
            "detail": detail,
            "report_radio-url": url,
        }

        self.request.data = data
        self.logger.info(f"Submitting URL to {self.request.url}")
        response_data = self.connection.send(self.request)

        reports = []
        for os in response_data["reports"].keys():
            report = response_data["reports"][os]
            report["platform"] = os
            reports.append(report)
        return {Output.SUCCESS: response_data["success"], Output.REPORTS: reports}
