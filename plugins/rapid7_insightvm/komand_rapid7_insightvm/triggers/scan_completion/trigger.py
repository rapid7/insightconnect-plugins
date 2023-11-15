import insightconnect_plugin_runtime
import time
from .schema import ScanCompletionInput, ScanCompletionOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests
import uuid
from komand_rapid7_insightvm.util import util
import csv
import io
from typing import List, Union, Dict
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
        start_time = time.time()
        print(self.get_results_from_query(scan_id))
        end_time = time.time()
        print(f"Total Time: {(end_time - start_time) // 60} Minutes")
        # self.send(
        #     {
        #         Output.ASSET_ID: results.get("asset_id"),
        #         Output.IP: results.get("ip_address"),
        #         Output.HOSTNAME: results.get("hostname"),
        #         Output.VULNERABILITY_INFO: results.get("vulnerability_info"),
        #     }
        # )

    @staticmethod
    def query_results(scan_id: int):
        return (
            f"SELECT fasvi.scan_id, fasvi.asset_id, da.host_name, da.ip_address, dss.solution_id, dss.summary, dv.nexpose_id, ds.finished "
            f"FROM fact_asset_scan_vulnerability_instance fasvi "
            f"JOIN dim_asset da ON (fasvi.asset_id = da.asset_id) "
            f"JOIN dim_vulnerability dv ON (fasvi.vulnerability_id = dv.vulnerability_id) "
            f"JOIN dim_solution dss ON (dv.nexpose_id = dss.nexpose_id) "
            f"JOIN dim_scan ds ON (fasvi.scan_id = ds.scan_id) "
            f"WHERE fasvi.scan_id = {scan_id} "
            f"GROUP BY fasvi.scan_id, fasvi.asset_id, dv.nexpose_id, da.host_name, da.ip_address, dss.solution_id, dss.summary, ds.finished "
            f"ORDER BY ds.finished DESC;"
        )

    def get_results_from_query(self, scan_id: int) -> List[Dict[str, Union[str, int]]]:
        """
        Take a scan id and run a sql query to retrieve the
        information needed for the trigger output

        :param scan_id: ID of the latest scan
        :return: A dictionary containing asset_id, ip_address, hostname, and a nested array with objects
        containing vulnerability_id, solution_id & solution summary.
        """

        identifier = uuid.uuid4()
        report_payload = {
            "name": f"Rapid7-InsightConnect-ScanCompletion-{identifier}",
            "format": "sql-query",
            "query": ScanCompletion.query_results(scan_id),
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

        scan_info = []

        for row in csv_report:
            asset = {
                "scan_id": int(row['scan_id']),
                "asset_id": int(row['asset_id']),
                "hostname": row["host_name"],
                "ip_address": row["ip_address"],
                "nexpose_id": row["nexpose_id"],
                "solution_id": row["solution_id"],
                "solution_summary": row["summary"],
            }
            scan_info.append(asset)

        return scan_info

    @staticmethod
    def filter_results(asset_group: int, cve: str, hostname: str, source: str, ip_address: str, risk_score: float, site_id: str, csv_results: list):
        # Return as normal if no inputs detected
        if not asset_group and cve and hostname and source and ip_address and risk_score and site_id:
            return csv_results

        filtered_results = []

        #
        for row in csv_results:
            for values in row.values():



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
