import insightconnect_plugin_runtime
from .schema import GetScanInput, GetScanOutput

# Custom imports below
import requests
from komand_rapid7_insightvm.util import endpoints
import json
from insightconnect_plugin_runtime.exceptions import PluginException


class GetScan(insightconnect_plugin_runtime.Action):

    _ERRORS = {
        400: "Bad Request",
        401: "Unauthorized",
        500: "Internal Server Error",
        503: "Service Unavailable",
        000: "Unknown Status Code",
    }

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_scan",
            description="Gets the status of a scan",
            input=GetScanInput(),
            output=GetScanOutput(),
        )

    def run(self, params={}):
        scan_id = params.get("scan_id")
        endpoint = endpoints.Scan.scans(self.connection.console_url, scan_id)
        self.logger.info(f"Using {endpoint}")

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
