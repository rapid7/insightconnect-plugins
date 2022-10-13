import insightconnect_plugin_runtime
from .schema import DeleteTicketNoteInput, DeleteTicketNoteOutput, Input, Output, Component

# Custom imports below


class DeleteTicketNote(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_ticket_note",
            description=Component.DESCRIPTION,
            input=DeleteTicketNoteInput(),
            output=DeleteTicketNoteOutput(),
        )

    def run(self, params: dict = None) -> dict:
        return {
            Output.SUCCESS: self.connection.api_client.delete_ticket_note(
                params.get(Input.TICKET_ID), params.get(Input.NOTE_ID)
            )
        }
