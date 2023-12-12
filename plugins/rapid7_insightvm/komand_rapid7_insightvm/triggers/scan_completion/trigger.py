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

    def run(self, params={}):
        # Write scan_id to cache
        self.logger.info("Getting latest scan...")

        site_id = params.get(Input.SITE_ID)
        first_latest_scan_id = self.find_latest_completed_scan(site_id, cached=False)

        while True:
            # Open cache
            starting_point = first_latest_scan_id

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
                        Output.VULNERABILITY_INFO: item.get("vulnerability_info"),
                    }
                )

            first_latest_scan_id = latest_scan_id

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

        results_dict = {}
        for row in csv_report:
            results_dict = Util.filter_results(params, row, results_dict)

        return list(results_dict.values())

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
            f"SELECT fasvi.scan_id, fasvi.asset_id, fasvi.vulnerability_id, dv.cvss_v3_score, dvr.source, daga.asset_group_id, dss.solution_id, dss.summary, dv.nexpose_id "  # nosec B608
            f"FROM fact_asset_scan_vulnerability_instance AS fasvi "
            f"JOIN dim_asset_group_asset AS daga ON (fasvi.asset_id = daga.asset_id) "
            f"JOIN dim_vulnerability AS dv ON (fasvi.vulnerability_id = dv.vulnerability_id) "
            f"JOIN dim_vulnerability_reference AS dvr ON (fasvi.vulnerability_id = dvr.vulnerability_id) "
            f"JOIN dim_solution AS dss ON (dv.nexpose_id = dss.nexpose_id) "
            f"WHERE fasvi.scan_id = {scan_id} "
        )


class Util:
    @staticmethod
    def filter_results(params: dict, csv_row: dict, results: dict) -> Union[None, dict]:
        """
        Filter the outputted results based on the user inputs.

        :param params: Input params
        :param csv_row: Dict row of the csv results
        :param results: New object to append results to

        :return: New object containing only the necessary fields for the required output.
        """

        # Input retrieval
        asset_group = params.get(Input.ASSET_GROUP, None)
        cve = params.get(Input.CVE, None)
        source = params.get(Input.SOURCE, None)
        cvss_score = params.get(Input.CVSS_SCORE, None)
        severity = params.get(Input.SEVERITY, None)

        # We retrieve this separately because we use it as a unique identifier for
        # the filtering process
        asset_id = int(csv_row.get("asset_id", 0))

        new_dict = {
            "asset_id": asset_id,
            "vulnerability_info": [
                {
                    "vulnerability_id": csv_row.get("vulnerability_id", ""),
                    "nexpose_id": csv_row.get("nexpose_id", ""),
                    "cvss_v3_score": csv_row.get("cvss_v3_score", 0),
                    "severity": csv_row.get("severity", ""),
                    "solution_id": Util.strip_msft_id(csv_row.get("solution_id", "")),
                    "solution_summary": csv_row.get("summary", ""),
                }
            ],
        }

        # If an input and it is not found, return None in place of the row to filter
        # out the result
        if asset_group and asset_group not in csv_row.get("asset_group_id", ""):
            return None
        if cve and cve not in csv_row.get("nexpose_id", ""):
            return None
        if source and source not in csv_row.get("source", ""):
            return None
        if cvss_score and cvss_score < csv_row.get("cvss_v3_score", 0):
            return None
        if severity and severity not in csv_row.get("severity", ""):
            return None
        # Otherwise, return the newly filtered result.

        existing_asset_id = results.get(asset_id, None)

        if existing_asset_id:
            existing_asset_id["vulnerability_info"] += new_dict["vulnerability_info"]
        else:
            results[asset_id] = new_dict

        return results

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
