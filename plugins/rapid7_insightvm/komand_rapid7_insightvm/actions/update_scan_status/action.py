import insightconnect_plugin_runtime
from .schema import UpdateScanStatusInput, UpdateScanStatusOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class UpdateScanStatus(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_scan_status",
            description="Update the status of a scan (pause, resume, stop)",
            input=UpdateScanStatusInput(),
            output=UpdateScanStatusOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        scan_id = params.get("id")
        status = params.get("status")
        endpoint = endpoints.Scan.scan_status(self.connection.console_url, scan_id, status)
        response = resource_helper.resource_request(endpoint=endpoint, method="post")

        return response
