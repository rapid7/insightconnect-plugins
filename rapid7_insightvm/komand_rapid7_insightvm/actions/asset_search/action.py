import komand
from .schema import AssetSearchInput, AssetSearchOutput
# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_helper import ResourceHelper


class AssetSearch(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='asset_search',
                description='Search for assets using filtered asset search',
                input=AssetSearchInput(),
                output=AssetSearchOutput())

    def run(self, params={}):

        resource_helper = ResourceHelper(self.connection.session, self.logger)
        search_criteria = params.get('searchCriteria')
        self.logger.info("Performing filtered asset search with criteria %s" % search_criteria)
        endpoint = endpoints.Asset.search(self.connection.console_url)

        response = resource_helper.paged_resource_request(endpoint=endpoint,
                                                          method='post',
                                                          payload=search_criteria)

        return {"assets": response}
