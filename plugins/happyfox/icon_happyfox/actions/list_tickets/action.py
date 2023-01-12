import insightconnect_plugin_runtime
from .schema import ListTicketsInput, ListTicketsOutput, Input, Output, Component

# Custom imports below
from icon_happyfox.util.constants import sort_by, TextCase
from icon_happyfox.util.helpers import clean_dict, convert_dict_keys_case


class ListTickets(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_tickets", description=Component.DESCRIPTION, input=ListTicketsInput(), output=ListTicketsOutput()
        )

    def run(self, params={}):
        minify_response = params.get(Input.MINIFYRESPONSE)
        parameters = {
            "minify_response": "true" if minify_response else "false",
            "status": params.get(Input.STATUS),
            "category": params.get(Input.CATEGORY),
            "sort": sort_by.get(params.get(Input.SORT)),
            "q": params.get(Input.QUERY),
            "page": params.get(Input.PAGE),
            "size": params.get(Input.SIZE),
        }
        if minify_response:
            return {Output.TICKETIDS: self.connection.api.list_tickets(clean_dict(parameters)).get("data")}
        return {
            Output.TICKETS: convert_dict_keys_case(
                self.connection.api.list_tickets(clean_dict(parameters)).get("data"), TextCase.CAMEL_CASE
            )
        }
