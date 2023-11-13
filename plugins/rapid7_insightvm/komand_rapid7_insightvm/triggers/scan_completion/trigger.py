import insightconnect_plugin_runtime
import time
from .schema import ScanCompletionInput, ScanCompletionOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightvm.util.endpoints import Scan, Asset, VulnerabilityResult
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests
import uuid
from komand_rapid7_insightvm.util import util
import csv
import io
from typing import List, Dict
from insightconnect_plugin_runtime.exceptions import PluginException


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

        scan_id = 3

        results_from_query = self.get_results_from_query(scan_id)
        asset_id = results_from_query[0].get("asset_id")

        results_from_vuln_query = self.get_vuln_from_asset_id(asset_id)
        results_from_solution_info = self.get_solution_info(asset_id, results_from_vuln_query)

        self.send(
            {
                Output.ASSET_ID: asset_id,
                Output.IP: results_from_query[0].get("ip_address"),
                Output.HOSTNAME: results_from_query[0].get("hostname"),
                Output.SOLUTION_ID: results_from_solution_info[0].get("solution_id"),
                Output.SOLUTION_SUMMARY: results_from_solution_info[0].get("summary"),
                Output.VULNERABILITY_ID: results_from_solution_info[0].get("vulnerability_id"),
            }
        )

    @staticmethod
    def another_query(scan_id):
        return (
            f"SELECT fasvi.scan_id, fasvi.asset_id, da.host_name, da.ip_address, dv.severity, ds.finished "
            f"FROM fact_asset_scan_vulnerability_instance AS fasvi "
            f"JOIN dim_asset da ON (fasvi.asset_id = da.asset_id) "
            f"JOIN dim_vulnerability dv ON (fasvi.vulnerability_id = dv.vulnerability_id) "
            f"JOIN dim_scan ds ON (fasvi.scan_id = ds.scan_id) "
            f"WHERE fasvi.scan_id = {scan_id} "
            f"GROUP BY fasvi.scan_id, fasvi.asset_id, da.host_name, da.ip_address, dv.severity, ds.finished "
            f"ORDER BY ds.finished DESC, dv.severity DESC;"
        )

    def get_results_from_query(self, scan_id: int):
        identifier = uuid.uuid4()

        report_payload = {
            "name": f"Rapid7-InsightConnect-ScanCompletion-{identifier}",
            "format": "sql-query",
            "query": ScanCompletion.another_query(scan_id),
            "version": "2.3.0",
        }

        self.logger.info("Getting report")
        report_contents = util.adhoc_sql_report(self.connection, self.logger, report_payload)

        try:
            csv_report = csv.DictReader(io.StringIO(report_contents["raw"]))
        except Exception as error:
            raise PluginException(
                cause="Error: Failed to process query response while fetching site scans.",
                assistance=f"Exception returned was {error}",
            )

        scans = []
        for row in csv_report:
            site_scan = {
                "asset_id": int(row["asset_id"]),
                "hostname": row["host_name"],
                "ip_address": row["ip_address"],
            }
            scans.append(site_scan)

        print(f"SCHANS: {scans}")
        return scans

    def get_vuln_from_asset_id(self, asset_id: int) -> List[str]:
        vuln_ids = []

        resource_helper = ResourceRequests(self.connection.session, self.logger)

        endpoint = VulnerabilityResult.vulnerabilities_for_asset(self.connection.console_url, asset_id)
        try:
            asset_vuln_response = resource_helper.paged_resource_request(endpoint=endpoint, method="get")
        except Exception:
            raise PluginException()

        for vulnerability in asset_vuln_response:
            vuln_ids.append(vulnerability.get("id"))

        print(f"VULN IDS: {vuln_ids}")
        return vuln_ids

    def get_solution_info(self, asset_id: int, vulnerability_ids):

        vuln_info_list = []
        resource_helper = ResourceRequests(self.connection.session, self.logger)

        for vulnerability_id in vulnerability_ids:
            endpoint = Asset.asset_vulnerability_solution(self.connection.console_url, asset_id, vulnerability_id)
            try:
                solution_response = resource_helper.resource_request(endpoint=endpoint, method="get")
            except Exception:
                raise PluginException()

            info = solution_response.get("resources")[0]

            vuln_info = {
                "summary": info.get("summary").get("text"),
                "solution_id": info.get("id"),
                "vulnerability_id": vulnerability_id,
            }

            vuln_info_list.append(vuln_info)

        print(f"VULN INFO LIST: {vuln_info_list}")
        return vuln_info_list

    # def ignore_this(self):
    #     # Build API call
    #     resource_helper = ResourceRequests(self.connection.session, self.logger)
    #     scans_endpoint = Scan.scans(self.connection.console_url)
    #
    #     # Get ALL scans and handle pagination - find last/latest completed scan ID
    #     response = resource_helper.resource_request(endpoint=scans_endpoint, method="get", params={"sort": "id,desc"})
    #     last_id = 0
    #     # print(response)
    #     if response.get("resources")[0].get("id") > last_id:
    #         last_id = response.get("resources")[0].get("id")
    #
    #     while True:
    #
    #         while True:
    #
    #             if site_id and site_id in response[0]["siteId"]:
    #                 continue
    #
    #             endpoint = Asset.assets(self.connection.console_url, last_id)
    #
    #             try:
    #                 asset_response = resource_helper.resource_request(endpoint=endpoint, method="get")
    #             except Exception:
    #                 break
    #
    #             # Placeholders for now - Basically check for input and
    #             # if it is in response
    #             if ip_address and ip_address in asset_response.get("ip"):
    #                 continue
    #
    #             # if risk_score and risk_score in asset_response.get('riskScore'):
    #             #     continue
    #
    #             # Hostname is not always present so we need to handle it.
    #             if not asset_response.get("hostName"):
    #                 asset_response["hostName"] = ""
    #             if not asset_response.get("hostNames"):
    #                 asset_response["hostNames"] = ""
    #
    #             if hostname and hostname in asset_response.get("hostName"):
    #                 continue
    #
    #             if source and source in asset_response.get("hostNames")[0].get("source"):
    #                 continue
    #
    #             # Cannot find asset_group, cve or site_id from Get Asset By ID.
    #             # Next, run GET Asset Vulnerabilities to retrieve vulnerability IDs
    #             endpoint = VulnerabilityResult.vulnerabilities_for_asset(self.connection.console_url, last_id)
    #             try:
    #                 asset_vuln_response = resource_helper.paged_resource_request(endpoint=endpoint, method="get")
    #             except Exception:
    #                 break
    #
    #             # Add all the vulnerability IDs related to the asset into a list
    #             vulnerability_ids = []
    #             # print(f"\n{asset_vuln_response}\n")
    #             for vulns in asset_vuln_response:
    #                 vulnerability_ids.append(vulns.get("id"))
    #             print(f"\n{vulnerability_ids}\n")
    #
    #             # Next, Get Asset Vulnerability Solution by vulnerability ID
    #             for vulnerability_id in vulnerability_ids:
    #                 print(f"\n\n{last_id} + {vulnerability_id}")
    #
    #                 endpoint = Asset.asset_vulnerability_solution(
    #                     self.connection.console_url, last_id, vulnerability_id
    #                 )
    #                 try:
    #                     solution_response = resource_helper.resource_request(endpoint=endpoint, method="get")
    #                 except Exception:
    #                     break
    #
    #                 try:
    #                     solution_data = solution_response.get("resources")[0]
    #                 except IndexError:
    #                     break
    #
    #                 self.send(
    #                     {
    #                         Output.ASSET_ID: asset_response.get("id"),
    #                         Output.HOSTNAME: asset_response.get("hostName"),
    #                         Output.IP: asset_response.get("ip"),
    #                         Output.SOLUTION_ID: self.strip_msft_id(solution_data.get("id")),
    #                         Output.SOLUTION_SUMMARY: solution_data.get("summary").get("text"),
    #                         Output.VULNERABILITY_ID: vulnerability_id,
    #                     }
    #                 )
    #             last_id += 1
    #
    #         time.sleep(params.get(Input.INTERVAL) * 10)
    #
    # @staticmethod
    # def strip_msft_id(solution_id: str) -> str:
    #     """
    #     Helper method to strip solution IDs specific to microsoft IDs
    #     to return a useful solution ID for sccm
    #
    #     :param solution_id: Solution ID
    #     :return: Regular solution ID or stripped solution ID
    #     """
    #
    #     list_x = solution_id.split("-")
    #
    #     if list_x[0] == "msft":
    #         return "-".join(list_x[2:])
    #     else:
    #         return solution_id
