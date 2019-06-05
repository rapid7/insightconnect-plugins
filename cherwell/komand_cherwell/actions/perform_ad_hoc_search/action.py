import komand
from .schema import PerformAdHocSearchInput, PerformAdHocSearchOutput
# Custom imports below


class PerformAdHocSearch(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='perform_ad_hoc_search',
                description='Runs an ad-hoc Business Object search. To execute a search with Prompts, the PromptId and Value are required in the data request object',
                input=PerformAdHocSearchInput(),
                output=PerformAdHocSearchOutput())

    def run(self, params={}):
        search_params = params["data_request"]

        response = self.connection.api.get_searchresults(search_params)

        return {
            "search_results": response
        }
