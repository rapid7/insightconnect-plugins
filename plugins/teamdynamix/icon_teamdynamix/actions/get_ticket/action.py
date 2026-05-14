"""Get Ticket action for TeamDynamix InsightConnect plugin."""

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean

from .schema import GetTicketInput, GetTicketOutput, Input, Output, Component


class GetTicket(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_ticket",
            description=Component.DESCRIPTION,
            input=GetTicketInput(),
            output=GetTicketOutput(),
        )

    def run(self, params={}):
        ticket_id = params.get(Input.TICKET_ID)

        response = self.connection.client.get_ticket(ticket_id)

        if not response:
            raise PluginException(
                cause=f"No ticket found with ID {ticket_id}.",
                assistance="Verify the ticket ID and application ID in your connection.",
            )

        return clean(
            {
                Output.TICKET: response,
                Output.TITLE: response.get("Title", ""),
                Output.STATUS: response.get("StatusName", ""),
                Output.TICKET_ID: response.get("ID", 0),
            }
        )
