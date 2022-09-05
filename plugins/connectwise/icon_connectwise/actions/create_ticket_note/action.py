import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import clean

from .schema import CreateTicketNoteInput, CreateTicketNoteOutput, Input, Output, Component

# Custom imports below


class CreateTicketNote(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_ticket_note",
            description=Component.DESCRIPTION,
            input=CreateTicketNoteInput(),
            output=CreateTicketNoteOutput(),
        )

    def run(self, params: dict = None) -> dict:
        note_parameters = params.copy()
        ticket_id = note_parameters.pop(Input.TICKET_ID)
        return clean({Output.TICKET_NOTE: self.connection.api_client.create_ticket_note(ticket_id, note_parameters)})
