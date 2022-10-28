import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import clean

from icon_freshdesk.util.helpers import convert_dict_keys_case, replace_ticket_fields_id_to_name
from icon_freshdesk.util.constants import Include, Ticket, TextCase
from .schema import GetTicketByIdInput, GetTicketByIdOutput, Input, Output, Component


# Custom imports below


class GetTicketById(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="getTicketById",
            description=Component.DESCRIPTION,
            input=GetTicketByIdInput(),
            output=GetTicketByIdOutput(),
        )

    def run(self, params: dict = None) -> dict:
        include = params.get(Input.INCLUDE)
        include = include if include in Include.get_include_parameters_list() else None
        ticket = self.connection.api_client.get_ticket_by_id(ticket_id=params.get(Input.TICKETID), include=include)
        ticket_fields = self.connection.api_client.get_ticket_fields()
        return clean(
            {
                Output.TICKET: convert_dict_keys_case(
                    replace_ticket_fields_id_to_name(ticket, Ticket.FIELDS_TO_NAME_ID_CONVERSION, ticket_fields),
                    TextCase.CAMEL_CASE,
                )
            }
        )
