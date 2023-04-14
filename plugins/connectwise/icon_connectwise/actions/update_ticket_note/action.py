import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import clean

from .schema import UpdateTicketNoteInput, UpdateTicketNoteOutput, Input, Output, Component

# Custom imports below


class UpdateTicketNote(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_ticket_note",
            description=Component.DESCRIPTION,
            input=UpdateTicketNoteInput(),
            output=UpdateTicketNoteOutput(),
        )

    def run(self, params: dict = None) -> dict:
        note_parameters = params.copy()
        ticket_id = note_parameters.pop(Input.TICKET_ID)
        note_id = note_parameters.pop(Input.NOTE_ID)
        return clean(
            {Output.TICKET_NOTE: self.connection.api_client.update_ticket_note(ticket_id, note_id, note_parameters)}
        )
