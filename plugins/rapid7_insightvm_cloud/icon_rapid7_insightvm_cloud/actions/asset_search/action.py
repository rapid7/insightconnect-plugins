import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import clean

from .schema import AssetSearchInput, AssetSearchOutput, Input, Output, Component
from icon_rapid7_insightvm_cloud.util.constants import CRITERIA_OPERATOR_MAP, MAX_PAGE_SIZE


class AssetSearch(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="asset_search", description=Component.DESCRIPTION, input=AssetSearchInput(), output=AssetSearchOutput()
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        asset_criteria = params.get(Input.ASSET_CRITERIA, "")
        vulnerability_criteria = params.get(Input.VULN_CRITERIA, "")
        operator_criteria = params.get(Input.CRITERIA_OPERATOR, "")
        current_time = params.get(Input.CURRENT_TIME, "")
        comparison_time = params.get(Input.COMPARISON_TIME, "")
        sort_criteria = params.get(Input.SORT_CRITERIA, {})
        size = params.get(Input.SIZE, 200)
        # END INPUT BINDING - DO NOT REMOVE

        # Setting up the JSON body for request
        json_body = {"asset": asset_criteria, "vulnerability": vulnerability_criteria}
        if all((asset_criteria, vulnerability_criteria)):
            vulnerability_query = vulnerability_criteria.replace("vulnerability.", "asset.vulnerability.")
            json_body = {
                "asset": f"{asset_criteria} {CRITERIA_OPERATOR_MAP.get(operator_criteria, '&&')} {vulnerability_query}"
            }

        query_parameters = {
            "currentTime": current_time,
            "comparisonTime": comparison_time,
        }

        # Capped Max Page Size, maximum API supports is 500 (causes timeouts)
        query_parameters["size"] = MAX_PAGE_SIZE if size >= MAX_PAGE_SIZE else size

        for key, value in sort_criteria.items():
            query_parameters["sort"] = f"{key},{value}"

        assets = []
        for page in range(0, 10_000):
            self.logger.info(f"Receiving {page} page of results...")
            query_parameters["page"] = page
            resources = self.connection.ivm_cloud_api.call_api(
                "assets", "POST", clean(query_parameters), clean(json_body)
            ).get("data", [])
            assets += resources

            # If no more records returned, then we pulled all the search results
            if not resources:
                self.logger.info("Pagination has finished.")
                break

            # If the `size` parameter is greater than 500, then we will have 500 results on each page. If we want to retrieve 502 results, then size needs to be set to 502
            # we should retrieve data from 2 pages in that case and cut off unnecessary results to return 502 of them.
            if len(assets) >= size:
                assets = assets[:size]
                break

        self.logger.info(f"Found {len(assets)} assets. Returning results...")
        return {Output.ASSETS: assets}
