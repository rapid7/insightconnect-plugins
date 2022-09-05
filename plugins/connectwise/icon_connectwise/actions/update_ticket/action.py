import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import clean

from icon_connectwise.util.helpers import iso8601_to_utc_date
from icon_connectwise.util.constants import Ticket
from .schema import UpdateTicketInput, UpdateTicketOutput, Input, Output, Component

# Custom imports below


class UpdateTicket(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_ticket",
            description=Component.DESCRIPTION,
            input=UpdateTicketInput(),
            output=UpdateTicketOutput(),
        )

    def run(self, params: dict = None):
        ticket_parameters = params.copy()
        ticket_id = ticket_parameters.pop(Input.TICKET_ID)
        ticket_parameters[Ticket.ESTIMATED_START_DATE] = iso8601_to_utc_date(ticket_parameters.get(Ticket.ESTIMATED_START_DATE, ""))
        ticket_parameters[Ticket.REQUIRED_DATE] = iso8601_to_utc_date(ticket_parameters.get(Ticket.REQUIRED_DATE, ""))
        ticket_parameters[Ticket.COMPANY] = {"id": ticket_parameters.pop(Input.COMPANY_ID, None)}
        ticket_parameters[Ticket.PRIORITY] = {"id": ticket_parameters.pop(Input.PRIORITY_ID, None)}
        return {Output.TICKET: clean(self.connection.api_client.update_ticket(ticket_id, ticket_parameters))}
