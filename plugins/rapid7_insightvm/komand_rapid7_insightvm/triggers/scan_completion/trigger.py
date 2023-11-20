import insightconnect_plugin_runtime
import time
from .schema import ScanCompletionInput, ScanCompletionOutput, Input, Output, Component

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
        results = self.get_results_from_query(params=params)
        end_time = time.time()
        print(f"Total Time: {(end_time - start_time) // 60} Minutes")

        for item in results:
            self.send(
                {
                    Output.ASSET_ID: item.get("asset_id"),
                    Output.IP: item.get("ip_address"),
                    Output.HOSTNAME: item.get("hostname"),
                    Output.VULNERABILITY_INFO: item.get("vulnerability_info"),
                }
            )

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
            new_row = self.filter_results(params, row)
            if new_row:
                results.append(new_row)

        print(f"Results before condense: {results}")
        results = self.condense_results(results)
        print(f"Results after condense: {results}")
        return results

    @staticmethod
    def filter_results(params: dict, csv_row: dict):
        """
        Filter the outputted results based on the user inputs.

        :param params:
        :param csv_row:

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
            "hostname": csv_row["host_name"],
            "vulnerability_id": csv_row["vulnerability_id"],
            "nexpose_id": csv_row["nexpose_id"],
            "solution_id": csv_row["solution_id"],
            "solution_summary": csv_row["summary"],
        }

        # Return as normal if no inputs detected
        if asset_group and asset_group not in csv_row["asset_group_id"]:
            return None
        if cve and cve not in csv_row["reference"]:
            return None
        if hostname and hostname not in csv_row["host_name"]:
            return None
        if source and source not in csv_row["source"]:
            return None
        if ip_address and ip_address not in csv_row["ip_address"]:
            return None
        if risk_score != 0 and risk_score not in csv_row["riskscore"]:
            return None
        if site_id and site_id not in csv_row["site_id"]:
            return None
        else:
            return new_dct

    @staticmethod
    def condense_results(results: list):
        """
        Helper method to condense vulnerability info into a nested object for the 'vulnerability info' key
        within the original objects.

        :param results:

        :return:
        """

        merge_keys = ("asset_id", "ip_address", "hostname")
        dct = {}
        new_results = []

        for el in results:
            key = tuple([el[k] for k in merge_keys])
            partial_el = {k: v for k, v in el.items() if k not in merge_keys}
            dct.setdefault(key, []).append(partial_el)

        for key, value in dct.items():
            entry = {k: v for (k, v) in zip(merge_keys, key)}
            entry["vuln_info"] = value
            new_results.append(entry)

        return new_results

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
