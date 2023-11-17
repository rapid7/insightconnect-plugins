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

        start_time = time.time()
        print(self.get_results_from_query())
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
    def query_results(scan_id: int = 3):
        return (
            f"SELECT fasvi.scan_id, fasvi.asset_id, fasvi.status_id, daga.asset_group_id, dsa.site_id, dvr.source, dvr.reference, da.host_name, da.ip_address, dss.solution_id, dss.summary, dv.nexpose_id, dv.riskscore "
            f"FROM fact_asset_scan_vulnerability_instance AS fasvi "
            f"JOIN dim_asset da ON (fasvi.asset_id = da.asset_id) "
            f"JOIN dim_site_asset dsa ON(fasvi.asset_id = dsa.asset_id) "
            f"JOIN dim_asset_group_asset daga ON (fasvi.asset_id = daga.asset_id) "
            f"JOIN dim_vulnerability dv ON (fasvi.vulnerability_id = dv.vulnerability_id) "
            f"JOIN dim_vulnerability_reference dvr ON (fasvi.vulnerability_id = fasvi.vulnerability_id) "
            f"JOIN dim_solution dss ON (dv.nexpose_id = dss.nexpose_id) "
            f"JOIN dim_scan ds ON (fasvi.scan_id = ds.scan_id) "
            f"WHERE fasvi.scan_id = {scan_id} "
            f"AND ds.status_id = 'C' "
        )

    def get_results_from_query(self) -> List[Dict[str, Union[str, int]]]:
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
            "query": ScanCompletion.query_results(),
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
            print(row)
            # We don't need to pull back status_id because we only used it to filter completed scans

            # This is where we need to handle input filtering.
            # Luckily each row is an object so working with it should be easy.
            # If key, value != input, do not append row to output.
            inputs = {
                "asset_group_id": int(row['asset_group_id']),
                "site_id": row['source'],
                "hostname": row['host_name'],
                "ip": row['ip_address'],
                "risk_score": float(row['riskscore']),
                "cve": row['reference'],
                "source": row['source']
            }

            outputs = {
                "asset_id": int(row['asset_id']),
                "hostname": row["host_name"],
                "ip_address": row["ip_address"],
                "vulnerability_id": row["vulnerability_id"],
                "nexpose_id": row["nexpose_id"],
                "solution_id": row["solution_id"],
                "solution_summary": row["summary"],
            }
            scan_info.append(outputs)

        # We need to combine the last 3 fields into each to reduce number of entries rather than separate
        # elements for everything.
        return scan_info

    @staticmethod
    def filter_results(params: dict, csv_results: dict):
        # Return as normal if no inputs detected
        if not params:
            return csv_results


    @staticmethod
    def condense_results(results: list):
        """
        Helper method to condense vulnerability info into a nested object for the 'vulnerability info' key
        within the original objects.
        """
        merge_keys = ('scan_id', 'asset_id', 'ip_address', 'hostname')
        dct = {}

        for element in results:
            key = [element[k] for k in merge_keys]
            partial_el = {k: v for k, v in element.items() if k not in merge_keys}
            dct.setdefault(key, []).append(partial_el)

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
