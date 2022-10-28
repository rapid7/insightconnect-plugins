import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import clean

from icon_freshdesk.util.helpers import convert_dict_keys_case, replace_ticket_fields_id_to_name
from icon_freshdesk.util.constants import Include, Ticket, TextCase
from .schema import GetTicketsInput, GetTicketsOutput, Input, Output, Component


# Custom imports below


class GetTickets(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="getTickets", description=Component.DESCRIPTION, input=GetTicketsInput(), output=GetTicketsOutput()
        )

    def run(self, params: dict = None) -> dict:
        include = params.get(Input.INCLUDE)
        include = include if include in Include.get_include_parameters_list() else None
        tickets = self.connection.api_client.get_tickets(
            predefined_filter=params.get(Input.PREDEFINEDFILTER),
            include=include,
            order_by=params.get(Input.ORDERBY),
            filter_by=convert_dict_keys_case(params.get(Input.FILTERBY, {}), TextCase.SNAKE_CASE),
            order_type=params.get(Input.ORDERTYPE),
            per_page=params.get(Input.PERPAGE),
            page=params.get(Input.PAGE),
        )
        ticket_fields = self.connection.api_client.get_ticket_fields()
        return clean(
            {
                Output.TICKETS: convert_dict_keys_case(
                    [
                        replace_ticket_fields_id_to_name(ticket, Ticket.FIELDS_TO_NAME_ID_CONVERSION, ticket_fields)
                        for ticket in tickets
                    ],
                    TextCase.CAMEL_CASE,
                )
            }
        )
