"""Search Tickets action for TeamDynamix InsightConnect plugin."""

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import clean

from icon_teamdynamix.util.constants import DEFAULT_MAX_RESULTS
from .schema import SearchTicketsInput, SearchTicketsOutput, Input, Output, Component


class SearchTickets(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_tickets",
            description=Component.DESCRIPTION,
            input=SearchTicketsInput(),
            output=SearchTicketsOutput(),
        )

    def run(self, params={}):
        search_payload = {
            "MaxResults": params.get(Input.MAX_RESULTS, DEFAULT_MAX_RESULTS),
        }

        if params.get(Input.SEARCH_TEXT):
            search_payload["SearchText"] = params.get(Input.SEARCH_TEXT)
        if params.get(Input.STATUS_ID):
            search_payload["StatusIDs"] = [params.get(Input.STATUS_ID)]

        tickets = self.connection.client.search_tickets(search_payload)

        return clean(
            {
                Output.TICKETS: tickets,
                Output.COUNT: len(tickets),
            }
        )
