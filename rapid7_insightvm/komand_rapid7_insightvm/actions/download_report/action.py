import komand
from .schema import DownloadReportInput, DownloadReportOutput
# Custom imports below
import requests
from komand_rapid7_insightvm.util import endpoints
import base64


class DownloadReport(komand.Action):
    _ERRORS = {
        401: "Unauthorized",
        404: "Not Found",
        500: "Internal Server Error",
        503: "Service Unavailable",
        000: "Unknown Status Code"
    }

    def __init__(self):
        super(self.__class__, self).__init__(
            name='download_report',
            description='Returns the contents of a generated report',
            input=DownloadReportInput(),
            output=DownloadReportOutput())

    def run(self, params={}):
        report_id = params.get("id")
        instance_id = params.get("instance")
        endpoint = endpoints.Report.download(self.connection.console_url, report_id, instance_id)
        self.logger.info("Using %s ..." % endpoint)

        try:
            response = self.connection.session.get(url=endpoint, verify=False)
        except requests.RequestException as e:
            self.logger.error(e)
            raise

        else:
            if response.status_code in [200, 201]:  # 200 is documented, 201 is undocumented
                report = base64.b64encode(response.content).decode()

                return {"report": report}
            else:
                try:
                    reason = response.json()["message"]
                except KeyError:
                    reason = "Unknown error occurred. Please contact support or try again later."

                status_code_message = self._ERRORS.get(response.status_code, self._ERRORS[000])
                self.logger.error("{status} ({code}): {reason}".format(status=status_code_message,
                                                                       code=response.status_code,
                                                                       reason=reason))
                raise Exception
