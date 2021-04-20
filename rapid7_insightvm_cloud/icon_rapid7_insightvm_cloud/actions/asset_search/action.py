import insightconnect_plugin_runtime
from .schema import AssetSearchInput, AssetSearchOutput, Input, Output, Component
# Custom imports below
from icon_rapid7_insightvm_cloud.util import endpoints
from icon_rapid7_insightvm_cloud.util.resource_requests import ResourceRequests

class AssetSearch(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='asset_search',
                description=Component.DESCRIPTION,
                input=AssetSearchInput(),
                output=AssetSearchOutput())

    def run(self, params={}):
        search_criteria = params.get(Input.SEARCHCRITERIA)
        size = params.get(Input.SIZE, 0)
        sort_criteria = params.get(Input.SORT_CRITERIA, dict())
        parameters = list()

        for key, value in sort_criteria.items():
            parameters.append(("sort", f"{key},{value}"))

        if size == 0:
            parameters.append(("size", 100))
            resources = self.connection.ivm_cloud_api.call_api_pages("assets", "POST", parameters)
        elif size <= 100:
            parameters.append(("size", size))
            resources = self.connection.ivm_cloud_api.call_api_pages("assets", "POST", parameters)
        else:
            parameters.append(("size", 100))
            resources = self.connection.ivm_cloud_api.call_api_pages("assets", "POST", parameters)

        return {Output.ASSETS: resources}
