import insightconnect_plugin_runtime
from .schema import ListInactiveAssetsInput, ListInactiveAssetsOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class ListInactiveAssets(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_inactive_assets",
            description=Component.DESCRIPTION,
            input=ListInactiveAssetsInput(),
            output=ListInactiveAssetsOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)

        days_ago = params.get(Input.DAYS_AGO)
        size = params.get(Input.SIZE, 500)
        endpoint = endpoints.Asset.asset_search(self.connection.console_url)
        self.logger.info("Using %s ..." % endpoint)

        if size > 1000:
            self.logger.info("The action will return the maximum number of results: 1000")
            size = 1000

        payload = {
            "filters": [{"field": "last-scan-date", "operator": "is-earlier-than", "value": days_ago}],
            "match": "all",
        }
        assets = resource_helper.paged_resource_request(
            endpoint=endpoint, method="post", payload=payload, number_of_results=size
        )

        return {Output.ASSETS: assets}
