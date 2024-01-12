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
            self.send({Output.SCAN_COMPLETED_OUTPUT: results})

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
            results_list.append(row)

        return results_list

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

        :param scan_id: Scan ID to query against
        :return: The completed query string
        """
        return f"""
        SELECT
           DISTINCT ON (dv.vulnerability_id, da.ip_address, da.host_name) da.ip_address AS "IP Address",
           da.host_name AS "Hostname",
           dos.description AS "Operating System",
           da.sites AS "Member of Sites",
           dv.severity AS "Severity",
           round(dv.riskscore :: numeric, 0) AS "Risk",
           round(dv.cvss_score :: numeric, 2) AS "CVSS Score",
           round(dv.cvss_v3_score :: numeric, 2) AS "CVSSv3 Score",
           dv.exploits AS "Number of Public Exploits",
           dv.malware_kits AS "Number of Malware Kits Known",
           dv.vulnerability_id AS "Vulnerability ID",
           dv.title AS "Vulnerability Name",
           proofAsText(dv.description) AS "Vulnerability Details",
           fasvf.vulnerability_instances AS "Vulnerability Count on Asset",
           dv.date_published AS "Date Vulnerability First Published",
           CURRENT_DATE - dv.date_published :: date AS "Days Since Vulnerability First Published",
           round(fava.age_in_days :: numeric, 0) AS "Days Present on Asset",
           fava.first_discovered AS "Date First Seen on Asset",
           fava.most_recently_discovered AS "Date Most Recently Seen on Asset",
           ds.solution_id AS "Solution ID",
           ds.nexpose_id AS "Nexpose ID",
           proofAsText(ds.fix) AS "Best Solution",
           ds.estimate AS "Estimated Time To Fix Per Asset",
           proofAsText(ds.solution_type) AS "Solution Type"
        FROM
           dim_asset da
           JOIN dim_operating_system dos ON dos.operating_system_id = da.operating_system_id
           JOIN fact_asset_scan_vulnerability_instance fasvi ON fasvi.asset_id = da.asset_id
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
