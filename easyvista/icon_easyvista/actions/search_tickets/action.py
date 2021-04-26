import insightconnect_plugin_runtime
from .schema import SearchTicketsInput, SearchTicketsOutput, Input, Output, Component

# Custom imports below


class SearchTickets(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_tickets",
            description=Component.DESCRIPTION,
            input=SearchTicketsInput(),
            output=SearchTicketsOutput(),
        )

    def run(self, params={}):
        return {Output.RESULTS: self.connection.client.search_tickets(params.get(Input.QUERY))}
