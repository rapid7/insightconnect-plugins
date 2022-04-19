import insightconnect_plugin_runtime
from .schema import UpdateAssetGroupSearchCriteriaInput, UpdateAssetGroupSearchCriteriaOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class UpdateAssetGroupSearchCriteria(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_asset_group_search_criteria",
            description="Updates the search criteria for an existing asset group",
            input=UpdateAssetGroupSearchCriteriaInput(),
            output=UpdateAssetGroupSearchCriteriaOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        asset_group_id = params.get("id")
        search_criteria = params.get("searchCriteria")
        endpoint = endpoints.AssetGroup.asset_group_search_criteria(self.connection.console_url, asset_group_id)
        self.logger.info(f"Using {endpoint}")

        response = resource_helper.resource_request(endpoint=endpoint, method="put", payload=search_criteria)

        return response
