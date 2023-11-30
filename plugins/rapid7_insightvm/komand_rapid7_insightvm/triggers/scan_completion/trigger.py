import insightconnect_plugin_runtime
import time
from .schema import ScanCompletionInput, ScanCompletionOutput, Input, Output, Component

# Custom imports below
import uuid
from komand_rapid7_insightvm.util import util
import csv
import io
import json
from typing import List, Union, Dict
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests
from komand_rapid7_insightvm.util import endpoints


class ScanCompletion(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="scan_completion",
            description=Component.DESCRIPTION,
            input=ScanCompletionInput(),
            output=ScanCompletionOutput(),
        )

    CACHE_FILE_NAME = f"site_scans_cache_{time.time()}"

    def run(self, params={}):
        start_time = time.time()

        # Write scan_id to cache
        self.logger.info("Getting latest scan..")

        site_id = params.get(Input.SITE_ID)
        latest_scan_id = self.find_latest_completed_scan(site_id)

        # Initialize trigger cache at startup
        # self.logger.info("Initialising trigger cache..")
        util.write_to_cache(self.CACHE_FILE_NAME, json.dumps(latest_scan_id))

        while True:
            # Open cache
            starting_point = Cache.get_cache_site_scans(self)
            # starting_point = 11568

            latest_scan_id = self.find_latest_completed_scan(site_id)

            # Check if latest is in cache
            print(f"Latest scan ID: {latest_scan_id} | cache site scans: {starting_point}")
            if latest_scan_id == starting_point:
                print(f"Sleeping 60 seconds")
                time.sleep(60)
                continue

            results = self.get_results_from_latest_scan(params=params, scan_id=int(latest_scan_id))

            # results = [{'asset_id': 2477, 'ip_address': '10.4.31.243', 'hostname': 'ivm-console-test', 'vuln_info': [{'vulnerability_id': '116131', 'nexpose_id': 'cifs-generic-0005', 'solution_id': '62875', 'solution_summary': 'Upgrade the CIFS authentication method'}]}]
            # Submit scan for trigger
            for item in results:
                self.send(
                    {
                        Output.ASSET_ID: item.get("asset_id"),
                        Output.IP: item.get("ip_address"),
                        Output.HOSTNAME: item.get("hostname"),
                        Output.VULNERABILITY_INFO: item.get("vuln_info"),
                    }
                )

            # Update cache
            try:
                util.write_to_cache(self.CACHE_FILE_NAME, json.dumps(latest_scan_id))
            except TypeError as error:
                raise PluginException(
                    cause="Failed to save cache to file", assistance=f"Exception returned was {error}"
                )

            end_time = time.time()
            print(f"Total Time: {(end_time - start_time) // 60} Minutes")
            # Sleep configured in minutes
            time.sleep(params.get(Input.INTERVAL, 5) * 60)

    def get_results_from_latest_scan(self, params: dict, scan_id: int) -> List[Dict[str, Union[str, int]]]:
        """
        Take a scan id and run a sql query to retrieve the
        information needed for the trigger output

        :param params:
        :param scan_id:
        :return:
        """

        identifier = uuid.uuid4()

        report_payload = {
            "name": f"Rapid7-InsightConnect-ScanCompletion-{identifier}",
            "format": "sql-query",
            "query": ScanQueries.query_results_from_latest_scan(scan_id),
            "version": "2.3.0",
        }

        self.logger.info("Getting report")
        report_contents = util.adhoc_sql_report(self.connection, self.logger, report_payload)
        try:
            csv_report = csv.DictReader(io.StringIO(report_contents["raw"]))
            print(f"CSV Report: {csv_report}")
        except Exception as error:
            raise PluginException(
                cause="Error: Failed to process query response while fetching site scans.",
                assistance=f"Exception returned was {error}",
            )

        results = []

        for row in csv_report:
            new_row = Util.filter_results(params, row)
            if new_row:
                results.append(new_row)
        results = Util.condense_results(results)
        return results

    def find_latest_completed_scan(self, site_id: str = None) -> int:
        """ """
        # Use API call for speed.
        # Super simple get the latest scan ID
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        if site_id:
            endpoint = endpoints.Scan.site_scans(self.connection.console_url, site_id)
        else:
            endpoint = endpoints.Scan.scans(self.connection.console_url)

        response = resource_helper.resource_request(endpoint=endpoint, method="get", params={"sort": "id,desc"})

        # print(f"Response zero: {response.get('resources')[0:2]}")
        for scan in response.get("resources"):
            if scan.get("status") == "finished":
                self.logger.info(f"Latest finished scan ID: {scan.get('id')}")
                return scan.get("id")

        # Handle processing


class ScanQueries:
    @staticmethod
    def query_results_from_latest_scan(scan_id):
        return (
            f"SELECT fasvi.scan_id, fasvi.asset_id, fasvi.vulnerability_id, dvr.source, da.host_name, da.ip_address, dss.solution_id, dss.summary, dv.nexpose_id, dv.riskscore "
            f"FROM fact_asset_scan_vulnerability_instance AS fasvi "
            f"JOIN dim_asset AS da ON (fasvi.asset_id = da.asset_id) "
            f"JOIN dim_vulnerability AS dv ON (fasvi.vulnerability_id = dv.vulnerability_id) "
            f"JOIN dim_vulnerability_reference AS dvr ON (fasvi.vulnerability_id = dvr.vulnerability_id) "
            f"JOIN dim_solution AS dss ON (dv.nexpose_id = dss.nexpose_id) "
            f"WHERE fasvi.scan_id = {scan_id} "
        )


class Cache:
    CACHE_FILE_NAME = f"site_scans_cache_{time.time()}"

    def get_cache_site_scans(self) -> dict:
        try:
            return json.loads(util.read_from_cache(ScanCompletion.CACHE_FILE_NAME))
        except ValueError as error:
            raise PluginException(cause="Failed to load cache file", assistance=f"Exception returned was {error}")


class Util:
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
        else:
            print(f"new dict final: {new_dct}")
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
