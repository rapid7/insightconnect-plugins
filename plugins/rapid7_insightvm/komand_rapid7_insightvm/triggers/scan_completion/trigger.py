import insightconnect_plugin_runtime
import time
from .schema import ScanCompletionInput, ScanCompletionOutput, Input, Output, Component

# Custom imports below
import uuid
from komand_rapid7_insightvm.util import util
import csv
import io
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
            #
            # # Check if latest is in cache
            if latest_scan_id == starting_point:
                self.logger.info("No new scans, sleeping 1 minute.")
                time.sleep(60)
                continue

            asset_results, vuln_results = self.get_results_from_latest_scan(params=params, scan_id=int(latest_scan_id))

            # Submit scan for trigger
            self.send({Output.ASSETS: asset_results, Output.VULNERABILITY_INFO: vuln_results})

            first_latest_scan_id = latest_scan_id

            # Sleep configured in minutes
            time.sleep(params.get(Input.INTERVAL, 5) * 60)

    def get_results_from_latest_scan(self, params: dict, scan_id: int):
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

        assets_list = []
        vulnerability_list = []
        for row in csv_report:
            new_assets, new_vulns = Util.filter_results(params, row)
            assets_list.append(new_assets)
            vulnerability_list.append(new_vulns)

        # Remove duplicate assets
        assets_list = self.clean_assets_list(assets_list)

        return assets_list, vulnerability_list

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
            f"WITH matching_asset_group_ids AS (SELECT asset_id, string_agg(CAST(asset_group_id AS varchar), ',') AS asset_group_ids " # nosec B608
            f"FROM dim_asset_group_asset "
            f"GROUP BY asset_id) "
            f"SELECT fasvi.scan_id, fasvi.asset_id, fasvi.vulnerability_id, dv.nexpose_id, dv.severity, dv.cvss_v3_score, dvc.category_name, ds.solution_id, ds.summary, dvr.source "  
            f"FROM fact_asset_scan_vulnerability_instance AS fasvi "
            f"INNER JOIN dim_vulnerability AS dv ON (fasvi.vulnerability_id = dv.vulnerability_id) "
            f"INNER JOIN dim_vulnerability_category AS dvc ON (fasvi.vulnerability_id = dvc.vulnerability_id) "
            f"INNER JOIN dim_solution AS ds ON (dv.nexpose_id = ds.nexpose_id) "
            f"INNER JOIN matching_asset_group_ids AS magi ON (fasvi.asset_id = magi.asset_id) "
            f"LEFT JOIN dim_vulnerability_reference AS dvr ON (fasvi.vulnerability_id = dvr.vulnerability_id) "
            f"WHERE fasvi.scan_id = {scan_id} "
            f"GROUP BY fasvi.scan_id, fasvi.asset_id, fasvi.vulnerability_id, magi.asset_group_ids, dv.nexpose_id, dv.cvss_v3_score, dvc.category_name, ds.solution_id, ds.summary, dvr.source, dv.severity "
        )


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
        source = params.get(Input.SOURCE, None)
        cvss_score = params.get(Input.CVSS_SCORE, None)
        severity = params.get(Input.SEVERITY, None)
        category = params.get(Input.CATEGORY_NAME, "").lower()

        # We retrieve this separately because we use it as a unique identifier for
        # the filtering process
        asset_id = int(csv_row.get("asset_id", 0))

        asset_dict = {
            "asset_id": asset_id,
            "hostname": csv_row.get("host_name", ""),
            "ip_address": csv_row.get("ip_address", ""),
        }

        vulnerability_dict = {
            "vulnerability_id": csv_row.get("vulnerability_id", ""),
            "nexpose_id": csv_row.get("nexpose_id", ""),
            "cvss_v3_score": csv_row.get("cvss_v3_score", 0),
            "severity": csv_row.get("severity", ""),
            "category": csv_row.get("category_name", ""),
            "solution_id": Util.strip_msft_id(csv_row.get("solution_id", "")),
            "solution_summary": csv_row.get("summary", ""),
        }

        # If an input and it is not found, return None in place of the row to filter
        # out the result
        conditions = (
            asset_group and asset_group not in csv_row.get("asset_group_id", ""),
            cve and cve not in csv_row.get("nexpose_id", ""),
            source and source not in csv_row.get("source", ""),
            cvss_score and csv_row.get("cvss_v3_score", 0) < cvss_score,
            severity and severity not in csv_row.get("severity", ""),
            category and category not in csv_row.get("category_name", "").lower(),
            asset_group and asset_group not in csv_row.get("asset_group_id", []).split(","),
        )

        if any(conditions):
            return {}, {}

        # Otherwise, return the newly filtered result.
        return asset_dict, vulnerability_dict

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

    @staticmethod
    def clean_assets_list(assets_list: list):
        seen_asset_id = set()
        new_asset_list = []
        for obj in assets_list:
            if obj["asset_id"] not in seen_asset_id:
                new_asset_list.append(obj)
                seen_asset_id.add(obj["asset_id"])

        return new_asset_list
