import komand
from .schema import AssetSearchInput, AssetSearchOutput, Input, Output
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
        search_criteria = params.get(Input.SEARCHCRITERIA)
        size = params.get(Input.SIZE, 0)
        sort = params.get(Input.SORT, '')
        self.logger.info(f'Performing filtered asset search with criteria {search_criteria}')
        endpoint = endpoints.Asset.search(self.connection.console_url)

        if size == 0:
            parameters = {'sort': sort}
            resources = resource_helper.paged_resource_request(endpoint=endpoint,
                                                               method='post', params=parameters,
                                                               payload=search_criteria)
        elif size <= 100:
            parameters = {'size': size, 'sort': sort}
            resources = resource_helper.resource_request(endpoint=endpoint,
                                                         method='post', params=parameters,
                                                         payload=search_criteria)
            resources = resources['resources']
        else:
            resources = []
            current_page = 0
            page_size = 100
            results_retreved = 0
            while results_retreved <= size:
                if results_retreved + page_size > size:
                    page_size = size - results_retreved
                self.logger.info(f"Fetching results from page {current_page}")
                parameters = {'sort': sort, 'page': current_page, 'size': page_size}
                response = resource_helper.get_resource_page(endpoint=endpoint,
                                                             method='post', params=parameters,
                                                             payload=search_criteria)

                resources += response.resources  # Grab resources and append to total
                results_retreved += len(response.resources)
                if (response.total_pages == 0) or ((response.total_pages - 1) == response.page_num):
                    self.logger.info("All pages consumed, returning results...")
                    break  # exit the loop
                else:
                    self.logger.info("More pages exist, fetching...")
                    current_page += 1

        return {Output.ASSETS: resources}
