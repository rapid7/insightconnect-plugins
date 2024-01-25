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

            # Check if latest is in cache
            if latest_scan_id == starting_point:
                self.logger.info("No new scans, sleeping 1 minute.")
                time.sleep(60)
                continue

            results = self.get_results_from_latest_scan(scan_id=int(latest_scan_id))

            # Submit scan for trigger
            self.send({Output.SCAN_ID: latest_scan_id, Output.SCAN_COMPLETED_OUTPUT: results})

            first_latest_scan_id = latest_scan_id

            # Sleep configured in minutes
            time.sleep(params.get(Input.INTERVAL, 5) * 60)

    def get_results_from_latest_scan(self, scan_id: int):
        """
        Take a scan id and run a sql query to retrieve the
        information needed for the trigger output

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
            "scope": {"scan": scan_id},
            "query": ScanQueries.query_results_from_latest_scan(),
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

        results_list = []

        for row in csv_report:
            row = self.filter_results(row)
            results_list.append(row)

        return results_list

    @staticmethod
    def filter_results(row: dict) -> dict:
        """
        Helper method to convert relevant fields to their appropriate type

        :param row: A row within the csv report
        :return: The row with the fields converted
        """
        int_keys = (
            "riskscore",
            "exploits",
            "malware_kits",
            "vulnerability_id",
            "vulnerability_instances",
            "days_since_vuln_first_published",
            "days_present_on_asset",
            "solution_id",
        )
        float_keys = ("cvss_score", "cvss_v3_score")

        for item, value in row.items():
            if item in int_keys:
                row[item] = int(value)
            if item == "member_of_sites":
                row[item] = value.split(",")
            if item == float_keys:
                if row[item] == "":
                    row[item] = 0
                else:
                    row[item] = float(value)

        return row

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
    def query_results_from_latest_scan() -> str:
        """
        Generate an SQL query string needed to to retrieve all the necessary outputs

        :return: The completed query string
        """
        return """SELECT 
    DISTINCT ON (dv.vulnerability_id, da.ip_address, da.host_name) da.ip_address AS "ip_address",
    da.host_name AS "hostname",
    dos.description AS "os",
    da.sites AS "member_of_sites",
    dv.severity AS "severity",
    round(dv.riskscore :: numeric, 0) AS "riskscore",
    round(dv.cvss_score :: numeric, 2) AS "cvss_score",
    round(dv.cvss_v3_score :: numeric, 2) AS "cvss_v3_score",
    dv.exploits AS "exploits",
    dv.malware_kits AS "malware_kits",
    dv.vulnerability_id AS "vulnerability_id",
    dv.title AS "vulnerability_name",
    proofAsText(dv.description) AS "vulnerability_details",
    fasvf.vulnerability_instances AS "vulnerability_instances",
    dv.date_published AS "vuln_first_published",
    CURRENT_DATE - dv.date_published :: date AS "days_since_vuln_first_published",
    round(fava.age_in_days :: numeric, 0) AS "days_present_on_asset",
    fava.first_discovered AS "date_first_seen_on_asset",
    fava.most_recently_discovered AS "date_most_recently_seen_on_asset",
    ds.solution_id AS "solution_id",
    ds.nexpose_id AS "nexpose_id",
    proofAsText(ds.fix) AS "best_solution",
    ds.estimate AS "est_time_to_fix",
    proofAsText(ds.solution_type) AS "solution_type"
 FROM
    dim_asset da
    JOIN dim_operating_system dos ON dos.operating_system_id = da.operating_system_id
    JOIN dim_asset_vulnerability_best_solution davbs ON davbs.asset_id = da.asset_id
    JOIN dim_solution ds ON ds.solution_id = davbs.solution_id
    JOIN dim_vulnerability dv ON dv.vulnerability_id = davbs.vulnerability_id
    JOIN dim_vulnerability_reference dvf ON dvf.vulnerability_id = dv.vulnerability_id
    JOIN fact_asset_vulnerability_age fava ON dv.vulnerability_id = fava.vulnerability_id
    JOIN fact_asset_vulnerability_finding fasvf ON dv.vulnerability_id = fasvf.vulnerability_id
    WHERE dvf.source IN ('MSKB','MS')
        """  # nosec B608


class Util:
    @staticmethod
    def verify_scan_id_input(scan_id: int):
        """
        Simple helper method to verify the scan_id input for the query is a valid integer.

        :param scan_id: The scan ID.
        """

        if not isinstance(scan_id, int):
            raise PluginException(cause="Scan ID is not of type integer.", assistance="Possible SQL Injection detected")
