import insightconnect_plugin_runtime
from .schema import PerformAdHocSearchInput, PerformAdHocSearchOutput, Input, Output, Component

# Custom imports below


class PerformAdHocSearch(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="perform_ad_hoc_search",
            description=Component.DESCRIPTION,
            input=PerformAdHocSearchInput(),
            output=PerformAdHocSearchOutput(),
        )

    def run(self, params={}):
        search_params = params.get(Input.DATA_REQUEST)

        response = self.connection.api.get_searchresults(search_params)

        return {Output.SEARCH_RESULTS: response}
