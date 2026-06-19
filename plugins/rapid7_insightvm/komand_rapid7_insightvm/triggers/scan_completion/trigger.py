import insightconnect_plugin_runtime
import time
from .schema import ScanCompletionInput, ScanCompletionOutput, Input, Output, Component

# Custom imports below
import uuid
from komand_rapid7_insightvm.util import util
import csv
import io
from typing import List, Union
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests
from komand_rapid7_insightvm.util import endpoints


class ScanCompletion(insightconnect_plugin_runtime.Trigger):
    # Safety bound on the per-poll pagination loop in find_new_completed_scans. At size=500
    # this caps a single poll at 50k scans — well above any realistic burst — and prevents
    # an infinite loop if the API keeps returning fresh pages without ever reaching the
    # high-water mark.
    _MAX_PAGES_PER_POLL = 100

    def __init__(self):
        super(self.__class__, self).__init__(
            name="scan_completion",
            description=Component.DESCRIPTION,
            input=ScanCompletionInput(),
            output=ScanCompletionOutput(),
        )

    def run(self, params={}):
        self.logger.info("Getting latest scan...")

        site_id = params.get(Input.SITE_ID)
        resource_helper = ResourceRequests(self.connection.session, self.logger, self.connection.ssl_verify)
        interval_seconds = params.get(Input.INTERVAL, 5) * 60

        last_seen_scan_id = self.find_latest_completed_scan(site_id, resource_helper)

        while True:
            # Without a high-water mark we'd paginate the entire scan history every poll, so
            # defer scanning until a baseline is established (e.g. console has no finished
            # scans yet, or only Agent scans which we skip).
            if last_seen_scan_id is None:
                last_seen_scan_id = self.find_latest_completed_scan(site_id, resource_helper)
                if last_seen_scan_id is None:
                    time.sleep(interval_seconds)
                    continue

            new_scan_ids = self.find_new_completed_scans(site_id, last_seen_scan_id, resource_helper)

            if not new_scan_ids:
                self.logger.info("No new scans, sleeping.")
            else:
                self.logger.info(f"Found {len(new_scan_ids)} new completed scan(s) to process: {new_scan_ids}")
                for scan_id in new_scan_ids:
                    results = self.get_results_from_latest_scan(scan_id=int(scan_id))
                    self.send({Output.SCAN_ID: scan_id, Output.SCAN_COMPLETED_OUTPUT: results})
                    last_seen_scan_id = scan_id

            time.sleep(interval_seconds)

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
            if item in float_keys:
                if value == "":
                    row[item] = 0
                else:
                    row[item] = float(value)

        return row

    def find_latest_completed_scan(self, site_id: str, resource_helper: ResourceRequests) -> Union[int, None]:
        """
        Get the most recent reportable finished scan ID, used as the initial high-water
        mark when the trigger starts. Two different endpoints depending on whether Site
        ID is provided as an input or not.

        :param site_id: Optional site id input
        :param resource_helper: ResourceRequests instance for API calls
        :return: ID of the latest 'finished' scan, or None if no reportable scan exists
        """
        if site_id:
            endpoint = endpoints.Scan.site_scans(self.connection.console_url, site_id)
        else:
            endpoint = endpoints.Scan.scans(self.connection.console_url)

        response = resource_helper.paged_resource_request(
            endpoint=endpoint, method="get", params={"sort": "id,desc", "size": 500, "page": 0}
        )

        for scan in response:
            if self._is_reportable_finished_scan(scan):
                self.logger.info(f"Latest finished scan ID: {scan.get('id')}")
                return scan.get("id")

        self.logger.info("No reportable finished scan found yet; will retry on next poll.")
        return None

    def find_new_completed_scans(
        self, site_id: str, last_seen_scan_id: int, resource_helper: ResourceRequests
    ) -> List[int]:
        """
        Return all 'finished' scan IDs greater than the last seen scan ID, ordered ascending
        so they can be processed in chronological order. Since the API returns scans sorted
        by ID descending, pagination stops once a scan ID at or below the high-water mark
        is encountered.

        :param site_id: Optional site id input
        :param last_seen_scan_id: High-water mark; scans with this ID or lower are skipped
        :param resource_helper: ResourceRequests instance for API calls
        :return: List of new finished scan IDs in ascending order
        """
        if site_id:
            endpoint = endpoints.Scan.site_scans(self.connection.console_url, site_id)
        else:
            endpoint = endpoints.Scan.scans(self.connection.console_url)

        new_scan_ids = []

        for page in range(self._MAX_PAGES_PER_POLL):
            response = resource_helper.resource_request(
                endpoint=endpoint, method="get", params={"sort": "id,desc", "size": 500, "page": page}
            )

            resources = response.get("resources") or []
            if not resources:
                self.logger.info("No more resources on this page, stopping pagination")
                break

            reached_known_scan = False
            for scan in resources:
                scan_id = scan.get("id")
                if scan_id is None:
                    continue
                if self._is_reportable_finished_scan(scan):
                    new_scan_ids.append(scan_id)

                # Stop when reaching the last known scan. If last_seen_scan_id is None (first run)
                # this will paginate through all historical scans up to the page cap
                # This could be optimized in future to only fetch recent scans on initial setup
                if last_seen_scan_id is not None and scan_id <= last_seen_scan_id:
                    reached_known_scan = True
                    self.logger.info(f"Reached known scan ID {last_seen_scan_id}, stopping pagination")
                    break

            page_info = response.get("page") or {}
            total_pages = page_info.get("totalPages", 0)
            if reached_known_scan or (page + 1) >= total_pages:
                break
        else:
            self.logger.warning(
                f"Reached page cap ({self._MAX_PAGES_PER_POLL}) before exhausting scan history; "
                "some completed scans may be missed this poll"
            )

        # Process oldest-first to preserve event ordering
        new_scan_ids.sort()
        return new_scan_ids

    @staticmethod
    def _is_reportable_finished_scan(scan: dict) -> bool:
        """
        Determine whether a scan is finished and eligible for SQL reporting.
        InsightVM rejects SQL reports scoped to a single scan when that scan is an
        Insight Agent scan ("When the scope of the report is a scan, agent scans
        may not be specified."), so those must be skipped.

        :param scan: Scan resource as returned by the InsightVM scans API
        :return: True if the scan is finished and not an Agent scan
        """
        return scan.get("status", "").lower() == "finished" and scan.get("scanType", "").lower() != "agent"


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
