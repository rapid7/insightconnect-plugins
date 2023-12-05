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
        # Write scan_id to cache
        self.logger.info("Getting latest scan...")

        site_id = params.get(Input.SITE_ID)
        latest_scan_id = self.find_latest_completed_scan(site_id, cached=False)

        # Initialize trigger cache at startup
        self.logger.info("Initialising trigger cache...")
        util.write_to_cache(self.CACHE_FILE_NAME, json.dumps(latest_scan_id))

        while True:
            # Open cache
            starting_point = Cache.get_cache_site_scans()

            latest_scan_id = self.find_latest_completed_scan(site_id, cached=True)

            # Check if latest is in cache
            if latest_scan_id == starting_point:
                self.logger.info("No new scans, sleeping 1 minute.")
                time.sleep(60)
                continue

            results = self.get_results_from_latest_scan(params=params, scan_id=int(latest_scan_id))

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

            # Sleep configured in minutes
            time.sleep(params.get(Input.INTERVAL, 5) * 60)

    def get_results_from_latest_scan(self, params: dict, scan_id: int) -> List[Dict[str, Union[str, int]]]:
        """
        Take a scan id and run a sql query to retrieve the
        information needed for the trigger output

        :param params: All of the user input params
        :param scan_id: The ID of the scan

        :return: A list of condensed and filter results for output in the trigger.
        """

        # Generate a unique name for the report
        identifier = uuid.uuid4()

        # Verify the scan_id input
        Util.verify_scan_id_input(scan_id)

        # Generate the payload for the reporting API call.
        report_payload = {
            "name": f"Rapid7-InsightConnect-ScanCompletion-{identifier}",
            "format": "sql-query",
            "query": ScanQueries.query_results_from_latest_scan(scan_id),
            "version": "2.3.0",
        }

        self.logger.info("Getting report...")
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
            new_row = Util.filter_results(params, row)
            if new_row:
                results.append(new_row)

        results = Util.condense_results(results)
        return results

    def find_latest_completed_scan(self, site_id: str, cached: bool) -> int:
        """
        Use API calls to get the latest scan ID.
        Two different endpoints depending on whether Site ID is provided as an input or not.

        :param site_id: Optional site id input
        :param cached: Boolean to indicate whether to only scan most recent 10
        :return: ID of the latest 'finished' scan
        """

        resource_helper = ResourceRequests(self.connection.session, self.logger)
        if site_id:
            endpoint = endpoints.Scan.site_scans(self.connection.console_url, site_id)
        else:
            endpoint = endpoints.Scan.scans(self.connection.console_url)

        if not cached:
            response = resource_helper.paged_resource_request(
                endpoint=endpoint, method="get", params={"sort": "id,desc"}
            )

            for scan in response:
                if scan.get("status") == "finished":
                    self.logger.info(f"Latest finished scan ID: {scan.get('id')}")
                    return scan.get("id")
        else:
            response = resource_helper.resource_request(endpoint=endpoint, method="get", params={"sort": "id,desc"})

            for scan in response.get("resources"):
                if scan.get("status") == "finished":
                    self.logger.info(f"Latest finished scan ID: {scan.get('id')}")
                    return scan.get("id")


class ScanQueries:
    @staticmethod
    def query_results_from_latest_scan(scan_id: int) -> str:
        """
        Generate an SQL query string needed to to retrieve all the necessary outputs

        :param scan_id: Scan ID to query against
        :return: The completed query string
        """

        return (
            f"SELECT fasvi.scan_id, fasvi.asset_id, fasvi.vulnerability_id, dvr.source, daga.asset_group_id, da.host_name, da.ip_address, dss.solution_id, dss.summary, dv.nexpose_id "  # nosec B608
            f"FROM fact_asset_scan_vulnerability_instance AS fasvi "
            f"JOIN dim_asset_group_asset AS daga ON (fasvi.asset_id = daga.asset_id) "
            f"JOIN dim_asset AS da ON (fasvi.asset_id = da.asset_id) "
            f"JOIN dim_vulnerability AS dv ON (fasvi.vulnerability_id = dv.vulnerability_id) "
            f"JOIN dim_vulnerability_reference AS dvr ON (fasvi.vulnerability_id = dvr.vulnerability_id) "
            f"JOIN dim_solution AS dss ON (dv.nexpose_id = dss.nexpose_id) "
            f"WHERE fasvi.scan_id = {scan_id} "
        )


class Cache:
    @staticmethod
    def get_cache_site_scans() -> dict:
        try:
            return json.loads(util.read_from_cache(ScanCompletion.CACHE_FILE_NAME))
        except ValueError as error:
            raise PluginException(cause="Failed to load cache file", assistance=f"Exception returned was {error}")


class Util:
    @staticmethod
    def filter_results(params: dict, csv_row: dict):
        """
        Filter the outputted results based on the user inputs.

        :param params: Input params
        :param csv_row: Dict row of the csv results

        :return: New object containing only the necessary fields for the required output.
        """

        # Input retrieval
        asset_group = params.get(Input.ASSET_GROUP, None)
        cve = params.get(Input.CVE, None)
        hostname = params.get(Input.HOSTNAME, None)
        source = params.get(Input.SOURCE, None)
        ip_address = params.get(Input.IP_ADDRESS, None)

        try:
            new_dct = {
                "asset_id": int(csv_row["asset_id"]),
                "ip_address": csv_row["ip_address"],
                "hostname": csv_row["host_name"],
                "vulnerability_id": csv_row["vulnerability_id"],
                "nexpose_id": csv_row["nexpose_id"],
                "solution_id": Util.strip_msft_id(csv_row.get("solution_id", "")),
                "solution_summary": csv_row["summary"],
            }
        except KeyError as error:
            raise PluginException(cause="Unable to filter results.", assistance=f"Error: {error}")

        # If an input and it is not found, return None in place of the row to filter
        # out the result
        if asset_group and asset_group not in csv_row["asset_group_id"]:
            return None
        if cve and cve not in csv_row["nexpose_id"]:
            return None
        if hostname and hostname not in csv_row["host_name"]:
            return None
        if source and source not in csv_row["source"]:
            return None
        if ip_address and ip_address not in csv_row["ip_address"]:
            return None
        # Otherwise, return the newly filtered result.
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

        for element in results:
            key = tuple(element[key_] for key_ in merge_keys)
            partial_element = {key_: value_ for key, value_ in element.items() if key_ not in merge_keys}
            dct.setdefault(key, []).append(partial_element)

        for key, value in dct.items():
            entry = dict(zip(merge_keys, key))
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

    @staticmethod
    def verify_scan_id_input(scan_id: int):
        """
        Simple helper method to verify the scan_id input for the query is a valid integer.

        :param scan_id: The scan ID.
        """

        if not isinstance(scan_id, int):
            raise PluginException(cause="Scan ID is not of type integer.", assistance="Possible SQL Injection detected")
