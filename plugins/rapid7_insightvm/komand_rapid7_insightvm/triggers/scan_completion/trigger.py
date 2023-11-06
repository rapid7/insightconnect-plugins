import insightconnect_plugin_runtime
import time
from .schema import ScanCompletionInput, ScanCompletionOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightvm.util.endpoints import Scan, Asset
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


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
        site_id = params.get(Input.SITE_ID, None)

        # Output mapping
        # output_map = {
        #     Output.ASSET_ID: "asset_id",
        #     Output.HOSTNAME: "hostname",
        #     Output.IP: "ip",
        #     Output.NEXPOSE_ID: "nexpose_id",
        #     Output.SOFTWARE_UPDATE_ID: "software_update_id",
        #     Output.SOLUTION_ID: "solution_id",
        #     Output.SOLUTION_SUMMARY: "solution_summary",
        #     Output.VULNERABILITY_ID: "vulnerability_id",
        # }

        # {
        #     "field": "<field-name>",
        #     "operator": "<operator>",
        #     ["value": < value >,],
        #     ["lower": < value >,],
        #     ["upper": < value >],
        # }

        # Build API call
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        endpoint = Scan.scans(self.connection.console_url)

        # Get ALL scans and handle pagination - find last ID
        response = resource_helper.paged_resource_request(endpoint=endpoint, method="get", params={"sort": "id,desc"})
        last_id = 0
        for resp in response:
            if resp["id"] > last_id:
                last_id = resp["id"]

        while True:
            while True:

                # POST Asset Search endpoint
                # endpoint = Scan.scans(self.connection.console_url, last_id + 1)
                endpoint = Asset.search(self.connection.console_url)

                try:
                    params_dict = {}
                    response = resource_helper.resource_request(endpoint=endpoint, method="post")
                    # response.get('resources')[0].get('id')

                except Exception:
                    break
                last_id += 1

                # Right, so now that we've got our scan result
                # First, we make sure `status == 'finished`
                # From here, we take some identifier and run other API calls on it -
                # - depending on the input filters.
                self.send(response)

            time.sleep(100)
