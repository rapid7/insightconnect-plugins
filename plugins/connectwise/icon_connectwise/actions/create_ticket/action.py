import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import clean
from datetime import datetime

from icon_connectwise.util.constants import Ticket
from icon_connectwise.util.helpers import iso8601_to_utc_date
from .schema import CreateTicketInput, CreateTicketOutput, Input, Output, Component

# Custom imports below


class CreateTicket(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_ticket",
            description=Component.DESCRIPTION,
            input=CreateTicketInput(),
            output=CreateTicketOutput(),
        )

    def run(self, params: dict = None) -> dict:
        ticket_parameters = params.copy()
        ticket_parameters[Ticket.ESTIMATED_START_DATE] = iso8601_to_utc_date(ticket_parameters.get(Ticket.ESTIMATED_START_DATE, ""))
        ticket_parameters[Ticket.REQUIRED_DATE] = iso8601_to_utc_date(ticket_parameters.get(Ticket.REQUIRED_DATE, ""))
        ticket_parameters[Ticket.COMPANY] = {"id": ticket_parameters.pop(Input.COMPANY_ID)}
        return {Output.TICKET: clean(self.connection.api_client.create_ticket(ticket_parameters))}
