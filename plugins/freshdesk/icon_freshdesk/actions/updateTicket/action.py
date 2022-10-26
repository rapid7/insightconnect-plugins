import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import clean

from icon_freshdesk.util.constants import Ticket
from icon_freshdesk.util.helpers import (
    convert_dict_keys_case,
    add_keys_prefix,
    replace_ticket_fields_name_to_id,
    replace_ticket_fields_id_to_name,
)
from .schema import UpdateTicketInput, UpdateTicketOutput, Input, Output, Component

# Custom imports below


class UpdateTicket(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="updateTicket",
            description=Component.DESCRIPTION,
            input=UpdateTicketInput(),
            output=UpdateTicketOutput(),
        )

    def run(self, params: dict = None) -> dict:
        params_copy = params.copy()
        ticket_id = params_copy.pop(Input.TICKETID)

        ticket_fields = self.connection.api_client.get_ticket_fields()
        ticket_parameters = convert_dict_keys_case(params_copy, "snake_case")
        attachments = ticket_parameters.pop(Ticket.ATTACHMENTS, [])
        ticket_parameters[Ticket.CUSTOM_FIELDS] = add_keys_prefix(
            ticket_parameters.get(Ticket.CUSTOM_FIELDS, {}), "cf_"
        )
        ticket_parameters = replace_ticket_fields_name_to_id(
            ticket_parameters, Ticket.FIELDS_TO_NAME_ID_CONVERSION, ticket_fields
        )
        ticket = self.connection.api_client.update_ticket(ticket_id, ticket_parameters, attachments)

        return clean(
            {
                Output.TICKET: convert_dict_keys_case(
                    replace_ticket_fields_id_to_name(ticket, Ticket.FIELDS_TO_NAME_ID_CONVERSION, ticket_fields),
                    "camel_case",
                )
            }
        )
