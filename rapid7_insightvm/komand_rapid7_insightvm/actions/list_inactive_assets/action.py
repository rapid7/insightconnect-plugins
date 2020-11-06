import komand
from .schema import ListInactiveAssetsInput, ListInactiveAssetsOutput, Input, Output, Component
# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class ListInactiveAssets(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_inactive_assets',
                description=Component.DESCRIPTION,
                input=ListInactiveAssetsInput(),
                output=ListInactiveAssetsOutput())

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)

        days_ago = params.get(Input.DAYS_AGO)
        endpoint = endpoints.Asset.asset_search(self.connection.console_url)
        self.logger.info("Using %s ..." % endpoint)

        payload = {
            "filters": [
                {
                    "field": "last-scan-date",
                    "operator": "is-earlier-than",
                    "value": days_ago
                }
            ],
            "match": "all"
        }
        assets = resource_helper.resource_request(endpoint, method="post", payload=payload)
        return {Output.ASSETS:assets.get("resources", [])}
