import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import clean
from .schema import FilterTicketsInput, FilterTicketsOutput, Input, Output, Component
# Custom imports below


class FilterTickets(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="filterTickets",
                description=Component.DESCRIPTION,
                input=FilterTicketsInput(),
                output=FilterTicketsOutput())

    def run(self, params={}):
        query = params.get(Input.QUERY)
        page = params.get(Input.PAGE)
        response_json = self.connection.api_client.filter_tickets(query, page)

        return {
            Output.TOTAL: response_json.get("total", 0),
            Output.RESULTS: clean(response_json.get("results", [])),
        }
