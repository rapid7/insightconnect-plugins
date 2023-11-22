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
        print(f"before find latest scan")
        latest_scan_id = self.find_latest_scan()
        print(f"after find latest scan")

        # Initialize trigger cache at startup
        self.logger.info("Initialising trigger cache..")
        util.write_to_cache(self.CACHE_FILE_NAME, json.dumps(latest_scan_id))
        print(f"write to cache hit")
        print(f"cache file: {Cache.CACHE_FILE_NAME}")
        print(f"cache file contents beginning: {util.read_from_cache(self.CACHE_FILE_NAME)}")

        while True:
            latest_scan_id = self.find_latest_scan()
            print(f"while True hit")
            # Open cache
            cache_site_scans = Cache.get_cache_site_scans(self)
            print(f"Open cache hit")

            # Check if latest is in cache
            print("Before continue")
            if latest_scan_id != cache_site_scans:
                continue
            print("After continue")

            print("before get results")
            results = self.get_results_from_latest_scan(params=params, scan_id=int(latest_scan_id))
            print("after get results")

            print("before loop")
            # Submit scan for trigger
            for item in results:
                print("in loop")
                self.send(
                    {
                        Output.ASSET_ID: item.get("asset_id"),
                        Output.IP: item.get("ip_address"),
                        Output.HOSTNAME: item.get("hostname"),
                        Output.VULNERABILITY_INFO: item.get("vuln_info"),
                    }
                )
            print("after loop")

            print(f"Results final: {results}")
            print(f"Results final type: {type(results)}")

            # Update cache
            try:
                util.write_to_cache(self.CACHE_FILE_NAME, json.dumps(latest_scan_id))
            except TypeError as error:
                raise PluginException(
                    cause="Failed to save cache to file", assistance=f"Exception returned was {error}"
                )
            print(f"cache file contents end of loop: {util.read_from_cache(self.CACHE_FILE_NAME)}")

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
        print(f"Report contents: {report_contents}")
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
            print(f"Row in csv report: {row}")
            new_row = Util.filter_results(params, row)
            print(f"New row in csv report: {new_row}")
            if new_row:
                results.append(new_row)
        print(f"Results before condense: {results}")
        results = Util.condense_results(results)
        print(f"Results after condense: {results}")
        return results

    def find_latest_scan(self) -> int:
        """

        """
        # Use API call for speed.
        # Super simple get the latest scan ID
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        endpoint = endpoints.Scan.scans(self.connection.console_url)
        response = resource_helper.resource_request(endpoint=endpoint, method="get", params={'sort': 'id,desc'})

        latest_scan_id = response.get('resources')[0].get('id')
        print(f"Latest scan ID in method: {latest_scan_id}")
        return latest_scan_id


class ScanQueries:
    @staticmethod
    def query_results_from_latest_scan(scan_id):
        return (
            f"SELECT fasvi.scan_id, fasvi.asset_id, fasvi.vulnerability_id, ds.status_id, daga.asset_group_id, dsa.site_id, dvr.source, dvr.reference, da.host_name, da.ip_address, dss.solution_id, dss.summary, dv.nexpose_id, dv.riskscore "
            f"FROM fact_asset_scan_vulnerability_instance AS fasvi "
            f"JOIN dim_asset AS da ON (fasvi.asset_id = da.asset_id) "
            f"JOIN dim_site_asset AS dsa ON (fasvi.asset_id = dsa.asset_id) "
            f"JOIN dim_asset_group_asset AS daga ON (fasvi.asset_id = daga.asset_id) "
            f"JOIN dim_vulnerability AS dv ON (fasvi.vulnerability_id = dv.vulnerability_id) "
            f"JOIN dim_vulnerability_reference AS dvr ON (fasvi.vulnerability_id = dvr.vulnerability_id) "
            f"JOIN dim_solution AS dss ON (dv.nexpose_id = dss.nexpose_id) "
            f"JOIN dim_scan AS ds ON (fasvi.scan_id = ds.scan_id) "
            f"WHERE ds.status_id = 'C' "
            f"AND ds.scan_id = {scan_id} "
            f"LIMIT 2 "
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
        print(f"Filter results start")
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
        print(f"new dict begin: {new_dct}")

        ScanCompletion.logger.info("Writing latest scan to cache..")
        util.write_to_cache(ScanCompletion.CACHE_FILE_NAME, json.dumps(csv_row["scan_id"]))

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
        print(f"condense results start")
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
        print(f"condense results end: {new_results}")
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
