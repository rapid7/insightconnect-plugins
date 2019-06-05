import komand
from .schema import GetScanInput, GetScanOutput
# Custom imports below
import requests
from komand_rapid7_insightvm.util import endpoints


class GetScan(komand.Action):

    _ERRORS = {
        400: "Bad Request",
        401: "Unauthorized",
        500: "Internal Server Error",
        503: "Service Unavailable",
        000: "Unknown Status Code"
    }

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_scan',
                description='Gets the status of a scan',
                input=GetScanInput(),
                output=GetScanOutput())

    def run(self, params={}):
        scan_id = params.get("scan_id")
        endpoint = endpoints.Scan.scans(self.connection.console_url, scan_id)
        self.logger.info("Using %s ..." % endpoint)

        try:
            response = self.connection.session.get(url=endpoint, verify=False)
        except requests.RequestException as e:
            self.logger.error(e)
            raise

        else:
            if response.status_code in [200, 201]:  # 200 is documented, 201 is undocumented
                scan_details = response.json()

                return scan_details
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
