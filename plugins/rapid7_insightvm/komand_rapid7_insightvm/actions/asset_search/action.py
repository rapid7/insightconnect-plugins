import insightconnect_plugin_runtime
from .schema import AssetSearchInput, AssetSearchOutput, Input, Output

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class AssetSearch(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="asset_search",
            description="Search for assets using filtered asset search",
            input=AssetSearchInput(),
            output=AssetSearchOutput(),
        )

    def run(self, params={}):

        resource_helper = ResourceRequests(self.connection.session, self.logger)
        search_criteria = params.get(Input.SEARCHCRITERIA)
        size = params.get(Input.SIZE, 0)
        sort_criteria = params.get(Input.SORT_CRITERIA, dict())
        self.logger.info(f"Performing filtered asset search with criteria {search_criteria}")
        endpoint = endpoints.Asset.search(self.connection.console_url)
        parameters = list()

        for key, value in sort_criteria.items():
            parameters.append(("sort", f"{key},{value}"))

        if size == 0:
            parameters.append(("size", 100))
            resources = resource_helper.paged_resource_request(
                endpoint=endpoint, method="post", params=parameters, payload=search_criteria
            )
        elif size <= 100:
            parameters.append(("size", size))
            resources = resource_helper.resource_request(
                endpoint=endpoint, method="post", params=parameters, payload=search_criteria
            )
            resources = resources["resources"]
        else:
            parameters.append(("size", 100))
            number_of_results = size
            resources = resource_helper.paged_resource_request(
                endpoint=endpoint,
                method="post",
                params=parameters,
                payload=search_criteria,
                number_of_results=number_of_results,
            )

        return {Output.ASSETS: resources}
