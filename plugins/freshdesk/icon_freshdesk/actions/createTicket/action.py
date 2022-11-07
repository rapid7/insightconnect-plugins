import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean

from icon_freshdesk.util.constants import Ticket, TextCase
from icon_freshdesk.util.helpers import (
    convert_dict_keys_case,
    add_keys_prefix,
    replace_ticket_fields_name_to_id,
    replace_ticket_fields_id_to_name,
)
from .schema import CreateTicketInput, CreateTicketOutput, Input, Output, Component

# Custom imports below


class CreateTicket(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="createTicket",
            description=Component.DESCRIPTION,
            input=CreateTicketInput(),
            output=CreateTicketOutput(),
        )

    def run(self, params: dict = None) -> dict:
        if not any(
            [
                params.get(Input.REQUESTERID),
                params.get(Input.EMAIL),
                params.get(Input.PHONE),
                params.get(Input.TWITTERID),
                params.get(Input.UNIQUEEXTERNALID),
            ]
        ):
            raise PluginException(
                "Not enough input parameters were provided.",
                f"Please provide one of the {[Input.REQUESTERID, Input.EMAIL, Input.PHONE, Input.TWITTERID, Input.UNIQUEEXTERNALID]} and try again. If the issue persists, please contact support.",
            )

        ticket_fields = self.connection.api_client.get_ticket_fields()
        ticket_parameters = convert_dict_keys_case(params, TextCase.SNAKE_CASE)
        attachments = ticket_parameters.pop(Ticket.ATTACHMENTS, [])
        ticket_parameters[Ticket.CUSTOM_FIELDS] = add_keys_prefix(
            ticket_parameters.get(Ticket.CUSTOM_FIELDS, {}), "cf_"
        )
        ticket_parameters = replace_ticket_fields_name_to_id(
            ticket_parameters, Ticket.FIELDS_TO_NAME_ID_CONVERSION, ticket_fields
        )
        ticket = self.connection.api_client.create_ticket(ticket_parameters)
        if attachments:
            ticket = self.connection.api_client.update_ticket(ticket.get(Ticket.ID), attachments=attachments)

        return clean(
            {
                Output.TICKET: convert_dict_keys_case(
                    replace_ticket_fields_id_to_name(ticket, Ticket.FIELDS_TO_NAME_ID_CONVERSION, ticket_fields),
                    TextCase.CAMEL_CASE,
                )
            }
        )
