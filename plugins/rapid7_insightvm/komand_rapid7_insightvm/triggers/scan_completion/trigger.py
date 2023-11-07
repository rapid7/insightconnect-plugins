import insightconnect_plugin_runtime
import time
from .schema import ScanCompletionInput, ScanCompletionOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightvm.util.endpoints import Scan, Asset, VulnerabilityResult
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

        # Build API call
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        endpoint = Scan.scans(self.connection.console_url)

        # Get ALL scans and handle pagination - find last/latest completed scan ID
        response = resource_helper.paged_resource_request(endpoint=endpoint, method="get", params={"sort": "id,desc"})
        last_id = 0
        for resp in response:
            if resp["id"] > last_id:
                last_id = resp["id"]

        while True:
            while True:
                endpoint = Asset.assets(self.connection.console_url, last_id + 1)

                try:
                    asset_response = resource_helper.resource_request(endpoint=endpoint, method="get")
                except Exception:
                    break

                # Placeholders for now - Basically check for input and
                # if it is in response
                if ip_address and ip_address in asset_response.get('ip'):
                    continue

                if risk_score and risk_score in asset_response.get('riskScore'):
                    continue

                if hostname and hostname in asset_response.get('hostName'):
                    continue

                if source and source in asset_response.get('hostNames')[0].get('source'):
                    continue

                # Cannot find asset_group, cve or site_id from Get Asset By ID.
                # Next, run GET Asset Vulnerabilities to retrieve vulnerability IDs
                endpoint = VulnerabilityResult.vulnerabilities_for_asset(self.connection.console_url, last_id + 1)
                try:
                    asset_vuln_response = resource_helper.resource_request(endpoint=endpoint, method="get")
                except Exception:
                    break

                # Add all the IDs into a list
                vulnerability_ids = []
                for i in asset_vuln_response:
                    vulnerability_ids.append(i.get('id'))

                # Next, Get Asset Vulnerability Solution by vulnerability ID
                for vulnerability_id in vulnerability_ids:
                    endpoint = Asset.asset_vulnerability_solution(self.connection.console_url, last_id + 1, vuln_id)
                    try:
                        solution_response = resource_helper.resource_request(endpoint=endpoint, method="get")
                    except Exception:
                        break

                    solution_data = solution_response.get('resources')[0]

                    self.send(
                        {
                            Output.ASSET_ID: asset_response.get("id"),
                            Output.HOSTNAME: asset_response.get("hostName"),
                            Output.IP: asset_response.get("ip"),
                            Output.NEXPOSE_ID: "",
                            Output.SOFTWARE_UPDATE_ID: "",
                            Output.SOLUTION_ID: solution_data.get('id'),
                            Output.SOLUTION_SUMMARY: solution_data.get('summary').get('text'),
                            Output.VULNERABILITY_ID: vulnerability_id,
                        }
                    )
                last_id += 1

            time.sleep(params.get(Input.INTERVAL) * 60)
