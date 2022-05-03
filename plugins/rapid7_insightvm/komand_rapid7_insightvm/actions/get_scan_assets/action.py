import insightconnect_plugin_runtime
from .schema import GetScanAssetsInput, GetScanAssetsOutput, Input, Output, Component

# Custom imports below
import csv
import io
import uuid
from komand_rapid7_insightvm.util import util
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests
from insightconnect_plugin_runtime.exceptions import PluginException


class GetScanAssets(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_scan_assets",
            description=Component.DESCRIPTION,
            input=GetScanAssetsInput(),
            output=GetScanAssetsOutput(),
        )

    def run(self, params={}):
        # Generate unique identifier for report names
        identifier = uuid.uuid4()
        scan_id = params.get(Input.SCAN_ID)

        # Report to collect site ID and asset IDs of scan
        report_payload = {
            "name": f"Rapid7-ScanAssets-InsightConnect-{identifier}",
            "format": "sql-query",
            "query": "SELECT site_id, asset_id "
            "FROM dim_site_scan AS dss "
            "JOIN dim_asset_scan AS das ON das.scan_id = dss.scan_id",
            "version": "2.3.0",
            "scope": {"scan": scan_id},
        }

        report_contents = util.adhoc_sql_report(self.connection, self.logger, report_payload)
        self.logger.info(f"Processing Assets of Scan ID {scan_id}")

        # Extract site ID and asset IDs
        scan_asset_ids = set()
        scan_site_id = None

        try:
            csv_report = csv.DictReader(io.StringIO(report_contents["raw"]))
        except Exception as e:
            raise PluginException(
                cause=f"Error: Failed to process query response for assets returned for " f"scan ID {scan_id}.",
                assistance=f"Exception returned was {e}",
            )

        for row in csv_report:
            scan_asset_ids.add(int(row["asset_id"]))

            # Assign site ID for scan
            if scan_site_id is None:
                scan_site_id = row["site_id"]

        # Get assets of site of scan
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        search_criteria = {
            "filters": [{"field": "site-id", "operator": "in", "values": [scan_site_id]}],
            "match": "all",
        }
        self.logger.info("Performing filtered asset search with criteria %s" % search_criteria)
        endpoint = endpoints.Asset.search(self.connection.console_url)

        site_assets = resource_helper.paged_resource_request(endpoint=endpoint, method="post", payload=search_criteria)

        # Filter assets to specific scan assets
        filtered_assets = [asset for asset in site_assets if asset["id"] in scan_asset_ids]

        return {Output.ASSETS: filtered_assets}
