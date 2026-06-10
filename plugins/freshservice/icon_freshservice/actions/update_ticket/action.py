import insightconnect_plugin_runtime
from .schema import UpdateTicketInput, UpdateTicketOutput, Input, Output, Component

# Custom imports below
from icon_freshservice.util.helpers import clean_dict, dict_keys_to_camel_case, dict_keys_to_snake_case


class UpdateTicket(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_ticket",
            description=Component.DESCRIPTION,
            input=UpdateTicketInput(),
            output=UpdateTicketOutput(),
        )

    def run(self, params={}):
        ticket_id = params.get(Input.TICKETID)
        attachments = params.get(Input.ATTACHMENTS)

        json_data = clean_dict(dict_keys_to_snake_case(params))
        json_data.pop("ticket_id", None)
        json_data.pop("attachments", None)

        response = self.connection.api.update_ticket(ticket_id, clean_dict(json_data))
        if attachments:
            response = self.connection.api.update_ticket(ticket_id, attachments=attachments)
        return {Output.TICKET: dict_keys_to_camel_case(response.get("ticket", {}))}
