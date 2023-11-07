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
        cve = params.get(Input.CVE, None)
        hostname = params.get(Input.HOSTNAME, None)
        source = params.get(Input.SOURCE)
        ip_address = params.get(Input.IP_ADDRESS)
        risk_score = params.get(Input.RISK_SCORE)
        site_id = params.get(Input.SITE_ID, None)

        x = []
        if cve:
            x.append(
                {
                    "field": "cve",
                    "operator": "is",
                    "value": cve,
                }
            )
        if hostname:
            x.append(
                {
                    "field": "host-name",
                    "operator": "is",
                    "value": hostname,
                },
            )

        if ip_address:
            x.append(
                {
                    "field": "ip-address",
                    "operator": "is",
                    "value": ip_address,
                }
            )
        if risk_score:
            x.append(
                {
                    "field": "risk-score",
                    "operator": "is",
                    "value": risk_score,
                }
            )
        if site_id:
            x.append(
                {
                    "field": "site-id",
                    "operator": "is",
                    "value": site_id,
                }
            )
        z = {"filters": x, "match": "any"}

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
                endpoint_asset_search = Asset.search(self.connection.console_url)
                endpoint = Asset.assets(self.connection.console_url, last_id + 1)

                asset_search_response = resource_helper.resource_request(
                    endpoint=endpoint_asset_search, method="post", payload=z
                )
                try:
                    asset_assets_response = resource_helper.resource_request(endpoint=endpoint, method="get")
                except Exception:
                    break

                endpoint = Asset.asset_vulnerability_solution(self.connection.console_url, last_id + 1, "???")
                try:
                    vuln_response = resource_helper.resource_request(endpoint=endpoint, method="get")
                except Exception:
                    break

                vuln_data = vuln_response.get("resources")[0]
                last_id += 1

                self.send(
                    {
                        Output.ASSET_ID: asset_assets_response.get("id"),
                        Output.HOSTNAME: asset_assets_response.get("hostName"),
                        Output.IP: asset_assets_response.get("ip"),
                        Output.NEXPOSE_ID: "???",
                        Output.SOFTWARE_UPDATE_ID: vuln_data.get("id"),
                        Output.SOLUTION_ID: "solution_id",
                        Output.SOLUTION_SUMMARY: "solution_summary",
                        Output.VULNERABILITY_ID: "vulnerability_id",
                    }
                )

            time.sleep(params.get(Input.INTERVAL) * 60)
