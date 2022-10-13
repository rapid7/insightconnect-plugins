import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import clean

from .schema import GetTicketNotesInput, GetTicketNotesOutput, Input, Output, Component

# Custom imports below


class GetTicketNotes(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_ticket_notes",
            description=Component.DESCRIPTION,
            input=GetTicketNotesInput(),
            output=GetTicketNotesOutput(),
        )

    def run(self, params: dict = None) -> dict:
        return clean(
            {
                Output.TICKET_NOTES: self.connection.api_client.get_ticket_notes(
                    ticket_id=params.get(Input.TICKET_ID),
                    page_size=params.get(Input.PAGESIZE),
                    page=params.get(Input.PAGE),
                    conditions=params.get(Input.CONDITIONS),
                )
            }
        )
