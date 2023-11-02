import insightconnect_plugin_runtime
import time
from .schema import ScanCompletionInput, ScanCompletionOutput, Input, Output, Component

# Custom imports below


class ScanCompletion(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="scan_completion",
            description=Component.DESCRIPTION,
            input=ScanCompletionInput(),
            output=ScanCompletionOutput(),
        )

    def run(self, params={}):
        # END INPUT BINDING - DO NOT REMOVE
        # Input retrieval
        asset_group = params.get(Input.ASSET_GROUP)
        cve = params.get(Input.CVE)
        hostname = params.get(Input.HOSTNAME)
        source = params.get(Input.SOURCE)
        ip_address = params.get(Input.IP_ADDRESS)
        risk_score = params.get(Input.RISK_SCORE)
        site_id = params.get(Input.SITE_ID)

        # Output mapping
        output_map = {
            Output.ASSET_ID: "asset_id",
            Output.HOSTNAME: "hostname",
            Output.IP: "ip",
            Output.NEXPOSE_ID: "nexpose_id",
            Output.SOFTWARE_UPDATE_ID: "software_update_id",
            Output.SOLUTION_ID: "solution_id",
            Output.SOLUTION_SUMMARY: "solution_summary",
            Output.VULNERABILITY_ID: "vulnerability_id",
        }

        response = ""

        while True:
            # TODO: Implement trigger functionality
            self.send({output_map: response})
            time.sleep(5)
