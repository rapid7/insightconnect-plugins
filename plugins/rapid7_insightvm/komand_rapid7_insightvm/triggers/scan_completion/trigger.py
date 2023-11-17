import insightconnect_plugin_runtime
import time
from .schema import ScanCompletionInput, ScanCompletionOutput, Input, Component

# Custom imports below
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
        start_time = time.time()
        print(self.get_results_from_query(params=params))
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
            f"SELECT fasvi.scan_id, fasvi.asset_id, fasvi.vulnerability_id, ds.status_id, daga.asset_group_id, dsa.site_id, dvr.source, dvr.reference, da.host_name, da.ip_address, dss.solution_id, dss.summary, dv.nexpose_id, dv.riskscore "
            f"FROM fact_asset_scan_vulnerability_instance AS fasvi "
            f"JOIN dim_asset da ON (fasvi.asset_id = da.asset_id) "
            f"JOIN dim_site_asset dsa ON(fasvi.asset_id = dsa.asset_id) "
            f"JOIN dim_asset_group_asset daga ON (fasvi.asset_id = daga.asset_id) "
            f"JOIN dim_vulnerability dv ON (fasvi.vulnerability_id = dv.vulnerability_id) "
            f"JOIN dim_vulnerability_reference dvr ON (fasvi.vulnerability_id = dvr.vulnerability_id) "
            f"JOIN dim_solution dss ON (dv.nexpose_id = dss.nexpose_id) "
            f"JOIN dim_scan ds ON (fasvi.scan_id = ds.scan_id) "
            f"WHERE fasvi.scan_id = {scan_id} "
            f"AND ds.status_id = 'C' "
            f"LIMIT 10 "
        )

    def get_results_from_query(self, params: dict) -> List[Dict[str, Union[str, int]]]:
        """
        Take a scan id and run a sql query to retrieve the
        information needed for the trigger output

        :param params:
        :return:
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

        results = []

        for row in csv_report:
            print(row)
            self.filter_results(params=params, csv_row=row, results=results)

        # self.condense_results(results)
        return results

    @staticmethod
    def filter_results(params: dict, csv_row: dict, results: list):
        """
        Filter the outputted results based on the user inputs.

        :param params:
        :param csv_row:
        :param results:

        :return:
        """

        # Input retrieval
        asset_group = params.get(Input.ASSET_GROUP, None)
        cve = params.get(Input.CVE, None)
        hostname = params.get(Input.HOSTNAME, None)
        source = params.get(Input.SOURCE, None)
        ip_address = params.get(Input.IP_ADDRESS, None)
        risk_score = params.get(Input.RISK_SCORE, None)
        site_id = params.get(Input.SITE_ID, None)

        new_dct = {
            "asset_id": int(csv_row["asset_id"]),
            "ip_address": csv_row["ip_address"],
            "vulnerability_id": csv_row["vulnerability_id"],
            "nexpose_id": csv_row["nexpose_id"],
            "solution_id": csv_row["solution_id"],
            "solution_summary": csv_row["summary"],
        }

        # Return as normal if no inputs detected
        if not params:
            results.append(new_dct)

        else:
            if asset_group and asset_group == csv_row["asset_group_id"]:
                results.append(new_dct)
            if cve and cve == csv_row["reference"]:
                results.append(new_dct)
            if hostname and hostname == csv_row["host_name"]:
                results.append(new_dct)
            if source and source == csv_row["source"]:
                results.append(new_dct)
            if ip_address and ip_address == csv_row["ip_address"]:
                results.append(new_dct)
            if risk_score and risk_score == csv_row["riskscore"]:
                results.append(new_dct)
            if site_id and site_id == csv_row["site_id"]:
                results.append(new_dct)

        return results

    @staticmethod
    def condense_results(results: list):
        """
        TODO
        Helper method to condense vulnerability info into a nested object for the 'vulnerability info' key
        within the original objects.

        :param results:

        :return:
        """

        merge_keys = ("scan_id", "asset_id", "ip_address", "hostname")
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
