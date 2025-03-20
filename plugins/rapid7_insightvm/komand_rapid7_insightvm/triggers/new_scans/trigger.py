import insightconnect_plugin_runtime
from .schema import NewScansInput, NewScansOutput, Input, Output, Component

# Custom imports below
from collections import defaultdict
import csv
import io
import json
import re
import time
import uuid
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util import util
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests
from insightconnect_plugin_runtime.exceptions import PluginException


class NewScans(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="new_scans",
            description=Component.DESCRIPTION,
            input=NewScansInput(),
            output=NewScansOutput(),
        )

        self.CACHE_FILE_NAME = f"site_scans_cache_{time.time()}"

    def run(self, params={}):
        # Initialize trigger cache at startup
        self.logger.info("Initializing trigger cache")
        site_scans = NewScans.get_site_scans(self, params)

        # Track site and scan IDs
        track_site_scans = NewScans.get_track_site_scans(self, site_scans)

        self.logger.info(
            f"Writing state of site scans during initialization of trigger (Site regex: "
            f"{params.get(Input.SITE_NAME_FILTER)})"
        )
        util.write_to_cache(self.logger, self.CACHE_FILE_NAME, json.dumps(track_site_scans))

        while True:
            site_scans = NewScans.get_site_scans(self, params)

            # If configured, only get most recent scan ID by max ID
            if params.get(Input.MOST_RECENT_SCAN):
                for site_id, scans in site_scans.items():
                    max_scan_by_id = max(scans, key=lambda s: int(s.get("scan_id")))
                    site_scans[site_id] = [max_scan_by_id]

            # Open cache to only process previously undiscovered scan IDs
            cache_site_scans = NewScans.get_cache_site_scans(self)

            # Send scans based on configuration
            for site_id, scans in site_scans.items():
                for scan in scans:
                    # Only process scan IDs not previously cached
                    if scan.get("scan_id") in cache_site_scans.get(site_id, []):
                        continue

                    # Get scan details
                    endpoint = endpoints.Scan.scans(self.connection.console_url, scan["scan_id"])
                    scan_details = NewScans.get_scan_details(self, endpoint, scan)

                    # Add site name and id; not provided by endpoint
                    scan_details["siteId"] = scan.get("site_id")
                    scan_details["siteName"] = scan.get("site_name")

                    # Submit scan for trigger
                    self.logger.info(f"Submitting trigger event for scan (Scan ID: {scan['scan_id']})")
                    self.send({Output.SCAN: scan_details})

                    # Update cache
                    if cache_site_scans.get(site_id) is None:
                        cache_site_scans[site_id] = []
                    cache_site_scans[site_id].append(scan.get("scan_id"))

            # Update cache file
            self.logger.info("Writing to " + self.CACHE_FILE_NAME)
            try:
                util.write_to_cache(self.logger, self.CACHE_FILE_NAME, json.dumps(cache_site_scans))  # noqa: B608
            except TypeError as error:
                raise PluginException(
                    cause="Failed to save cache to file",
                    assistance=f"Exception returned was {error}",
                )

            # Sleep for configured frequency in minutes
            time.sleep(params.get(Input.FREQUENCY, 5) * 60)

    @staticmethod
    def scans_query(scan_statuses, site_ids):
        return (
            f"SELECT ds.scan_id, dss.description as status, dsscan.site_id, dsite.name as site_name "  # noqa: B608
            f"FROM dim_scan AS ds "
            f"JOIN dim_scan_status AS dss ON dss.status_id = ds.status_id "
            f"JOIN dim_site_scan AS dsscan ON dsscan.scan_id = ds.scan_id "
            f"JOIN dim_site AS dsite ON dsite.site_id = dsscan.site_id "
            f"WHERE dss.description IN ({','.join(scan_statuses)})"
            f"AND dsite.site_id IN ({','.join(site_ids)})"
        )

    def get_cache_site_scans(self) -> dict:
        try:
            return json.loads(util.read_from_cache(self.logger, self.CACHE_FILE_NAME))
        except ValueError as error:
            raise PluginException(
                cause="Failed to load cache file",
                assistance=f"Exception returned was {error}",
            )

    def get_track_site_scans(self, site_scans: dict) -> dict:
        track_site_scans = {}
        for site_id, scan_details in site_scans.items():
            track_site_scans[site_id] = [scan["scan_id"] for scan in scan_details]
        return track_site_scans

    def get_scan_details(self, endpoint: str, scan: dict) -> dict:
        response = self.connection.session.get(url=endpoint, verify=self.connection.ssl_verify)
        if response.status_code in [200, 201]:  # 200 is documented, 201 is undocumented
            try:
                scan_details = response.json()
            except json.decoder.JSONDecodeError as error:
                raise PluginException(
                    cause=f"Error: Failed to parse response while retrieving scan "
                    f"details for scan ID {scan['scan_id']}.",
                    assistance=f"Exception returned was {error}",
                )
        else:
            raise PluginException(
                cause=f"ERROR: Failed to retrieve scan ID {scan['scan_id']}.",
                assistance=f"Status code returned was {response.status_code}",
            )
        return scan_details

    def get_sites_within_scope(self, site_regex):
        resource_helper = ResourceRequests(self.connection.session, self.logger, self.connection.ssl_verify)
        endpoint = endpoints.Site.sites(self.connection.console_url)

        sites = resource_helper.paged_resource_request(endpoint=endpoint)
        # Filter sites by regex
        regex = re.compile(site_regex, re.IGNORECASE)
        site_ids = []
        for s in sites:
            if regex.match(s["name"]):
                site_ids.append(s["id"])
        self.logger.info(f"Identified {len(site_ids)} sites within trigger scope based on regular expression filter")

        return site_ids

    def get_site_scans(self, params):
        # Generate unique identifier for report names
        identifier = uuid.uuid4()

        # Gather site IDs of sites that match regular expression
        site_ids = NewScans.get_sites_within_scope(self, params.get(Input.SITE_NAME_FILTER))

        # Gather sites and corresponding site IDs in scope
        report_payload = {
            "name": f"Rapid7-InsightConnect-NewScans-{identifier}",
            "format": "sql-query",
            "query": NewScans.scans_query(
                map(lambda x: "'" + x + "'", params.get(Input.STATUS_FILTER)),
                [str(site_id) for site_id in site_ids],
            ),
            "version": "2.3.0",
        }

        # Run report to get scans based on sites in scope
        # This is preferred over API endpoints due to endpoints returning all scans for agent site
        self.logger.info("Pulling scans")
        report_contents = util.adhoc_sql_report(self.connection, self.logger, report_payload)

        site_scans = defaultdict(list)
        try:
            csv_report = csv.DictReader(io.StringIO(report_contents["raw"]))
        except Exception as e:
            raise PluginException(
                cause="Error: Failed to process query response while fetching site scans.",
                assistance=f"Exception returned was {e}",
            )

        # Identify all scans that match sites from regular expression and status filter
        for row in csv_report:
            site_scan = {
                "scan_id": int(row["scan_id"]),
                "status": row["status"],
                "site_id": int(row["site_id"]),
                "site_name": row["site_name"],
            }
            site_scans[row["site_id"]].append(site_scan)

        return site_scans
