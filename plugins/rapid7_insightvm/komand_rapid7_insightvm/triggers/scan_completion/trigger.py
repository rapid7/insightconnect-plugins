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
        scans_endpoint = Scan.scans(self.connection.console_url)

        # Get ALL scans and handle pagination - find last/latest completed scan ID
        response = resource_helper.resource_request(endpoint=scans_endpoint, method="get", params={"sort": "id,desc"})
        last_id = 0
        # print(response)
        if response.get("resources")[0].get("id") > last_id:
            last_id = response.get("resources")[0].get("id")

        while True:
            response = resource_helper.resource_request(endpoint=scans_endpoint, method="get",
                                                        params={"sort": "id,desc"})

            if response.get("resources")[0].get("id") >= last_id:
                continue

            while True:

                if site_id and site_id in response[0]["siteId"]:
                    continue

                endpoint = Asset.assets(self.connection.console_url, last_id)

                try:
                    asset_response = resource_helper.resource_request(endpoint=endpoint, method="get")
                except Exception:
                    break

                # Placeholders for now - Basically check for input and
                # if it is in response
                if ip_address and ip_address in asset_response.get("ip"):
                    continue

                # if risk_score and risk_score in asset_response.get('riskScore'):
                #     continue

                # Hostname is not always present so we need to handle it.
                if not asset_response.get("hostName"):
                    asset_response["hostName"] = ""
                if not asset_response.get("hostNames"):
                    asset_response["hostNames"] = ""

                if hostname and hostname in asset_response.get("hostName"):
                    continue

                if source and source in asset_response.get("hostNames")[0].get("source"):
                    continue

                # Cannot find asset_group, cve or site_id from Get Asset By ID.
                # Next, run GET Asset Vulnerabilities to retrieve vulnerability IDs
                endpoint = VulnerabilityResult.vulnerabilities_for_asset(self.connection.console_url, last_id)
                try:
                    asset_vuln_response = resource_helper.paged_resource_request(endpoint=endpoint, method="get")
                except Exception:
                    break

                # Add all the vulnerability IDs related to the asset into a list
                vulnerability_ids = []
                # print(f"\n{asset_vuln_response}\n")
                for vulns in asset_vuln_response:
                    vulnerability_ids.append(vulns.get("id"))
                print(f"\n{vulnerability_ids}\n")

                # Next, Get Asset Vulnerability Solution by vulnerability ID
                for vulnerability_id in vulnerability_ids:
                    print(f"\n\n{last_id} + {vulnerability_id}")

                    endpoint = Asset.asset_vulnerability_solution(
                        self.connection.console_url, last_id, vulnerability_id
                    )
                    try:
                        solution_response = resource_helper.resource_request(endpoint=endpoint, method="get")
                    except Exception:
                        break

                    try:
                        solution_data = solution_response.get("resources")[0]
                    except IndexError:
                        break

                    self.send(
                        {
                            Output.ASSET_ID: asset_response.get("id"),
                            Output.HOSTNAME: asset_response.get("hostName"),
                            Output.IP: asset_response.get("ip"),
                            Output.SOLUTION_ID: self.strip_msft_id(solution_data.get("id")),
                            Output.SOLUTION_SUMMARY: solution_data.get("summary").get("text"),
                            Output.VULNERABILITY_ID: vulnerability_id,
                        }
                    )
                last_id += 1

            time.sleep(params.get(Input.INTERVAL) * 10)

    @staticmethod
    def strip_msft_id(solution_id: str) -> str:
        """
        Helper method to strip solution IDs specific to microsoft IDs
        to return a useful solution ID for sccm

        :param solution_id: Solution ID
        :return: Regular solution ID or stripped solution ID
        """

        list_x = solution_id.split("-")

        if list_x[0] == "msft":
            return "-".join(list_x[2:])
        else:
            return solution_id
