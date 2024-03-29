import insightconnect_plugin_runtime
from .schema import DownloadReportInput, DownloadReportOutput, Input, Output

# Custom imports below
import requests
from komand_rapid7_insightvm.util import endpoints
import base64
import json
from insightconnect_plugin_runtime.exceptions import PluginException


class DownloadReport(insightconnect_plugin_runtime.Action):
    _ERRORS = {
        401: "Unauthorized",
        404: "Not Found",
        500: "Internal Server Error",
        503: "Service Unavailable",
        000: "Unknown Status Code",
    }

    def __init__(self):
        super(self.__class__, self).__init__(
            name="download_report",
            description="Returns the contents of a generated report",
            input=DownloadReportInput(),
            output=DownloadReportOutput(),
        )

    def run(self, params={}):
        report_id = params.get(Input.ID, "")
        instance_id = params.get(Input.INSTANCE, "")

        endpoint = endpoints.Report.download(self.connection.console_url, report_id, instance_id)
        self.logger.info(f"Using {endpoint}")

        try:
            response = self.connection.session.get(
                url=endpoint, verify=self.connection.ssl_verify, headers={"Accept": "application/pdf"}
            )
        except requests.RequestException as error:
            self.logger.error(error)
            raise

        else:
            if response.status_code in [200, 201]:  # 200 is documented, 201 is undocumented
                report = base64.b64encode(response.content).decode()

                return {Output.REPORT: report}
            else:
                reason = ""
                try:
                    reason = response.json()["message"]
                except KeyError:
                    reason = "Unknown error occurred. Please contact support or try again later."
                except json.decoder.JSONDecodeError:
                    raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=reason.text)

                status_code_message = self._ERRORS.get(response.status_code, self._ERRORS[000])
                self.logger.error(f"{status_code_message} ({response.status_code}): {reason}")
                raise PluginException(preset=PluginException.Preset.UNKNOWN)
