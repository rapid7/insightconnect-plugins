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
from typing import List, Dict, Union
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

        results = self.get_results_from_query(scan_id)
        # For the final 3, combine them into one output in spec, defined as an array of objects - need all
        # separate or do we surely they can split it??? Can they split it from front-end? I think they can

        self.send(
            {
                Output.ASSET_ID: results.get("asset_id"),
                Output.IP: results.get("ip_address"),
                Output.HOSTNAME: results.get("hostname"),
                Output.VULNERABILITY_INFO: results.get('vulnerability_info')
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

        resource_helper = ResourceRequests(self.connection.session, self.logger)

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

        scan = {}
        vuln_info = []

        for row in csv_report:
            scan["asset_id"] = int(row["asset_id"])
            scan["hostname"] = row["host_name"]
            scan["ip_address"] = row["ip_address"]

        endpoint = VulnerabilityResult.vulnerabilities_for_asset(self.connection.console_url, scan["asset_id"])
        asset_vuln_response = resource_helper.paged_resource_request(endpoint=endpoint, method="get")

        for vulnerability in asset_vuln_response:
            vulnerability_id = vulnerability.get("id")
            endpoint = Asset.asset_vulnerability_solution(
                self.connection.console_url, scan["asset_id"], vulnerability_id
            )
            solution_response = resource_helper.resource_request(endpoint=endpoint, method="get")
            solution_info = solution_response.get("resources")[0]
            vuln_info.append(
                {
                    "summary": solution_info.get("summary").get("text"),
                    "solution_id": self.strip_msft_id(solution_info.get("id")),
                    "vulnerability_id": vulnerability_id,
                }
            )
        scan["vulnerability_info"] = vuln_info

        return scan

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
